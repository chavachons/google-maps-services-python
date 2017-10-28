import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCtq57CiDDKwLWs7E7914so29vjNDK-MCw')


geocode_result = gmaps.places('restaurant','กรุงเทพ',50000,'Thai')

print(geocode_result)