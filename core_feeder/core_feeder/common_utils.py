from firebase_admin import credentials, firestore, auth
import firebase_admin

firebaseConfig = {
  "type": "service_account",
  "project_id": "ubuntu-ea452",
  "private_key_id": "***REMOVED***",
  "private_key": "-----BEGIN PRIVATE KEY-----\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\nn5PK2jMq9iiMr4X23yXGU25z\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-n83r1@ubuntu-ea452.iam.gserviceaccount.com",
  "client_id": "118156260357453720158",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-n83r1%40ubuntu-ea452.iam.gserviceaccount.com"
}


cred = credentials.Certificate(firebaseConfig)
firebase_admin.initialize_app(cred)
db = firestore.client()





