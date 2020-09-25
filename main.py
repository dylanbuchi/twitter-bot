import os
import tweepy
import dotenv


def get_api():
    """
    Load api keys in .env file, basic auth for twitter API and return the API
    """

    dotenv.load_dotenv()

    consumer_key = os.environ.get('consumer_key')
    consumer_secret = os.environ.get('consumer_secret')

    access_token = os.environ.get('access_token')
    access_token_secret = os.environ.get('access_token_secret')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api


def follow_original_author(api, subject, number_of_authors):
    """follow original authors by filtering retweets using tweets subject 

    Args:
        api (API): Twitter API
        subject (str): pick a subject for the tweets to like ex: 'python'
        number_of_authors (int): how many tweets to like
    """
    filter_retweets = "-filter:retweets"

    for follower in tweepy.Cursor(
            api.search,
            f"{subject} {filter_retweets}").items(number_of_authors):
        try:
            api.create_friendship(screen_name=follower.author.screen_name)
            print(follower)
        except tweepy.TweepError as error:
            print(error)
        except StopIteration:
            break
    print("done")


def like_python_tweets(api, subject, number_of_tweets):
    """like tweets by subject

    Args:
        api (API): Twitter API
        subject (str): pick a subject for the tweets to like ex: 'python'
        number_of_tweets (int): how many tweets to like
    """
    for tweet in tweepy.Cursor(api.search, subject).items(number_of_tweets):

        try:
            tweet.favorite()
            print('<3')
        except tweepy.TweepError as error:
            print(error)
        except StopIteration:
            break
    print("done")


if __name__ == "__main__":

    api = get_api()
