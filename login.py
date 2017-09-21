from user import User
from database import Database
from twitter_utils import get_request_token, get_oauth_verifier, get_access_token

user_email = input('Enter your email:')

Database.initialise(user='postgres', password="g4rc14!", host='localhost', database='Learning')

user = User.load_from_db_by_screen_name(screen_name)

if not user:
    request_token = get_request_token()

    oauth_verifier = get_oauth_verifier(request_token)

    access_token = get_access_token(request_token, oauth_verifier)

    first_name = input('Enter you first name: ')
    last_name = input('Enter you last name: ')

    user = User(screen_name, access_token['oauth_token'], access_token['oauth_token_secret'], None)

    user.save_to_db()

tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computer+filter:images')

for tweet in tweets['statuses']:
    print(tweet['text'])


