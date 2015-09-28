from secrets import *
from twitter import *

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, 
API_SECRET))

