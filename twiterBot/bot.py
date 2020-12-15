#!usr/bin/python


import os
import urllib.request
import time
import requests
from config import getApi


api = getApi()
nasaAPI = 'Rn8kSqjsLbjwTQsvb2DFstOBjht4PRkesybxBSKh'

def tweetRoverPhotos():
    marsSol = 1000
    req = requests.get(
        f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={str(marsSol)}&camera=mast&api_key={nasaAPI}')
    dictionary = req.json()
    index = 4

    if index == len(dictionary['photos']) - 1:
        marsSol+=1
        print("Mars Sol= " + str(marsSol))

    else:
        for photo in dictionary['photos']:
            imageURL = dictionary['photos'][index]['img_src']
            urllib.request.urlretrieve(imageURL, 'curiosity.jpg')
            status = f"MARTIAN DIRT ALERT: Check out this cool photo from the Curiosity Rover taken using the MAST Camera."
            api.PostUpdate(status, media="curiosity.jpg")
            os.remove("curiosity.jpg")
            time.sleep(900)
            index +=1

while True:
    tweetRoverPhotos()





