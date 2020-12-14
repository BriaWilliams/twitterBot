#!usr/bin/python


import os
import urllib.request
import time
import requests
from config import getApi


api = getApi()
nasaAPI = 'Rn9kSqjsLbjwABsvb2DFstOBjht6VRkesybxBSKh'

def tweetRoverPhotos():
    marsSol = 1000
    req = requests.get(
        f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={str(marsSol)}&camera=mast&api_key={nasaAPI}')
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
            time.sleep(900)
            index +=1


while True:
    tweetRoverPhotos()





# def getRandomDic():
#     '''Takes in dictionary with rovers as keys and cameras as values.
#         If a specific rover key is selected then a random camera will be selected from its list of values.
#          Returns chosen camera as a string'''
#     if randomRovers == "curiosity":
#         randomCam = random.choice(rovers['curiosity'])
#     elif randomRovers == "opportunity":
#         randomCam= random.choice(rovers['opportunity'])
#     else:
#         randomCam = random.choice(rovers['spirit'])






