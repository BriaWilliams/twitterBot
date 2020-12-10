#!usr/bin/python

from config import getApi
import os
import requests
import random

api = getApi()

nasaAPI = 'Rn9kSqjsLbjwABsvb2DFstOBjht6VRkesybxBSKh'

rovers = ['curiosity', 'opportunity', 'spirit']
cameras = ['fhaz', 'rhaz', 'mast', 'chemcam', 'mahli', 'mardi', 'navcam', 'pancam', 'minites']

randomCam = random.choice(cameras)

req = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera={randomCam}&api_key={nasaAPI}')
reqDict = req.json()

#print(reqDict['photos'][0]['id'])
print(req.url)



#{'photos':
#           [{'id': 102693,
#           'sol': 1000,
#           'camera':
#               {'id': 20,
#               'name': 'FHAZ',
#               'rover_id': 5,
#               'full_name': 'Front Hazard Avoidance Camera'},
#           'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG',
#           'earth_date': '2015-05-30',
#           'rover':
#               {'id': 5,
#               'name': 'Curiosity',
#               'landing_date': '2012-08-06',
#               'launch_date': '2011-11-26',
#               'status': 'active'}},
#           {'id': 102694,
#           'sol': 1000,
#           'camera':
#               {'id': 20,
#               'name': 'FHAZ',
#               'rover_id': 5,
#               'full_name': 'Front Hazard Avoidance Camera'},
#           'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FRB_486265257EDR_F0481570FHAZ00323M_.JPG',
#           'earth_date': '2015-05-30',
#           'rover':
#               {'id': 5,
#               'name': 'Curiosity',
#               'landing_date': '2012-08-06',
#               'launch_date': '2011-11-26',
#               'status': 'active'}}]}

# def postStatus(update):
#     #status = api.PostUpdate(update)
#     print(status)

#postStatus("Hi, I'm BriaBot")
