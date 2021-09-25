import tweepy

CONSUMER_KEY= "ZJMzn9u8SlfzxWIZXAQ34tT90"
CONSUMER_SECRET= "ITVg3utnB4kU4zeJAg79oqsY6YQCsN7mx49rLQanOlXdPKIKy6"
ACCESS_TOKEN_KEY= "1440660026209673218-rLS3ZFkwxtPx6gr0oKdiY1xiUJLar1"
ACCESS_TOKEN_SECRET= "5fyEdGQT4Xb1oaC2NqlYcttA6zJdU0ASTfHoo9mtG5iNQ"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
#api = tweepy.API(auth)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

def get_tweets(id) :
    tweet = api.get_status(id)
    return tweet