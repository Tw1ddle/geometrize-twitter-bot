## @package geometrize
#  Module that interfaces with the Geometrize executable, composing and executing scripts on it to geometrize images.

from subprocess import call

from PIL import Image

import dependency_locator
import image_console_printer
import script_wrangler

## Executes the given script source code.
## :return The Geometrize process return code, 0 indicates success.
def _run_geometrize_script(code):
    executable_path = dependency_locator.get_geometrize_executable_path()
    script_inline_flag = "--script_inline"
    return call([executable_path, script_inline_flag, code])

def _compose_image_path(filename):
    return dependency_locator.get_geometrize_image_file_absolute_path(filename)

## Loads up an image from the given filepath.
## :return The loaded image, or None if the image failed to load.
def _load_image(filepath):
    image = None
    print("Loading image from: " + filepath)
    try:
        image = Image.open(filepath)
    except:
        print("Failed to load image")
    return image

## Performs some basic tests to ensure that Geometrize can run scripts and turn images into shapes properly.
## :return True if the tests succeeded, else false.
def test_geometrize():
    print("Loading test script")
    code = dependency_locator.read_geometrize_script("geometrize_test_script.chai")
    if not code:
        print("Failed to read test script, test will fail")
        return False

    image_in = _compose_image_path("test_image_in.png")
    image_out = _compose_image_path("test_image_out.png")

    print("Loading input image")
    input_image = _load_image(image_in)
    if input_image is None:
        print("Failed to read the input image, test script will fail")
        return False

    print("Replacing script tags")

    # Note that the backslashes in image paths need to be escaped, or just use forward slashes.
    # This is because we are putting them into string literals in the scripts.
    code = script_wrangler.replace_tag(code, "::IMAGE_INPUT_PATH::", image_in)
    code = script_wrangler.replace_tag(code, "::IMAGE_OUTPUT_PATH::", image_out)

    if(script_wrangler.find_tags(code) != set()):
        print("Failed to replace all template tags in script, test script will fail")
        return False

    print("Running test script")
    ret_code = _run_geometrize_script(code)

    if ret_code != 0:
        print("Failed to execute test script")
        return False

    print("Checking if the test script saved the result image correctly")

    result_image = _load_image(image_out)
    if result_image is None:
        print("Failed to read the resulting geometrized image, test script will fail")
        return False

    print("Printing result image to console\r\n")
    image_console_printer.print_image_to_console(input_image)

    print("Printing test results to console\r\n")
    image_console_printer.print_image_to_console(result_image)

    return True