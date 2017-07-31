import os

from PIL import Image
from PIL import ImageFile

"""
Geometrizes the given image file, saving the resulting geometrized image to another file.

:Example:

>>> geometrize('file_in.jpg', 'file_out.jpg', "@Geometrizer 300 circles, 200 rectangles, 50 rotated rectangles")
>>> geometrize('another_file_in.jpg', 'file_out.jpg', "")

:param filename_in: the file that Geometrize will read in as the target image.
:param filename_out: the file that Geometrize will write out after geometrizing the target image.
:param options: the Geometrize options. This is a human-readable string that may contain key-value pairs - usually the body of a tweet.
:return True if the file was geometrized successfully, else false.
"""
def geometrize(filename_in, filename_out, options):
    print("Will geometrize image: " + filename_in " and save it as: " + filename_out + " for options: " + options)

    # TODO
    command = '../geometrize/Geometrize.exe'

    return True