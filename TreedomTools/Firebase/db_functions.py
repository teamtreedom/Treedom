from Firebase import db_connect

FIREBASE_KEY_PATH = "C:/Users/Treedom/Desktop/treedom-tools-firebase-adminsdk-xn36r-5f0eda3b35.json"
db = db_connect.get_firebase_db(FIREBASE_KEY_PATH)

def add_document(collection_path, document_json, custom_document_id = None):
    document_ref = db.collection(collection_path).document(custom_document_id).set(document_json)
    response_dict = {
        "collection_path": collection_path,
        "document_json": document_json,
        "document_firebase_id": document_ref.id
    }
    return response_dict

def get_collection(collection_path):
    collection_ref = db.collection(collection_path)
    collection_docs = collection_ref.get()

    response_dict = collection_docs
    ## check this to see if the return object is a dict or firebase obj,
    ## in which case it would need to be converted

    return response_dict