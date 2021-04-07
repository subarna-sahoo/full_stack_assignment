from firebase_admin import credentials, firestore, auth
import firebase_admin

firebaseConfig = {
#  your creadentials
}


cred = credentials.Certificate(firebaseConfig)
firebase_admin.initialize_app(cred)
db = firestore.client()





