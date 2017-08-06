## @package on_status_event
#  Module containing the code that the bot runs when it receives a status event.
#  This is where most of the work is triggered e.g. the bot receives a Tweet, it parses the tweet, and figures out how to respond.

import re
import requests
import uuid

from io import BytesIO

from PIL import Image
from PIL import ImageFile

import config
import dependency_locator
import geometrize
import tweet_parser

## Loads an image from the given filepath, returns the loaded image, or None if the loading failed.
def load_image(filepath):
    image = None
    try:
        image = Image.open(filepath)
    except:
        print("Failed to load image")
    return image

## Saves an image to the given filepath, returns true on success, false on failure.
def save_image(image, filepath):
    try:
        image.save(filepath)
    except:
        print("Failed to save image to: " + filepath)
        return False
    return True

## Downloads and saves an image taken from a tweet.
def _download_and_save_image(url, filepath):
    print("Will download and save image")

    request = requests.get(url, stream = True)
    
    if request.status_code != 200:
        print("Failed to download image, got status code: " + request.status_code)
        return False

    image = Image.open(BytesIO(request.content))
    return save_image(image, filepath)

## Tweets an image.
def _tweet_image(image_filepath, username, status_id, api):
    print("Will load and tweet image")

    message = '@{0}'.format(username)

    # Do not @ yourself when tweeting images to avoid infinite tweet loop
    if username == config.TWITTER_BOT_USERNAME:
        message = ""

    api.update_with_media(image_filepath, status = message, in_reply_to_status_id = status_id)

## Tweets a simple message.
def _tweet_message(message, username, status_id, api):
    print("Will send tweet message: " + message + " to " + username)
    api.update_status(status = '@{0} {1}'.format(username, message), in_reply_to_status_id = status_id)

## Handles a status change event from the Twitter streaming API.
## In practice, this means waiting for a status update and responding to it.
def on_status_event(api, status):
    username = status.user.screen_name
    status_id = status.id
    message = status.text
    
    ImageFile.LOAD_TRUNCATED_IMAGES = True

    code = dependency_locator.read_geometrize_script("geometrize_shape_choice_template.chai")
    if code == "":
        print("Failed to read script")
        return

    if re.search('Print Geometrize bot status', message, re.IGNORECASE):
        print("Received bot status request")
        _tweet_message('Geometrize bot status is good', username, status_id, api) # TODO should tweet some meaningful info
        return

    if 'media' in status.entities:
        for image in status.entities['media']:
            download_filename = 'temp_' + uuid.uuid4().hex + '.jpg'
            download_filepath = dependency_locator.get_geometrize_image_file_absolute_path(download_filename)
            result_filepath = dependency_locator.get_geometrize_image_file_absolute_path('geometrized_' + download_filename)
            
            geometrize_options = {}
            geometrize_options["::IMAGE_INPUT_PATH::"] = download_filepath
            geometrize_options["::IMAGE_OUTPUT_PATH::"] = result_filepath
            geometrize_options["::IMAGE_JOB_STEP_LOOPS::"] = tweet_parser.parse_tweet_for_shape_script(message)

            if(_download_and_save_image(image['media_url'], download_filepath)):
                if(geometrize.run_geometrize(code, geometrize_options)):
                    _tweet_image(result_filepath, username, status_id, api)
                else:
                    print("Failed to run geometrize")
            else:
                print("Failed to download and save tweet image to: " + download_filepath)