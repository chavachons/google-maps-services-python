import googlemaps
import pyrebase
import json
from datetime import datetime

API_KEY = 'AIzaSyAAKEfRsQq9pukks7umWncxcbPUIRPuEyA'
LOCATION = (18.7296314, 98.9279261)
RADIUS = 50000
LANGUAG = 'th'
MIN_PRICE = None
MAX_PRICE = None
OPEN_NOW = False
TYPE = 'food'

gmaps = googlemaps.Client(key=API_KEY)
geocode_result = gmaps.places('', location=LOCATION,
                           radius=RADIUS, language=LANGUAG,
                           min_price=MIN_PRICE, max_price=MAX_PRICE, 
                           open_now=OPEN_NOW, type=TYPE)

print(json.dumps(geocode_result['results'], indent=4, ensure_ascii=False ))

print(len(geocode_result['results']))

config = {
  "apiKey": "AIzaSyAAKEfRsQq9pukks7umWncxcbPUIRPuEyA",
  "authDomain": "travelai-1509135226166.firebaseapp.com",
  "databaseURL": "https://travelai-1509135226166.firebaseio.com",
  "storageBucket": "gs://travelai-1509135226166.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
db.child("users").child("Morty")