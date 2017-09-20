## @package tweet_parser
#  This module contains code that reads tweet text and figures out how the bot should do in response.

import random
import re

_rect_keywords = [ "rect", "rects", "rectangle", "rectangles" ]
_rotated_rect_keywords = [ "rotated_rect", "rotated_rects", "rotated_rectangle", "rotated_rectangles" ]
_triangle_keywords = [ "tri", "tris", "triangle", "triangles" ]
_ellipse_keywords = [ "ellipse", "ellipses" ]
_rotated_ellipse_keywords = [ "rotated_ellipse", "rotated_ellipses" ]
_circle_keywords = [ "circ", "circs", "circle", "circles" ]
_line_keywords = [ "line", "lines" ]
_quadratic_bezier_keywords = [ "bezier", "beziers", "quadratic_bezier", "quadratic_beziers" ]
_polyline_keywords = [ "polyline", "polylines" ]

## Returns true if the given string represents an integer value
def _represents_int(s):
    return re.match(r"[-+]?\d+$", s) is not None

## Clamps the given number within the range smallest, largest
def _clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

## Adds the given items to the given dictionary, mapping each keyword to the given shape name
def _add_shape_type_for_keywords(dict, shape_keywords, shape_name):
    for shape_keyword in shape_keywords:
        dict[shape_keyword] = shape_name

## Creates a dictionary mapping shape keywords to canonical shape names used by ChaiScript scripts
## Provides a convenient way to map words in tweets like "rects" to the shape type "RECTANGLE"
def _make_shape_keyword_dictionary():
    dict = {}
    _add_shape_type_for_keywords(dict, _rect_keywords, "RECTANGLE")
    _add_shape_type_for_keywords(dict, _rotated_rect_keywords, "ROTATED_RECTANGLE")
    _add_shape_type_for_keywords(dict, _triangle_keywords, "TRIANGLE")
    _add_shape_type_for_keywords(dict, _ellipse_keywords, "ELLIPSE")
    _add_shape_type_for_keywords(dict, _rotated_ellipse_keywords, "ROTATED_ELLIPSE")
    _add_shape_type_for_keywords(dict, _circle_keywords, "CIRCLE")
    _add_shape_type_for_keywords(dict, _line_keywords, "LINE")
    _add_shape_type_for_keywords(dict, _quadratic_bezier_keywords, "QUADRATIC_BEZIER")
    _add_shape_type_for_keywords(dict, _polyline_keywords, "POLYLINE")
    return dict

## Gets the maximum number of shapes allowed for the given shape type
## This to to set a sensible limit on the length of time the bot will spend on a single image
def _max_quantity_for_shape_type(shape_type):
    dict = {}
    dict["RECTANGLE"] = 500
    dict["ROTATED_RECTANGLE"] = 750
    dict["TRIANGLE"] = 750
    dict["ELLIPSE"] = 750
    dict["ROTATED_ELLIPSE"] = 750
    dict["CIRCLE"] = 750
    dict["LINE"] = 4000
    dict["QUADRATIC_BEZIER"] = 4000
    dict["POLYLINE"] = 4000

    return dict[shape_type]

## Parses a tweet message and returns a dictionary of the shape types and quantities that were requested
def _make_shape_quantity_dictionary(message):
    symbols = message.split(" ")
    shape_keyword_dictionary = _make_shape_keyword_dictionary()
    shape_quantity_dictionary = {}

    for symbol in symbols:
        pair = symbol.split("=")

        if len(pair) != 2:
            continue

        shape_type_key = pair[0].strip()
        if shape_type_key not in shape_keyword_dictionary:
            continue

        if not _represents_int(pair[1].strip()):
            continue

        shape_type = shape_keyword_dictionary[shape_type_key]
        shape_count = int(pair[1].strip())
        shape_count_max = _max_quantity_for_shape_type(shape_type)

        if shape_count <= 0:
            print("Got bad shape count request, must be positive")
            continue

        if shape_count >= shape_count_max:
            print("Requested shape count was too high, clamping it down")
            shape_count = shape_count_max

        shape_quantity_dictionary[shape_type] = shape_count

    return shape_quantity_dictionary

## Helper for constructing a ChaiScript script for geometrizing shapes
def _make_loop_body(shape_type):
    return "var prefs = task.getPreferences(); prefs.setShapeTypes(" + shape_type + "); task.setPreferences(prefs); task.stepModel();"

## Helper for constructing a ChaiScript script for geometrizing shapes
def _make_for_loop(step_count, shape_type):
    return "for(var i = 0; i < " + str(step_count) + "; ++i) { " + _make_loop_body(shape_type) + " }";

## Helper for constructing a ChaiScript script for geometrizing shapes
def _make_shape_code(dict):
    code = ""
    for key, value in dict.items():
        code += _make_for_loop(value, key)
    return code

## Parses the given tweet, returning the ChaiScript code for Geometrize to run based on the contents of the tweet.
## The shapes are added in the order they are specified in the message.
## Message examples: "@Geometrizer triangles=30 and rectangles=20, thanks bot!" - produces an image with 30 triangles, then 20 rectangles.
## Or: "@Geometrizer triangles=30 circles=500, triangles=20, nice bot!" - produces an image with 30 triangles, 500 circles, 20 triangles.
## Or: "@Geometrizer tris=300 circs=200" - produces an image with 300 triangles, 200 circles.
## Or: "@Geometrize rotated_rects=500" - produces an image with 500 rotated rectangles.
## Or: "@Geometrizer this is a really cool bot!" - produces an image with a random selection and quantity of shapes.
## :return A chunk of ChaiScript code that adds the shapes that the tweet requests (must be combined with a larger script to work).
def make_code_for_shape_tweet(message):

    shape_quantity_dictionary = _make_shape_quantity_dictionary(message)
    if shape_quantity_dictionary:
        # Try to match shapeTypeN=shapeQuantityN patterns
        code = _make_shape_code(shape_quantity_dictionary)
        print("Creating specific shapes and quantities code for tweet")
        return code

    # Failed, so use a random shape type instead
    print("Creating random shapes code for tweet")

    # Use a subset of possible shapes since random numbers of others don't always look good
    shape_types = ['ROTATED_RECTANGLE', 'ROTATED_ELLIPSE', 'TRIANGLE', 'CIRCLE', 'ELLIPSE']
    shape_type = random.choice(shape_types)
    shape_quantity = random.randint(200, 500)
    shape_quantity_dictionary[shape_type] = shape_quantity
    return _make_shape_code(shape_quantity_dictionary)