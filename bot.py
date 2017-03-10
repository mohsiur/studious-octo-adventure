import re, praw, requests, os, sys, urllib

def connect():
    user_agent      = "Reddit Music Player v0.1 alpha by /u/banglatoker"
    client_id       = "bZBbJ0n8UGi0VA"
    client_secret   = "qshO_VjERIwcs3RMqh_EGgK4BL0"
    r = praw.Reddit(client_id = client_id,
                    client_secret = client_secret,
                    user_agent = user_agent)
    return r

def main():
    r = connect()
    subredditLinks = loadSubReddit(r)
    getLinks(subredditLinks)

def loadSubReddit(r):
    sub = "trap"
    return r.subreddit(sub).stream.submissions()

def getLinks(subredditLinks):
    for links in subredditLinks:
        print(links.url)

main()
