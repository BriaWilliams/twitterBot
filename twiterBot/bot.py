#!usr/bin/python

from config import getApi
import os
import requests

api = getApi()

req = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY&fbclid=IwAR3gRKZW3ULPYn9fvdh1lQFsjtoQhM9GelkH8EQonQKlgpUbQGBQ1mplQgI')
data = req.text
print(type(data))



# def postStatus(update):
#     #status = api.PostUpdate(update)
#     stat
#     print(status)

#postStatus("Hi, I'm BriaBot")
