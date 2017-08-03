## @package bot
#  Module that sets up the Geometrize Twitter bot.
#
#  Invoke this script to run the bot e.g. "python bot.py".

import sys

import config
import dependency_locator
import geometrize
import geometrize_bot
import launch_text
import on_status_event

# Print welcome text.
launch_text.print_launch_text()

# Check that secrets/app credentials have been filled out.
if not config.validate_credentials():
    print("Failed to validate app credentials, will exit. Did you remember to enter them in config.py?")
    sys.exit(1)

# Check that the Geometrize executable is where we expect it to be.
if not dependency_locator.geometrize_executable_exists():
    print("Failed to locate the Geometrize executable, will exit. Did you copy it to the 'geometrize' subdirectory? Expected it to be here: " + dependency_locator.get_geometrize_executable_path())
    sys.exit(2)

# Run a quick test script to confirm Geometrize is in working order.
print("Running startup tests to ensure Geometrize is working...\r\n")
if geometrize.test_geometrize():
    print("Geometrize startup tests succeeded!\r\n")
else:
    print("Geometrize startup tests failed. Please report an issue here: https://github.com/Tw1ddle/geometrize-twitter-bot \r\n")
    sys.exit(3)

## Callback triggered when the stream listener connects.
def on_connect(api):
    print("Twitter stream listener did connect")

## Callback triggered when the stream listener times out.
def on_timeout(api):
    print("Twitter stream listener did time out")
    return False

## Callback triggered when the listener encounters an error.
def on_error(api, code):
    print("Encountered Twitter error response: %s" % code)
    return True

## Callback triggered when the stream listener reports a status event.
def on_status(api, status):
    print("Received Twitter stream listener status event")
    on_status_event.on_status_event(api, status)

# Create and set up the Geometrize bot, using credentials defined in the config file.
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