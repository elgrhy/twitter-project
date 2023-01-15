import tweepy

consumer_key = 'yC1V63NWuAZ0YUn87NlvwYce0'
consumer_secret = '0Hn5b1LUAr04cLZpxjRZOVy8JoTmUru8kI25LEcAXFnNq1Phgy'
access_token = '103599712-90XQ7sE6Zpn8sf7vluRirlL0H1VZQ3XNmZWvNQIW'
access_token_secret = 'vadmpHlhuQPnQN8tbhSfuu4Ot7K2t5gDKGaRwR5EYuVBu'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('elgrhy')
