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

print(len(result.val()))