import os
import requests
import twitter


def internetUp():
    try:
        response = requests.get("http://www.google.com")
	return True
    except requests.ConnectionError:
	pass
    return False


def getApi():
    c = os.getenv('CONSUMER_KEY')
    c_s = os.getenv('CONSUMER_SECRET')
    a_t = os.getenv('ACCESS_TOKEN')
    a_t_s = os.getenv('ACCESS_TOKEN_SECRET')
    return twitter.Api(consumer_key=c, consumer_secret=c_s,
                       access_token_key=a_t, access_token_secret=a_t_s)
