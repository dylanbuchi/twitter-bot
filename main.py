import dotenv
import tweepy
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    consumer_key = os.environ.get('consumer_key')
    consumer_secret = os.environ.get('consumer_secret')

    access_token = os.environ.get('access_token')
    access_token_secret = os.environ.get('access_token_secret')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()

    user = api.me()
    print(user)