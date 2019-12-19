## @package dependency_locator
#  Module with functionality for locating the Geometrize executable and other dependencies.

import os
import re
from sys import platform

## Gets an absolute path to where we expect to find the Geometrize executable.
def _get_geometrize_absolute_path():
    baseDir = os.path.normpath(os.path.join(os.path.dirname(__file__), "../geometrize/")).replace('\\', '/')
    
    possibleExecutables = [name for name in os.listdir(baseDir) if re.match(r'[G|g]eometrize.*', name)]
    
    if len(possibleExecutables) > 1:
        print("Warning, found multiple Geometrize executables: " + str(possibleExecutables))
    
    if not possibleExecutables:
        print("Failed to find a path to the Geometrize executable")    
    if platform == "linux" or platform == "linux2" or platform == "darwin" or platform == "win32":
        return baseDir + "/" + possibleExecutables[0]
    else:
        print("Warning, the Geometrize bot might not work on this OS")
        
    return baseDir + "/" + possibleExecutables[0]
        

## Gets the absolute path to where we expect to find the Geometrize executable.
def get_geometrize_executable_path():
    return _get_geometrize_absolute_path()

## Checks if the Geometrize executable exists.
## Returns true if the Geometrize executable exists at the expected location, else false.
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
