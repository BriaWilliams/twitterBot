#!usr/bin/python


import os
import urllib.request
import time
import requests
from config import getApi


api = getApi()
nasaAPI = 'Rn8kSqjsLbjwTQsvb2DFstOBjht4PRkesybxBSKh'

def tweetRoverPhotos():
    """This function makes a request to the NASA API
    by changing parameters in the URL. It uses a conditional that
    loops through every photo taken on that Sol and post a tweet with the photo included."""

    marsSol = 1000 #A Sol is a measurement for a day on Mars
    req = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={str(marsSol)}&camera=mast&api_key={nasaAPI}')
    dictionary = req.json()
    index = 0

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
            time.sleep(900) #Post every 15 minutes
            index +=1

while True:
    tweetRoverPhotos()





