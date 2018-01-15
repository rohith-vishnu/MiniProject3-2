
# coding: utf-8

# In[24]:


import pandas as pd
import re
import numpy as np
import csv
from datetime import datetime
from dateutil.parser import parse


# In[25]:


f=open('chat.txt','r') #opening the text file mailed from whatsapp
content=f.readlines() # reading the content line by line


# In[26]:


data=[['TimeStamp','User','Message']] #Header for CSV file
myFile = open('chat_converted.csv', 'wb')  #Creating a new CSV file
writer = csv.writer(myFile)
writer.writerows(data) #Appending header 


# In[27]:


regexTS=re.compile((r'\d\d/\d\d/\d\d, \d\d:\d\d')) #Matches 08/10/16, 05:11
regexUser=re.compile(r'- [A-Z]*[a-z]*') #Matches first name of user
regexMsg=re.compile(': .*') # Matches message after :

myChat=[]

for line in content:
    timestamp=regexTS.findall(line)
    user=regexUser.findall(line)
    message=regexMsg.findall(line) 
    myChat=[(timestamp,user,message)] #creating row with timestamp, user and message
    
    writer = csv.writer(myFile)
    writer.writerows(myChat) #appending to CSV file row by row

myFile.close() #closing the file

