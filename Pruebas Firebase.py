import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = firebase_admin.credentials.Certificate('/Users/antoniopatjane/Downloads/prueba-a5c60-firebase-adminsdk-x4i46-fa094b7b92.json')
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':'https://prueba-a5c60-default-rtdb.firebaseio.com/'
	})

from firebase_admin import db

ref = db.reference("/")

import json

with open("/Users/antoniopatjane/Downloads/data.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)