import logging
import tweepy

from stream.twitter import TwitterService, TwitterStreamListener

consumer_key = "AHB6bSwBcXsnLzFMh4wDbne27"
consumer_secret = "YCYo9Jv9d3QSbvIZDKYyw1rFccDVLbyjJl7PCZW1ipe304Evlw"
access_token = "3531429916-GJBeBqGlMSREIpOhPuH2LZzavgzkVKVP2NiWLGD"
access_secret = "SlmBNSy1dHcdUw0sthd4oxjpNGLmEtBqnb8Ac48UwszWC"


def tweet2text(out_path, keyword):
    twitter_connection = TwitterService(consumer_key=consumer_key, consumer_secret=consumer_secret,
                                        access_key=access_token, access_secret=access_secret)
    twitter_connection.connect()

    api = twitter_connection.api

    outfile = open(out_path, mode='at', encoding="utf8", newline="")

    stream_listener = TwitterStreamListener(dump=outfile)

    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

    stream.filter(track=["AzerbaijanGP", "F1", "BakuGP", "ScuderiaFerrari", "MercedesAMGF1", "LewisHamilton"],
                  languages=["en"], async=True)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    keyword = "F1"
    out = "C:\\Users\\sasce\\PycharmProjects\\HMMispelling\\dataset\\" + keyword + "_training.txt"
    tweet2text(out, keyword=keyword)
