import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyBOwegw3CG6IcvdubdcPc54e38yK8Pyc-k",
  "authDomain": "clientdetails-f1fcb.firebaseapp.com",
  "projectId": "clientdetails-f1fcb",
  "storageBucket": "clientdetails-f1fcb.firebasestorage.app",
  "messagingSenderId": "1010297172223",
  "appId": "1:1010297172223:web:a0904c300dc7ef0fe69cca",
  "measurementId": "G-G2GK37MQTH",
  "databaseURL":"https://clientdetails-f1fcb-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
# data={
#     'name':"varun",
#     'age':21
# }
# db.set(data)
# db.update({'address':'india'})

