import os

import tweepy
import logging


class TwitterService(object):
    def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
        self._consumer_key_ = consumer_key
        self._consumer_secret_ = consumer_secret
        self._access_key_ = access_key
        self._access_secret_ = access_secret

        self._api_ = None

    @property
    def api(self):
        return self._api_

    def connect(self):
        auth = tweepy.OAuthHandler(self._consumer_key_, self._consumer_secret_)
        auth.secure = True
        auth.set_access_token(self._access_key_, self._access_secret_)
        api = tweepy.API(auth)
        self._api_ = api

        return self


class TwitterStreamListener(tweepy.StreamListener):
    def __init__(self, dump=None, subscribers=None):
        super().__init__()
        if subscribers is None:
            subscribers = []
        self._dump_ = dump
        self._subscribers_ = subscribers

    @property
    def subscribers(self):
        return self.subscribers

    @subscribers.setter
    def subscribers(self, value):
        self.subscribers = value

    def on_status(self, status):
        tweet = status.text.replace("\r", " ").replace("\n", " ").strip()
        tweet_id = str(status.id)
        if not tweet:
            return

        if self._dump_ is not None:
            logging.info(tweet)
            self._dump_.write(tweet_id + "\t" + tweet + os.linesep)

        for subscriber in self._subscribers_:
            subscriber(status)

    def on_error(self, status_code):
        logging.debug(status_code)
        pass

    def on_disconnect(self, notice):
        logging.debug(notice)
        self._dump_.close() if self._dump_ is not None else None
        pass