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

def _represents_int(s):
    return re.match(r"[-+]?\d+$", s) is not None

def _clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

def _add_shape_type_for_keywords(dict, keywords, func):
    for keyword in keywords:
        dict[keyword] = func

def _make_shape_type_dictionary():
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

def _add_max_quantity_for_shape_type(dict, shape_type, quantity):
    dict[shape_type] = quantity

def _make_max_shape_quantity_dictionary():
    dict = {}
    _add_max_quantity_for_shape_type(dict, "RECTANGLE", 500)
    _add_max_quantity_for_shape_type(dict, "ROTATED_RECTANGLE", 750)
    _add_max_quantity_for_shape_type(dict, "TRIANGLE", 750)
    _add_max_quantity_for_shape_type(dict, "ELLIPSE", 750)
    _add_max_quantity_for_shape_type(dict, "ROTATED_ELLIPSE", 750)
    _add_max_quantity_for_shape_type(dict, "CIRCLE", 750)
    _add_max_quantity_for_shape_type(dict, "LINE", 4000)
    _add_max_quantity_for_shape_type(dict, "QUADRATIC_BEZIER", 4000)
    _add_max_quantity_for_shape_type(dict, "POLYLINE", 4000)
    return dict

def _max_quantity_for_shape_type(shape_type):
    dict = _make_max_shape_quantity_dictionary()
    return dict[shape_type]

def _make_loop_body(shape_type):
    return "var prefs = task.getPreferences(); prefs.setShapeTypes(" + shape_type + "); task.setPreferences(prefs); task.stepModel();"

def _make_for_loop(step_count, shape_type):
    return "for(var i = 0; i < " + str(step_count) + "; ++i) { " + _make_loop_body(shape_type) + " }";

def _make_random_shapes_code(dict):
    return _make_for_loop(random.randint(300, 500), dict[random.choice(list(dict.keys()))])

def _make_specific_shape_quantity_code(dict, message):
    code = ""

    symbols = message.split(" ")

    for symbol in symbols:

        pair = symbol.split("=")

        if len(pair) != 2:
            continue

        shape_type_key = pair[0].strip()
        if shape_type_key not in dict:
            continue

        if not _represents_int(pair[1].strip()):
            continue

        shape_type = dict[shape_type_key]
        shape_count = int(pair[1].strip())
        shape_count_max = _max_quantity_for_shape_type(shape_type)

        if shape_count <= 0:
            print("Got bad shape count request, must be positive")
            continue

        if shape_count >= shape_count_max:
            print("Requested shape count was too high, clamping it down")
            shape_count = shape_count_max

        code += _make_for_loop(shape_count, shape_type)

    return code

def _make_specific_shapes_code(dict, message):
    code = ""

    symbols = message.split(" ")

    for symbol in symbols:
        stripped_symbol = symbol.strip()
        if stripped_symbol not in dict:
            continue

        if stripped_symbol not in dict:
            continue

        shape_type = dict[stripped_symbol]
        shape_count = random.randint(100, 300)
        code += _make_for_loop(shape_count, shape_type)

    return code

## Parses the given tweet, returning the ChaiScript code for Geometrize to run based on the contents of the tweet.
## The shapes are added in the order they are specified in the message.
## Message examples: "@Geometrizer triangles=30 and rectangles=20, thanks bot!" - produces an image with 30 triangles, then 20 rectangles.
## Or: "@Geometrizer triangles=30 circles=500, triangles=20, nice bot!" - produces an image with 30 triangles, 500 circles, 20 triangles.
## Or: "@Geometrizer tris=300 circs=200" - produces an image with 300 triangles, 200 circles.
## Or: "@Geometrize rotated_rects=500" - produces an image with 500 rotated rectangles.
## Or: "@Geometrizer tris circ rects lines beziers" - produces an image with a random number of these shapes.
## Or: "@Geometrizer this is a really cool bot!" - produces an image with a random selection and quantity of shapes.
## :return A chunk of ChaiScript code that adds the shapes that the tweet requests (must be combined with a larger script to work).
def make_code_for_shape_tweet(message):

    dict = _make_shape_type_dictionary()

    # Try to match shapeTypeN=shapeQuantityN patterns
    code = _make_specific_shape_quantity_code(dict, message)
    if code:
        print("Creating specific shapes and quantities code for tweet")
        return code

    # Failed, try to match the standalone shapeType patterns
    code = _make_specific_shapes_code(dict, message)
    if code:
        print("Creating specific shapes code for tweet")
        return code
    
    # Failed, so use a random selection of shapes
    print("Creating random shapes code for tweet")
    return _make_random_shapes_code(dict)