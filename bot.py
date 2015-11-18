#!/usr/bin/env python3
from pprint import pprint
from secrets import *
from time import sleep
from twitter import *

USERNAME = 'emilio___'


def main():
    twObject = Twitter(auth=OAuth(ACCESS_TOKEN,
                                  ACCESS_TOKEN_SECRET,
                                  API_KEY, API_SECRET))
    twitterStream = TwitterStream(domain='userstream.twitter.com',
                                  auth=OAuth(ACCESS_TOKEN,
                                             ACCESS_TOKEN_SECRET,
                                             API_KEY, API_SECRET))

    while True:
        sleep(60)
        stream = twitterStream.user()

        for tweet in stream:
            if 'hangup' in tweet:
                return
            elif 'text' in tweet and tweet['user']['screen_name'] == NOEMI:
                reply = '@%s %s' % (tweet['user']['screen_name'],
                                    NOEMI_RESPONSE)
                twObject.statuses.update(status=reply,
                                         in_reply_to_status_id=tweet['id'])

if __name__ == "__main__":
    main()
