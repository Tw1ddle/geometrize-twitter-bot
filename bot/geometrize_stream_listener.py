## @package geometrize_stream_listener
#  Module containing the Geometrize bot stream listener, which triggers various callbacks when Twitter API events occur.

import tweepy

class GeometrizeStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        super(tweepy.StreamListener, self).__init__()
        print("Will create Twitter stream listener")

        self.on_connect_cb = None
        self.on_timeout_cb = None
        self.on_error_cb = None
        self.on_status_cb = None

        self.api = api

        print("Did create Twitter stream listener")

    def on_connect(self):
        if self.on_connect_cb:
            self.on_connect_cb(self.api)

    def on_timeout(self):
        if self.on_timeout_cb:
            return self.on_timeout_cb(self.api)
        return False

    def on_error(self, code):
        if self.on_error_cb:
            return self.on_error_cb(self.api, code)
        return True

    def on_status(self, status):
        if self.on_status_cb:
            self.on_status_cb(self.api, status)