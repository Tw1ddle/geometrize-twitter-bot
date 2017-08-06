## @package geometrize
#  Module that interfaces with the Geometrize executable, composing and executing scripts on it to geometrize images.

from subprocess import call

from PIL import Image

import dependency_locator
import image_console_printer
import script_wrangler

## Executes the given script source code.
## :return The Geometrize process return code, 0 indicates success.
def _run_geometrize_code(code):
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

## Executes the given script source code.
## :return True if the script executed successfully, else false.
def run_geometrize(code, tags = None):
    if tags is not None:
        code = script_wrangler.replace_tags(code, tags)

    if(script_wrangler.code_contains_tags(code)):
        print("Script has template tags that have not been replaced, will fail rather than run script")
        return False

    print("Will run script")
    print(code)
    ret_code = _run_geometrize_code(code)

    if ret_code != 0:
        print("Failed to execute test script")
        return False

    return True

## Performs some basic tests to ensure that Geometrize can run scripts and turn images into shapes properly.
## :return True if the tests executed successfully, else false.
def test_geometrize():
    print("Loading test script")
    code = dependency_locator.read_geometrize_script("geometrize_test_script.chai")
    if not code:
        print("Failed to read test script, test will fail")
        return False

    image_input_path = _compose_image_path("test_image_in.png")
    image_output_path = _compose_image_path("test_image_out.png")

    print("Loading input image")
    input_image = _load_image(image_input_path)
    if input_image is None:
        print("Failed to read the input image, test script will fail")
        return False

    print("Replacing script tags")

    # Note that the backslashes in image paths need to be escaped, or just use forward slashes.
    # This is because we are putting them into string literals in the scripts.
    code = script_wrangler.replace_tag(code, "::IMAGE_INPUT_PATH::", image_input_path)
    code = script_wrangler.replace_tag(code, "::IMAGE_OUTPUT_PATH::", image_output_path)

    if(script_wrangler.code_contains_tags(code)):
        print("Failed to replace all template tags in script, script will fail")
        return False

    if(script_wrangler.code_contains_tags(code)):
        print("Failed to replace all template tags in script, script will fail")
        return False
    
    ret_code = _run_geometrize_code(code)

    if ret_code != 0:
        print("Failed to execute test script")
        return False

    print("Checking if the test script saved the result image correctly")

    output_image = _load_image(image_output_path)
    if output_image is None:
        print("Failed to read the resulting geometrized image, test script will fail")
        return False

    print("Printing result image to console\r\n")
    image_console_printer.print_image_to_console(input_image)

    print("Printing test results to console\r\n")
    image_console_printer.print_image_to_console(output_image)

    return True