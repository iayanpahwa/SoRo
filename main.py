import os
import json
import tweepy
from flask import Flask
from flask_restful import Api, Resource, reqparse

# Creds to interact with twitter API, obtained from https://developer.twitter.com/
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth)

app = Flask(__name__)
api = Api(app)

tweet_post_args = reqparse.RequestParser()
tweet_post_args.add_argument("content", type=str, help="Content of the tweet is required", required=True)

class tweet(Resource):
    def post(self):
        args = tweet_post_args.parse_args()
        twitter_api.update_status(status = args['content'])
        return args

# API Endpoint to tweet 
api.add_resource(tweet, "/tweet")   

if __name__ == "__main__":
    app.run(debug=True, port= '5000')

    