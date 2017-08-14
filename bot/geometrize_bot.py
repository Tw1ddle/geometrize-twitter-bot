## @package geometrize_bot
#  Module that encapsulates the Geometrize bot class, which sets up a connection to the Twitter streaming API when instantiated.

import tweepy

import geometrize_stream_listener

class GeometrizeBot:
    def __init__(self,
        tweepy_auth,
        tweepy_api,
        on_connect = None,
        on_timeout = None,
        on_error = None,
        on_status = None,
        on_setup_filter = None):

        print("Will create Geometrize bot")

        self.api = tweepy_api
        self.auth = tweepy_auth

        # Set up a stream listener
        self.stream_listener = geometrize_stream_listener.GeometrizeStreamListener(self.api)
        self.stream_listener.on_connect_cb = on_connect
        self.stream_listener.on_timeout_cb = on_timeout
        self.stream_listener.on_error_cb = on_error
        self.stream_listener.on_status_cb = on_status

        self.stream = tweepy.Stream(self.auth, self.stream_listener)

        # Start listening for filtered tweets.
        if on_setup_filter is not None:
            on_setup_filter(self.stream)

        print("Did create Geometrize bot")