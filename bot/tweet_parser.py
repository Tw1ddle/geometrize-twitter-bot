## @package tweet_parser
#  This module contains code that reads tweet text sent to the bot and figures out how the bot should respond.

import random
import re

_rect_keywords = [ "rect", "rects", "rectangle", "rectangles" ]
_rotated_rect_keywords = [ "rotated rect", "rotated rects", "rotated rectangle", "rotated rectangles", "rotated_rectangle", "rotated_rectangles" ]
_triangle_keywords = [ "tri", "tris", "triangle", "triangles" ]
_ellipse_keywords = [ "ellipse", "ellipses" ]
_rotated_ellipse_keywords = [ "rotated ellipse", "rotated ellipses", "rotated_ellipse", "rotated_ellipses" ]
_circle_keywords = [ "circ", "circs", "circle", "circles" ]
_line_keywords = [ "line", "lines" ]
_quadratic_bezier_keywords = [ "bezier", "beziers", "quadratic bezier", "quadratic beziers", "quadratic_bezier", "quadratic_beziers" ]
_polyline_keywords = [ "polyline", "polylines" ]

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

def _add_function_for_keywords(dict, keywords, func):
    for keyword in keywords:
        dict[keyword] = func

def _make_chaiscript_function_dictionary():
    dict = {}
    _add_function_for_keywords(dict, _rect_keywords, "RECTANGLE")
    _add_function_for_keywords(dict, _rotated_rect_keywords, "ROTATED_RECTANGLE")
    _add_function_for_keywords(dict, _triangle_keywords, "TRIANGLE")
    _add_function_for_keywords(dict, _ellipse_keywords, "ELLIPSE")
    _add_function_for_keywords(dict, _rotated_ellipse_keywords, "ROTATED_ELLIPSE")
    _add_function_for_keywords(dict, _circle_keywords, "CIRCLE")
    _add_function_for_keywords(dict, _line_keywords, "LINE")
    _add_function_for_keywords(dict, _quadratic_bezier_keywords, "QUADRATIC_BEZIER")
    _add_function_for_keywords(dict, _polyline_keywords, "POLYLINE")
    return dict

def _make_loop_body(shapeType):
    return "var prefs = job.getPreferences(); prefs.setShapeTypes(" + shapeType + "); job.setPreferences(prefs); job.stepModel();"

def _make_for_loop(stepCount, shapeType):
    return "for(var i = 0; i < " + str(stepCount) + "; ++i) { " + _make_loop_body(shapeType) + " }";

def _make_random_shapes_code():
    d = _make_chaiscript_function_dictionary()
    return _make_for_loop(random.randint(50, 200), d[random.choice(list(d.keys()))])

## Parses the given tweet, returning the ChaiScript code for Geometrize to run based on what the tweet requests.
## The message should be structured as followed "@BotName shapeType1=shapeQuantity1 shapeTypeN=shapeQuantityN."
## The shapes are added in the order they are specified in the message.
## :return A chunk of ChaiScript code that adds the shapes that the tweet requests (must be combined with a larger script to work).
def parse_tweet_for_shape_script(message):
    # Message examples: "@Geometrizer triangles=30 and rectangles=20, thanks bot!" - produces an image with 30 triangles, then 20 rectangles.
    # Or: "@Geometrizer triangles=30 circles=500, triangles=20, nice bot!" - produces an image with 30 triangles, 500 circles (clamped to max), 20 triangles.
    # Or: "@Geometrizer tris=300 circs=200" - produces an image with 300 triangles, 200 circles.
    # Or: "@Geometrizer tris circ rects lines beziers" - produces an image with a random number of these shapes.
    # Or: "@Geometrizer this is a really cool bot!" - produces an image with a random selection and quantity of shapes.

    # Match the shapeTypeN=shapeQuantityN patterns
    
    
    # Failed, so try to match all the standalone shapeTypeN patterns
    
    
    # Failed, so use a random selection of shapes
    return _make_random_shapes_code()