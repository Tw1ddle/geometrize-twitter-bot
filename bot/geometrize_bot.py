import tweepy

import geometrize_stream_listener

class GeometrizeBot:
    def __init__(self,
        oauth_consumer_key,
        oauth_consumer_secret,
        oauth_access_token,
        oauth_access_secret,
        twitter_bot_username,
        on_connect = None,
        on_timeout = None,
        on_error = None,
        on_status = None):

        print("Will create Geometrize bot")

        # Connect to Twitter
        self.auth = tweepy.OAuthHandler(oauth_consumer_key, oauth_consumer_secret)
        self.auth.set_access_token(oauth_access_token, oauth_access_secret)
        self.api = tweepy.API(self.auth)

        # Set up a stream listener
        self.stream_listener = geometrize_stream_listener.GeometrizeStreamListener(self.api)
        self.stream_listener.on_connect_cb = on_connect
        self.stream_listener.on_timeout_cb = on_timeout
        self.stream_listener.on_error_cb = on_error
        self.stream_listener.on_status_cb = on_status

        self.stream = tweepy.Stream(self.auth, self.stream_listener)

        # Start listening for any tweets that @ the bot.
        self.stream.filter(track=[twitter_bot_username], async=True)

        print("Did create Geometrize bot")