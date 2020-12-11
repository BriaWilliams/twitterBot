#!usr/bin/python

from util import *
import os
import urllib.request
import time
import requests
import random
from config import getApi


api = getApi()
nasaAPI = 'Rn9kSqjsLbjwABsvb2DFstOBjht6VRkesybxBSKh'

rovers = {'curiosity':
                ['fhaz', 'rhaz', 'mast', 'chemcam', 'mahli', 'mardi', 'navcam'],
          'opportunity':
                ['fhaz', 'rhaz','navcam', 'pancam', 'minites'],
          'spirit':
                ['fhaz', 'rhaz','navcam', 'pancam', 'minites']
         }

randomRovers = random.choice(list(rovers))
print(randomRovers)

def getRandomDic():
    '''Takes in dictionary with rovers as keys and cameras as values.
        If a specific rover key is selected then a random camera will be selected from its list of values.
         Returns chosen camera as a string'''
    if randomRovers == "curiosity":
        randomCam = random.choice(rovers['curiosity'])
    elif randomRovers == "opportunity":
        randomCam= random.choice(rovers['opportunity'])
    else:
        randomCam = random.choice(rovers['spirit'])
    req = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/{randomRovers}/photos?sol=1000&camera={randomCam}&api_key={nasaAPI}')
    return req.json()


def postPhoto():
    dictionary = getRandomDic()
    cameraName = ''
    if dictionary['photos'] != []:
        if len(dictionary['photos']) == 1:
            cameraName = dictionary['photos'][0]['camera']['full_name']
            imageURL = dictionary['photos'][0]['img_src']
            urllib.request.urlretrieve(imageURL, 'mars.jpg')
            status = f"From #BriaBot: The {randomRovers.capitalize()} Rover took this photo using the {cameraName}."
            api.PostUpdate(status, media="mars.jpg")
            os.remove("mars.jpg")
        else:
            index = random.randint(0, len(dictionary['photos']) - 1)
            cameraName = dictionary['photos'][index]['camera']['full_name']
            imageURL = dictionary['photos'][index]['img_src']
            urllib.request.urlretrieve(imageURL, 'mars.jpg')
            status = f"From #BriaBot: The {randomRovers.capitalize()} Rover took this photo using the {cameraName}."
            api.PostUpdate(status, media="mars.jpg")
            os.remove("mars.jpg")

while True:
   postPhoto()
   getRandomDic()
   time.sleep(60)

