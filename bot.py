import re, praw, requests, os, sys, urllib, time, requests, json

firebase_url = "https://studious-octo-adventure.firebaseio.com/"
soundcloud = []
youtube = []

def connect():
    user_agent      = "Reddit Music Player v0.1 alpha by /u/banglatoker"
    client_id       = "bZBbJ0n8UGi0VA"
    client_secret   = "qshO_VjERIwcs3RMqh_EGgK4BL0"
    r = praw.Reddit(client_id = client_id,
                    client_secret = client_secret,
                    user_agent = user_agent)
    return r

def main():
    arg_len = len(sys.argv)
    if arg_len < 2:
        sub = "trap"
    elif arg_len >= 2:
        sub = sys.argv[1]
    r = connect()
    subredditLinks = loadSubReddit(sub, r)
    getLinks(subredditLinks, sub)

def loadSubReddit(sub, r):
    return r.subreddit(sub).hot()

def getLinks(subredditLinks, sub):
    for links in subredditLinks:
        if "soundcloud.com" in links.url:
            data = { 'link' : links.url, 'score': links.score, 'up': links.ups, 'down': links.downs}
            linkType = "soundcloud"
            postToFirebase(data, linkType, sub)
        if "youtube.com" in links.url:
            data = { 'link' : links.url, 'score': links.score, 'up' : links.ups, 'down': links.downs}
            linkType = "youtube"
            postToFirebase(data, linkType, sub)

def postToFirebase(data, linkType, sub):
    if "soundcloud" is linkType:
        result = requests.post(firebase_url + "/" + sub + '/soundcloud.json', data=json.dumps(data))
    if "youtube" is linkType:
        result = requests.post(firebase_url + "/" + sub + '/youtube.json', data=json.dumps(data))
    print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text

main()
