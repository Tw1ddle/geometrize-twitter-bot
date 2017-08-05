## @package on_status_event
#  Module containing the code that the bot runs when it receives a status event.
#  This is where most of the work is set in motion e.g. the bot receives a Tweet, it parses the tweet, and figures out how to respond.

import re
import uuid

from io import BytesIO

from PIL import Image
from PIL import ImageFile

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

## Geometrizes and saves an image.
def _geometrize_and_save_image(options):
    print("Will geometrize and save image")

    # Options should implicitly contain the input and output file paths
    result = geometrize.geometrize(options)

    return False

## Tweets an image.
def _tweet_image(image_filepath, username, status_id, api):
    print("Will load and tweet image")

    api.update_with_media(result_filepath, status = '@{0}'.format(username), in_reply_to_status_id = status_id)

## Handles a status change event from the Twitter streaming API.
## In practice, this means waiting for a status update and responding to it.
def on_status_event(api, status):
    message = status.text
    
    ImageFile.LOAD_TRUNCATED_IMAGES = True

    if re.search('status', message, re.IGNORECASE):
        print("Received bot status request")
        return

    username = status.user.screen_name
    status_id = status.id
    if 'media' in status.entities:
        for image in status.entities['media']:
            download_filepath = 'temp_' + uuid.uuid4() + '.jpg'
            result_filepath = 'geometrized_' + download_filepath
            if(_download_and_save_image(image['media_url'], download_filepath)):
                if(_geometrize_and_save_image(result_filepath)):
                    tweet_image(result_filepath, username, status_id, api)
                else:
                    print("Failed to geometrize and save image to: " + result_filepath)
            else:
                print("Failed to download and save tweet image to: " + download_filepath)