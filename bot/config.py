## @package config
#  Module containing secret Twitter API keys and bot configuration info.

OAUTH_CONSUMER_KEY = "YOUR_VALUE_HERE"
OAUTH_CONSUMER_SECRET = "YOUR_VALUE_HERE"
OAUTH_ACCESS_TOKEN = "YOUR_VALUE_HERE"
OAUTH_ACCESS_SECRET = "YOUR_VALUE_HERE"
## Secret Twitter app keys. Enter your own here. Never make these public.

## Used to error out if credentials aren't configured
UNCONFIGURED_CREDENTIAL_VALUE = "YOUR_VALUE_HERE"

## Checks whether credentials have been filled out in the bot configuration file.
def validate_credentials():
   return (OAUTH_CONSUMER_KEY != UNCONFIGURED_CREDENTIAL_VALUE
   and OAUTH_CONSUMER_SECRET != UNCONFIGURED_CREDENTIAL_VALUE
   and OAUTH_ACCESS_TOKEN != UNCONFIGURED_CREDENTIAL_VALUE
   and OAUTH_ACCESS_SECRET != UNCONFIGURED_CREDENTIAL_VALUE)

## Twitter username of the account that will run the Geometrize bot.
TWITTER_BOT_USERNAME = "@Geometrizer" # The official bot by https://twitter.com/Sam_Twidale - it lives here: https://twitter.com/Geometrizer

## Twitter user ids of accounts that the Geometrize bot will watch for new tweets.
## When a tweet contains images, Geometrize will geometrize the images and tweet them out.
## Note you can get look up account ids easily using various sites online
##                            "@PexelsPhotos", "@cc0_landscapes",    "@unsplash"
TWITTER_BOT_WATCH_ACCOUNTS = ['2420838708',    '748738721390792710', '1520228526']