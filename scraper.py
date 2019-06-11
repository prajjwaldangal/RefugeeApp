import random
import requests
import re
import time
import urllib.request as urllib2

from bs4 import BeautifulSoup
USER_AGENTS_FILE = 'user_agents.txt'
PROXY_FILE = "list_of_proxies.txt"

# proxy = {"http": "http://username:p3ssw0rd@10.10.1.10:3128"}
proxy = ['96.9.252.114']

http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"

tag_class_pairs = {
        "for discussions"                 :     ( 'li' ,    'node forum level', ""),
        "for threads"                    :    ( 'li',    'discussionListItem visible', "threads"),
        "for posts' body"                :    ( 'div',  'messageContent'),
        "for posts' likes"               :   ( 'dl',    'brLikeReceived'),
        "for liked by"                   :   ( 'a',  'likeCount OverlayTrigger'),
        "for liked by 2"                 :   ( 'div', 'publicControls'),
        "for quoted text"                :    ( 'div',  'quote' ),
        # "for username"                   :   ('h3', 'username'),
        "for datetime"                   :   ('dl', 'brRightInfo timeStamp'),
        "for pagenav"                    :   ('div', 'PageNav'),
        "for actual likers"              :   ('li', 'primaryContent memberListItem')
        # "for actual likers"              :   ('h3', 'username')
    }

def LoadProxy(pfile = PROXY_FILE):
    proxies = {}
    with open(pfile, 'r') as pf:
        for p in pf.readlines():
            for ip in p.split(","):
                proxies["http"] = "http://" + ip
    return proxies

def LoadUserAgents(uafile=USER_AGENTS_FILE):
    """
    uafile : string
         path to text file of user agents, one per line
    """
    uas = []
    with open(uafile, 'rb') as uaf:
         for ua in uaf.readlines():
              if ua:
                   uas.append(ua.strip()[1:-1-1])
    random.shuffle(uas)
    return uas
params = {"q" : "London,uk"}
proxy = LoadProxy()
uas = LoadUserAgents()
# proxy = random.choice(ps)
ua = random.choice(uas)
headers = {
        "Connection" : "close",  # another way to cover tracks
        "User-Agent" : ua
    }
#websites = ["nytimes", "breitbart", "foxnews", "ap"]
#websites_complete = ["www."+el+".com" for el in websites]
tags = ["button", "div", "p"]
url = "https://www.nytimes.com/"
html_page = urllib2.urlopen("https://arstechnica.com")
response = BeautifulSoup(html_page, 'lxml')
for tag in tags:
	search_limit_class = 0
	search_limit_id = 0
	classes_ = response.findAll(tag, attrs={'class': '', 'href': re.compile("^http://")})
	for class_ in classes_:
		print(class_.get('href'))