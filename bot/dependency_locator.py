## @package dependency_locator
#  Module with functionality for locating the Geometrize executable and other dependencies.

import os
from sys import platform

## Gets a relative path to the Geometrize executable.
def _get_geometrize_relative_path():
    if platform == "linux" or platform == "linux2":
        return "../geometrize/Geometrize"
    elif platform == "darwin":
        return "../geometrize/Geometrize.app"
    elif platform == "win32":
        return "../geometrize/Geometrize.exe"
    else:
        print("Warning, the Geometrize bot might not work on this OS")
        return "../geometrize/Geometrize"

## Gets the absolute path to where we expect to find the Geometrize executable.
def get_geometrize_executable_path():
    relative_path = _get_geometrize_relative_path()
    baseDir = os.path.dirname(__file__)
    return os.path.normpath(os.path.join(baseDir, _get_geometrize_relative_path())).replace('\\', '/')

## Returns true if the Geometrize executable exists at an expected location, else false.
def geometrize_executable_exists():
    return os.path.exists(get_geometrize_executable_path())

## Returns the absolute path the bot image data folder.
def get_geometrize_image_folder_absolute_path():
    baseDir = os.path.dirname(__file__)
    return os.path.normpath(os.path.join(baseDir, "../image_data/")).replace('\\', '/')

## Composes an absolute path for an image file in the image data folder.
def get_geometrize_image_file_absolute_path(filename):
    filepath = os.path.normpath(os.path.join(get_geometrize_image_folder_absolute_path(), filename)).replace('\\', '/')
    return filepath

## Gets an absolute path to the bot scripts folder.
def get_geometrize_script_folder_absolute_path():
    baseDir = os.path.dirname(__file__)
    return os.path.normpath(os.path.join(baseDir, "../script/")).replace('\\', '/')

## Reads a Chaiscript script file at the given location, returning the text content of the file.
## :return An empty string if we failed to read the script.
def read_script_file(filepath):
    with open(filepath, 'r') as content_file:
        content = content_file.read()
        return content
    
    print("Failed to read Geometrize script at: " + filepath)
    return ""

## Reads a Chaiscript script file out of the Twitter bot scripts folder, returning the text content of the file.
## :return An empty string if we failed to read the script.
def read_geometrize_script(filename):
    filepath = os.path.normpath(os.path.join(get_geometrize_script_folder_absolute_path(), filename)).replace('\\', '/')
    return read_script_file(filepath)