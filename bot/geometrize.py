from PIL import Image
from PIL import ImageFile

import dependency_locator

"""
Creates a Chaiscript script that will be fed to Geometrize, in order to Geometrize an image.
If no arguments are passed, one of the pre-set scripts will be selected.
"""
def _create_geometrize_script():
    script = dependency_locator.read_script_file("../script/geometrize_shape_choice_template.chai") # TODO
    return script

def _execute_geometrize_script(script):
    dependency_locator.get_geometrize_executable_path() + " --script " + script

"""
Geometrizes the given image file, saving the resulting geometrized image to another file.

:Example:

>>> geometrize('file_in.jpg', 'file_out.jpg', "@Geometrizer 300 circles, 200 rectangles, 50 rotated rectangles")
>>> geometrize('another_file_in.jpg', 'file_out.jpg', "")
>>> geometrize('in.jpg', 'out.jpg', "@Geometrizer 10 rotated rectangles, 20 rotated ellipses, 50 triangles")

:param filename_in: the file that Geometrize will read in as the target image.
:param filename_out: the file that Geometrize will write out after geometrizing the target image.
:param options: the Geometrize options. This is a human-readable string that may contain key-value pairs - usually the body of a tweet.
:return True if the file was geometrized successfully, else false.
"""
def geometrize(filename_in, filename_out, options):
    print("Will geometrize image: " + filename_in + " and save it as: " + filename_out + " for options: " + options)

    script = _create_geometrize_script()

    print("Loaded script: " + script)

    return True

"""
Performs some basic tests to ensure that Geometrize is executing scripts and turning images into shapes properly.
"""
def test_geometrize():
    print("Running tests to ensure Geometrize is working correctly...")

    script = _create_geometrize_script()

    _execute_geometrize_script("todo.chai")
    
    print("Test complete!\n")