from google.cloud import firestore

def get_firebase_db(firebase_key_path):
    db = firestore.Client.from_service_account_json(firebase_key_path)
    return db