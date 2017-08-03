## @package on_status_event
#  Module containing the code that the bot runs when it receives a status event.
#  This is where most of the work is set in motion e.g. the bot receives a Tweet, it parses the tweet, and figures out how to respond.

import uuid

from io import BytesIO

from PIL import Image
from PIL import ImageFile

# Geometrizes and tweets an image
def _geometrize_and_tweet_image(url, username, status_id, api):
    print("Will tweet image")
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    request = requests.get(url, stream = True)
    if request.status_code == 200:
        i = Image.open(BytesIO(request.content))
        filename = 'temp_' + uuid.uuid4() + '.jpg'
        i.save(filename)
        geometrize(filename, '')
        api.update_with_media(image_filename, status = '@{0}'.format(username), in_reply_to_status_id = status_id)
    else:
        print("Failed to download image")

# Handles a status change event from the Twitter streaming API
# In practice, this means waiting for media to appear and geometrizing it
def on_status_event(api, status):
    username = status.user.screen_name
    status_id = status.id
    if 'media' in status.entities:
        for image in status.entities['media']:
            _geometrize_and_tweet_image(image['media_url'], username, status_id, api)