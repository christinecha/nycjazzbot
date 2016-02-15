import tweepy
import api_keys
from datetime import datetime
from random import choice
import calendar
from firebase import firebase

#Twitter credentials
def twitterSetup():
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET = api_keys.getKeys()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def getData():
    showsDB = firebase.FirebaseApplication('https://nycjazz.firebaseio.com/', None)
    shows = showsDB.get('/shows/', None)
    return shows

def isWithinTwoDays(allShows, show):
    showTime = allShows[show]['startDateTime']
    datetimeNow = datetime.utcnow()
    timestampNow = calendar.timegm(datetimeNow.utctimetuple())
    twoDaysUnix = 60 * 60 * 48

    if showTime > timestampNow and showTime < timestampNow + twoDaysUnix:
        return True
    return False

def getRandomShow():
    allShows = getData()
    matchingShows = [allShows[show] for show in allShows if isWithinTwoDays(allShows, show)]
    print choice(matchingShows)


if __name__ == '__main__':
    getRandomShow()
    api = twitterSetup()
    # with open('data.txt','r') as f:

        #Print something
        # for line in f.readlines():
            # api.update_status(line)
            # print line
