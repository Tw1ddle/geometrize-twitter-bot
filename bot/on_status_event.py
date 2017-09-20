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

## Downloads an image from a tweet.
## Returns the request content if it succeeds, else None.
def _download_image(url):
    print("Will download image")
    request = requests.get(url, stream = True)
    if request.status_code != 200:
        print("Failed to download image, got status code: " + request.status_code)
        return None
    return request.content

## Tweets an image.
def _tweet_image(image_filepath, message, status_id, api):
    print("Will tweet image")

    # Truncate the message
    max_len = 110
    trimmed_message = message[:max_len] + (message[max_len:] and '...')

    api.update_with_media(image_filepath, status = trimmed_message, in_reply_to_status_id = status_id)

## Tweets a simple message.
def _tweet_message(message, username, status_id, api):
    print("Will send tweet message: " + message + " to " + username)
    api.update_status(status = '@{0} {1}'.format(username, message), in_reply_to_status_id = status_id)

## Handles a status change event from the Twitter streaming API.
## This means waiting for status updates and doing things to response to them.
def on_on_demand_status_event(api, status):
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
        _tweet_message('Geometrize bot status is alive', username, status_id, api)
        return

    if 'media' in status.entities:
        for image in status.entities['media']:
            download_filename = 'temp_' + uuid.uuid4().hex + '.png'
            download_filepath = dependency_locator.get_geometrize_image_file_absolute_path(download_filename)
            result_filepath = dependency_locator.get_geometrize_image_file_absolute_path('geometrized_' + download_filename)
            
            image_data = _download_image(image['media_url'])
            if image_data is None:
                print("Failed to download tweet image")
                continue

            image = Image.open(BytesIO(image_data))
            if not save_image(image, download_filepath):
                print("Failed to save image to filepath " + download_filepath)
                continue

            geometrize_options = {}
            geometrize_options["::IMAGE_INPUT_PATH::"] = download_filepath
            geometrize_options["::IMAGE_OUTPUT_PATH::"] = result_filepath
            geometrize_options["::IMAGE_TASK_STEP_LOOPS::"] = tweet_parser.make_code_for_shape_tweet(message)
            if not geometrize.run_geometrize(code, geometrize_options):
                print("Failed to run geometrize")
                continue

            if not username:
                continue

            at_username = '@{0}'.format(username)

            # Do not tweet @yourself when tweeting images - avoids an infinite tweet loop
            if at_username != config.TWITTER_BOT_USERNAME:
                _tweet_image(result_filepath, at_username + " Geometrize has geometrized your image...", status_id, api)

            print("Did tweet image")

## Handles a status change event from the Twitter streaming API.
## This means waiting for status updates and doing things to response to them.
def on_account_watcher_status_event(api, status):
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
        _tweet_message('Geometrize bot status is alive', username, status_id, api)
        return

    if 'media' in status.entities:
        for image in status.entities['media']:
            download_filename = 'temp_' + uuid.uuid4().hex + '.png'
            download_filepath = dependency_locator.get_geometrize_image_file_absolute_path(download_filename)
            result_filepath = dependency_locator.get_geometrize_image_file_absolute_path('geometrized_' + download_filename)
            
            image_data = _download_image(image['media_url'])
            if image_data is None:
                print("Failed to download tweet image")
                continue

            image = Image.open(BytesIO(image_data))
            if not save_image(image, download_filepath):
                print("Failed to save image to filepath " + download_filepath)
                continue

            geometrize_options = {}
            geometrize_options["::IMAGE_INPUT_PATH::"] = download_filepath
            geometrize_options["::IMAGE_OUTPUT_PATH::"] = result_filepath
            geometrize_options["::IMAGE_TASK_STEP_LOOPS::"] = tweet_parser.make_code_for_shape_tweet(message)
            if not geometrize.run_geometrize(code, geometrize_options):
                print("Failed to run geometrize")
                continue

            at_username = '@{0}'.format(username)

            _tweet_image(result_filepath, "", None, api)
            print("Did tweet image")