# Google Map
import googlemaps
import json
from datetime import datetime

# ARRAY_TYPE = ['accounting','airport','amusement_park','aquarium','art_gallery','atm','bakery','bank','bar','beauty_salon','bicycle_store','book_store','bowling_alley','bus_station','cafe','campground','car_dealer','car_rental','car_repair','car_wash','casino','cemetery','church','city_hall','clothing_store','convenience_store','courthouse','dentist','department_store','doctor','electrician','electronics_store','embassy','fire_station','florist','funeral_home','furniture_store','gas_station','gym','hair_care','hardware_store','hindu_temple','home_goods_store','hospital','insurance_agency','jewelry_store','laundry','lawyer','library','liquor_store','local_government_office','locksmith','lodging','meal_delivery','meal_takeaway','mosque','movie_rental','movie_theater','moving_company','museum','night_club','painter','park','parking','pet_store','pharmacy','physiotherapist','plumber','police','post_office','real_estate_agency','restaurant','roofing_contractor','rv_park','school','shoe_store','shopping_mall','spa','stadium','storage','store','subway_station','synagogue','taxi_stand','train_station','transit_station','travel_agency','university','veterinary_care','zoo']
ARRAY_TYPE = ['fire_station','florist','funeral_home','furniture_store','gas_station','gym','hair_care','hardware_store','hindu_temple','home_goods_store','hospital','insurance_agency','jewelry_store','laundry','lawyer','library','liquor_store','local_government_office','locksmith','lodging','meal_delivery','meal_takeaway','mosque','movie_rental','movie_theater','moving_company','museum','night_club','painter','park','parking','pet_store','pharmacy','physiotherapist','plumber','police','post_office','real_estate_agency','restaurant','roofing_contractor','rv_park','school','shoe_store','shopping_mall','spa','stadium','storage','store','subway_station','synagogue','taxi_stand','train_station','transit_station','travel_agency','university','veterinary_care','zoo']

API_KEY = 'AIzaSyAAKEfRsQq9pukks7umWncxcbPUIRPuEyA'
LOCATION = (18.7296314, 98.9279261)
RADIUS = 50000
LANGUAG = 'th'
MIN_PRICE = None
MAX_PRICE = None
OPEN_NOW = False
TYPE = 'department_store'
gmaps = googlemaps.Client(key=API_KEY)

def searchPlaces(_type=None,_token=None):
    places_result = gmaps.places('', location=LOCATION,
                        radius=RADIUS, language=LANGUAG,
                        min_price=MIN_PRICE, max_price=MAX_PRICE, 
                        open_now=OPEN_NOW, type=_type, page_token=_token)

    aPlaces = places_result['results']
    insertData(places=aPlaces)
    if(len(aPlaces)==20):
        if 'next_page_token' in places_result:
            searchPlaces(_type=_type,_token=places_result['next_page_token'])

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

def insertData(places):
    for place in places:
        db.child("places").push(place)
        pass


for TYPE in ARRAY_TYPE:
    searchPlaces(_type=TYPE,_token=None)
    pass
