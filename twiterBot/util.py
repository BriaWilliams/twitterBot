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

def getRandomDic():
    '''Takes in dictionary with rovers as keys and cameras as values.
        If a specific rover key is selected then a random camera will be selected from its list of values.
         Returns chosen camera as a string'''
    if randomRovers == "curiosity":
        randomCam= random.choice(randomRovers['curiosity'])
    elif randomRovers == "opportunity":
        randomCam= random.choice(randomRovers['opportunity'])
    else:
        randomCam = random.choice(randomRovers['spirit'])
    req = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/{randomRovers}/photos?sol=1000&camera={randomCam}&api_key={nasaAPI}')
    return req.json()
