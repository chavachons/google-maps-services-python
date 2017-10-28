# Google Map
import googlemaps
import json
from datetime import datetime

API_KEY = 'AIzaSyApSqzNGQK1GeCSVl5KzsUAjf58AA57fNU'
LANGUAG = 'th'
gmaps = googlemaps.Client(key=API_KEY)

def getDetail(id):
  detail = gmaps.place(place_id=id, language=LANGUAG)
  print(detail)


# Firebase
import pyrebase
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
serviceAccountKey = os.path.join(THIS_FOLDER, 'serviceAccountKey.json')

config = {
  "apiKey": "AIzaSyCmzbTkBNwtU0_pE82yfDCVzld0dRaomB4",
  "authDomain": "travelai-1509135226166.firebaseapp.com",
  "databaseURL": "https://travelai-1509135226166.firebaseio.com",
  "storageBucket": "gs://travelai-1509135226166.appspot.com",
  "serviceAccount": serviceAccountKey
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

result = db.child('places').get()

places = db.child("places").order_by_key().start_at("0").limit_to_first(1).get()
for place in places.each():
  print(place.key())
  print(place.val()['id'])
  print("===============================")
  # getDetail(id=place.val()['id'])
  pass

# print(places.val())

# getDetail(id="b735187076e0a2bd5b694810f3a6e5248536e303")
gmaps.place(place_id="b735187076e0a2bd5b694810f3a6e5248536e303")
