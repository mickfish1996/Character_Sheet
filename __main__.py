import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(".\character-sheet-68995-firebase-adminsdk-4b2e4-a00dcf1875.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

results = db.collection("users").where("email", "==", "mickfish1996@gmail.com").get()
data = None
for result in results:
    data = result.to_dict()

print(data)