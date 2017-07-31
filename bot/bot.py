import config

import geometrize_bot
import tweet_image

# Define some Twitter stream listener callbacks for the bot
def on_connect(api):
    print("Stream listener did connect")

def on_timeout(api):
    print("Stream listener did time out")
    return False

def on_error(api, code):
    print("Encountered error response: %s" % code)
    return True

def on_status(api, status):
    print("Received stream listener status event")
    username = status.user.screen_name
    status_id = status.id
    if 'media' in status.entities:
        for image in status.entities['media']:
            tweet_image.tweet_image(image['media_url'], username, status_id, self.api)

# Create and set up the Geometrize bot using credentials defined in the config file.
bot = geometrize_bot.GeometrizeBot(
    config.OAUTH_CONSUMER_KEY,
    config.OAUTH_CONSUMER_SECRET,
    config.OAUTH_ACCESS_TOKEN,
    config.OAUTH_ACCESS_SECRET,
    config.TWITTER_BOT_USERNAME,
    on_connect,
    on_timeout,
    on_error,
    on_status)