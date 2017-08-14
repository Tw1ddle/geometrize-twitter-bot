## @package bot
#  Module that sets up the Geometrize Twitter bot.
#
#  Invoke this script to run the bot i.e. "python bot.py".

import sys

import config
import dependency_locator
import geometrize
import geometrize_bot
import launch_text
import on_status_event
import tweepy

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

# Connect to Twitter.
tweepy_auth = tweepy.OAuthHandler(config.OAUTH_CONSUMER_KEY, config.OAUTH_CONSUMER_SECRET)
tweepy_auth.set_access_token(config.OAUTH_ACCESS_TOKEN, config.OAUTH_ACCESS_SECRET)
tweepy_api = tweepy.API(tweepy_auth)

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

## Callback triggered when setting up the stream filter for tracking the Geometrize bot account.
def on_on_demand_filter_setup(stream):
    print("Setting up on demand tweet filter...")
    stream.filter(track = [config.TWITTER_BOT_USERNAME], async = True)

## Callback triggered when setting up the stream filter for tracking specific Twitter accounts.
def on_account_watcher_filter_setup(stream):
    print("Setting up account watcher tweet filter...")
    stream.filter(follow = config.TWITTER_BOT_WATCH_ACCOUNTS, async = True)

# Create and set up the on-demand Geometrize bot.
# This bot waits for users to tweet images at the bot, which it then geometrizes.
on_demand_bot = geometrize_bot.GeometrizeBot(
    tweepy_auth,
    tweepy_api,
    on_connect,
    on_timeout,
    on_error,
    on_status,
    on_on_demand_filter_setup)

# Create and set up the specific account watcher bot.
# This bot watches specific accounts and geometrizes images they tweet.
account_watcher_bot = geometrize_bot.GeometrizeBot(
    tweepy_auth,
    tweepy_api,
    on_connect,
    on_timeout,
    on_error,
    on_status,
    on_account_watcher_filter_setup)