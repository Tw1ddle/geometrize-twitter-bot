# Bot configuration info

# Secret Twitter app keys. Enter your own here. Never make these public.
OAUTH_CONSUMER_KEY = "YOUR_VALUE_HERE"
OAUTH_CONSUMER_SECRET = "YOUR_VALUE_HERE"
OAUTH_ACCESS_TOKEN = "YOUR_VALUE_HERE"
OAUTH_ACCESS_SECRET = "YOUR_VALUE_HERE"

UNCONFIGURED_CREDENTIAL_VALUE = "YOUR_VALUE_HERE" # Used to error out if credentials aren't configured

def validate_credentials():
   return (OAUTH_CONSUMER_KEY != UNCONFIGURED_CREDENTIAL_VALUE 
   and OAUTH_CONSUMER_SECRET != UNCONFIGURED_CREDENTIAL_VALUE
   and OAUTH_ACCESS_TOKEN != UNCONFIGURED_CREDENTIAL_VALUE 
   and OAUTH_ACCESS_SECRET != UNCONFIGURED_CREDENTIAL_VALUE)

# Twitter username of the account that will run the Geometrize bot.
TWITTER_BOT_USERNAME = "@Geometrizer" # The official bot by https://twitter.com/Sam_Twidale lives here: https://twitter.com/Geometrizer

# Twitter usernames of accounts that the Geometrize bot will actively watch for new tweets.
# When a tweet contains images, Geometrize will geometrize the images and tweet the image.
# Not used for the time being
#TWITTER_BOT_WATCH_ACCOUNTS = ["@PexelsPhotos", "@cc0_landscapes", "@unsplash"]