import time
import os
import tweepy as tp

from keyfile import *

# twitter api logon
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tp.API(auth)

# iteration on the images folder
os.chdir('images')
for model_image in os.listdir('.'):
	api.update_with_media(model_image)
	time.sleep(3)