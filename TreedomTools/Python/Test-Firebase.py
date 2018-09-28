from google.cloud import firestore
from Users.volunteer import Volunteer

FIREBASE_KEY_PATH = "C:/Users/Treedom/Desktop/treedom-tools-firebase-adminsdk-xn36r-5f0eda3b35.json"
db = firestore.Client.from_service_account_json(FIREBASE_KEY_PATH)

new_volunteer_ref = db.collection('volunteers').document(None)
new_volunteer_ref.set(
    Volunteer("Vlad Deshkovich",25).to_dict()
)
print(new_volunteer_ref.id)