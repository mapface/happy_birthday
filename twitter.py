# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:11:12 2021

@author: Alistair
"""

#-*- coding: utf-8 -*-

#imports
import wikipedia
from datetime import datetime
import random
from twython import Twython

#twitter credentials
from auth import(consumer_key,
                 consumer_secret,
                 access_token,
                 access_token_secret)

#consume credentials with Twython
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)

#Get current date
dt_now = datetime.now()
print(dt_now)
#Arrange current date into a string into Month_Day format 
date_string = str(datetime.now().strftime("%B") + " " + datetime.now().strftime("%d"))
print(date_string)

#Use date_string to find the appropriate wikipedia page
wiki = wikipedia.WikipediaPage(date_string)

#Navigate to and subset the 'Births' section of the wikipedia page
text = wiki.section('Births')

text = text.replace(' – ',',')
text = text.replace('  ','')
text = text.replace('(',', ')
text = text.replace(')','')
text = text.replace(' , ',',')

#Split the lines and then choose a random line
myline = random.choice(list(text.splitlines()))

#Split the chosen line by ','
parts = myline.split(",") 
name = parts[1]
desc = parts[2]
age = int(dt_now.strftime("%Y")) - int(parts[0])

#Define a function that will update your twitter status
def hbd(x):
    if "d." in x:
       # pass
       twitter.update_status(status=("\U0001F973 Happy Birthday to %s!%s who would have turned %s today. \U0001F973" % (name,desc,age)))
    else:
       twitter.update_status(status=("\U0001F973 Happy Birthday to %s!%s who turns %s today. \U0001F973" % (name,desc,age)))

#tweet! - call the function
hbd(myline)
       
