## @package script_wrangler
#  This module contains code that manipulates ChaiScript template scripts to be executed by Geometrize.
#  The purpose of this is to find and replace tags in scripts e.g. ::IMAGE_INPUT_PATH:: to "path/to/image.png"

import re

## Replaces all instances of a template ::TAG:: in the given code with the given value.
def replace_tag(code, tag, value):
    return code.replace(tag, value)

## Replaces all instances of template ::TAG::s in the code from the given dictionary with their corresponding values.
def replace_tags(code, dict):
    for key, value in dict.items():
        code = replace_tag(code, key, value)
    return code

## Returns a set of all the template ::TAG::s found in the given code.
def find_tags(code):
    tag_set = set()
    
    for match in re.finditer(r"::(.+?)::", code):
        tag_set.add(match.group())

    return tag_set

## Returns true if the given code contains any ::TAG::s, else false.
def code_contains_tags(code):
    return find_tags == set()