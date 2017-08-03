## @package image_console_printer
#  This module contains code that converts image data to formats suitable for printing to console.
#  Based on https://github.com/hit9/img2txt by @hit9 with minor modifications, BSD license as follows:

# Copyright (c) 2013 - 2016, hit9
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#   * Neither the name of img2txt nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys

from PIL import Image

def _alpha_blend(src, dst):
    # Does not assume that dst is fully opaque
    # See https://en.wikipedia.org/wiki/Alpha_compositing - section on "Alpha Blending"
    src_multiplier = (src[3] / 255.0)
    dst_multiplier = (dst[3] / 255.0) * (1 - src_multiplier)
    result_alpha = src_multiplier + dst_multiplier
    if result_alpha == 0:       # special case to prevent div by zero below
        return (0, 0, 0, 0)
    else:
        return (
            int(((src[0] * src_multiplier) + (dst[0] * dst_multiplier)) / result_alpha), 
            int(((src[1] * src_multiplier) + (dst[1] * dst_multiplier)) / result_alpha),
            int(((src[2] * src_multiplier) + (dst[2] * dst_multiplier)) / result_alpha),
            int(result_alpha * 255) 
        ) 
           
def _generate_grayscale_for_image(pixels, width, height, bgcolor):

    # grayscale
    color = "MNHQ$OC?7>!:-;. "

    string = ""
    # first go through the height,  otherwise will rotate
    for h in range(height):
        for w in range(width):

            rgba = pixels[w, h]

            # If partial transparency and we have a bgcolor, combine with bg
            # color
            if rgba[3] != 255 and bgcolor is not None:
                rgba = _alpha_blend(rgba, bgcolor)

            # Throw away any alpha (either because bgcolor was partially
            # transparent or had no bg color)
            # Could make a case to choose character to draw based on alpha but
            # not going to do that now...
            rgb = rgba[:3]

            string += color[int(sum(rgb) / 3.0 / 256.0 * 16)]

        string += "\n"

    return string

def print_image_to_console(img):
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    fill_string = "\x1b[49m"
    fill_string += "\x1b[K"          # does not move the cursor
    sys.stdout.write(fill_string)

    pixels = img.load()
    sys.stdout.write(_generate_grayscale_for_image(pixels, img.width, img.height, None))

    # Undo residual color changes, output newline because
    # generate_ANSI_from_pixels does not do so
    # removes all attributes (formatting and colors)
    sys.stdout.write("\x1b[0m\n")