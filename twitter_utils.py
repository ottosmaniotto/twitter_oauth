import oauth2
import constants
import urllib.parse as urlparse

consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)


def get_request_token():
    # Create a consumer that uses a KEy and SECRET to identify the app
    client = oauth2.Client(consumer)

    # Use client to perform a request token
    response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
    if response.status != 200:
        print("An error ocurred getting the request token from Twitter")

    # Get the request token parsing he query string returned
    return dict(urlparse.parse_qsl(content.decode('utf-8')))


def get_oauth_verifier(request_token):
    # Ask the user to authorize
    print('Go to the following site in your browser to access with Twitter:')
    print(get_oauth_verifier_url(request_token))

    return input("What is the PIN?")

def get_oauth_verifier_url(request_token):
    return "{}?oauth_token={}".format(constants.AUTHORIZATION_URL, request_token['oauth_token'])


def get_access_token(request_token, oauth_verifier):
    # Create a Token object which contains the request token, and the verifier
    token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)

    # Create a client with our consumer (app) and the newly created and verified token
    client = oauth2.Client(consumer, token)

    # Ask twitter for an access token, it gives cuz is verified
    response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
    return dict(urlparse.parse_qsl(content.decode('utf-8')))