from subprocess import call

from PIL import Image
from PIL import ImageFile

import dependency_locator

"""
Reads a Chaiscript script out of the Twitter bot scripts folder to feed to Geometrize.
If no arguments are passed, one of the pre-set scripts will be selected.
"""
def _read_geometrize_script(filename):
    filepath = dependency_locator.get_geometrize_script_folder_absolute_path() + filename
    return dependency_locator.read_script_file(filepath)

"""
Replaces all instances of a symbol in the given code with the given value.
"""
def _replace_symbol(code, symbol, value):
    code.replace(symbol, value)
    return code

"""
Replaces all instances of symbols in the code from the given dictionary with their corresponding values.
"""
def _replace_symbols(code, dict):
    for key, value in d.items():
        code = _replace_symbol(key, value)

"""
Executes the given script source code.
:return The Geometrize process return code, 0 indicates success.
"""
def _execute_geometrize_code(code):
    executable_path = dependency_locator.get_geometrize_executable_path()
    script_inline_flag = "--script_inline"
    return call([executable_path, script_inline_flag, code])

"""
Geometrizes the given image file, saving the resulting geometrized image to another file.

:Example:

>>> geometrize('file_in.jpg', 'file_out.jpg', "@Geometrizer 300 circles, 200 rectangles, 50 rotated rectangles")
>>> geometrize('another_file_in.jpg', 'file_out.jpg', "")
>>> geometrize('in.jpg', 'out.jpg', "@Geometrizer 10 rotated rectangles, 20 rotated ellipses, 50 triangles")
:param options: the Geometrize options. This is a human-readable string that may contain key-value pairs - usually the body of a tweet.
:return True if the file was geometrized successfully, else false.
"""
def geometrize(filename_in, filename_out, options):
    print("Will geometrize image: " + filename_in + " and save it as: " + filename_out + " for options: " + options)

    script = _read_geometrize_script("/geometrize_test_script.chai")

    print("Loaded script: " + script)

    return True

"""
Performs some basic tests to ensure that Geometrize is executing scripts and turning images into shapes properly.
:return True if the tests succeeded, else false.
"""
def test_geometrize():
    code = _read_geometrize_script("/geometrize_test_script.chai")
    ret_code = _execute_geometrize_code(code)

    return ret_code == 0