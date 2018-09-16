#!/usr/bin/python2.7
import praw
import itertools
import string
import config
import json

#Getting all possible characters
chars= string.ascii_lowercase+string.digits+"_-"

#Logging into Reddit
r = praw.Reddit(username=config.r_username, password=config.r_password,client_id=config.r_client_id,client_secret=config.r_client_secret,user_agent=config.r_user_agent)


#Opening the data file
with open("data.json","r") as f:
    data = json.loads(f.read())

#Producing all possible three-character usernames
users = list(itertools.product(chars,repeat=3))

#Iterating through possible usernames
for a in users:
    user = "".join(a)

    #Checking if the username has already been processed
    if user not in data:
        u = r.redditor(user)
        try:
            #Checking if account has available statistics
            created= u.created_utc
            data[user]=created

            print user, created
        
        except Exception as exc:
            #The account was shadowbanned, deleted, or suspended. Account creation date is unknown.
            data[user]=str(exc)

            print user, exc
        #Writing to the data file.
        with open("data.json","w") as f:
            f.write(json.dumps(data,indent=4,sort_keys=True))

    else:
        #print user, 'already processed'
        pass





















