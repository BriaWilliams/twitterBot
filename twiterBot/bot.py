#!usr/bin/python

from config import getApi
import os
import requests
import random
import urllib.request

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
def getRoverCam(rovers):
    '''Takes in dictionary with rovers as keys and cameras as values.
        If a specific rover key is selected then a random camera will be selected from its list of values.
         Returns chosen camera as a string'''

    if randomRovers == "curiosity":
        randomCam= random.choice(rovers['curiosity'])

    elif randomRovers == "opportunity":
        randomCam= random.choice(rovers['opportunity'])

    else:
        randomCam = random.choice(rovers['spirit'])

    print(randomCam)
    return randomCam

req = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/{randomRovers}/photos?sol=1000&camera={getRoverCam(rovers)}&api_key=DEMO_KEY')
reqDict = req.json()
#reqURL = req.url()
print(req.url)

#imageURL = (reqDict['photos'][0]['img_src'])
#urllib.request.urlretrieve(imageURL, 'mars.jpg')
#print(type(imageURL))


# def postStatus(update):
#     #status = api.PostUpdate(update)
#     print(status)

def postPhoto(update):
    print(api.PostUpdate(update, media ="mars.jpg"))
    os.remove("mars.jpg")

#postPhoto("From #BriaBot: Did you know that the Mars Rover took this photo?")
