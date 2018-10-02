from Firebase import db_connect
from google.cloud import firestore
import google.cloud.exceptions

FIREBASE_KEY_PATH = "C:/Users/Treedom/Desktop/treedom-tools-firebase-adminsdk-xn36r-5f0eda3b35.json"
db = db_connect.get_firebase_db(FIREBASE_KEY_PATH)

def add_document(collection_path, document_json, custom_document_id = None):
    document_ref = db.collection(collection_path).document(custom_document_id)
    document_ref.set(document_json)
    response_dict = {
        "collection_path": collection_path,
        "document_json": document_json,
        "document_firebase_id": document_ref.id
    }
    return response_dict

def get_collection(collection_path):
    collection_ref = db.collection(collection_path).get()

    response_dict = collection_ref
    # check this to see if the return object is a dict or firebase obj,
    # in which case it would need to be converted

    return response_dict

def get_document(document_path):
    document_ref = db.document(document_path).get()

    response_dict = document_ref
    # check this to see if the return object is a dict or firebase obj,
    # in which case it would need to be converted

    return response_dict

def check_document_exists(document_path):
    ref = db.document(document_path)

    try:
        ref.get()
        return True
    except google.cloud.exceptions.NotFound:
        return False

def check_collection_exists(collection_path):
    ref = db.collection(collection_path)

    try:
        ref.get()
        return True
    except google.cloud.exceptions.NotFound:
        return False

def get_query_data(collection_path, attribute_name, operator, comparison):
    return_data = db.collection(collection_path).where(attribute_name, operator, comparison)
    # this will be a collection of docs, check object and return properly

    return return_data

def update_document(document_path, update_json, create_if_missing = False):
    doc_ref = db.document(document_path)
    doc_ref.update(update_json, firestore.CreateIfMissingOption(create_if_missing))

    # for nested jsons use parent.child in json update rather than parent : { child }
    # for timestamp updates use firestore.SERVER_TIMESTAMP
    # to delete a field, add "attribute_name" : firestore.DELETE_FIELD in json

    return {
        "new_json" : doc_ref.get(),
        "doc_id" : doc_ref.id
    }

def get_docs_with_order_and_limit(collection_path, order_attribute_name, limit):
    doc_ref = db.collection(collection_path).order_by(order_attribute_name).limit(limit)
    docs = doc_ref.get()

    #return in some way that makes sense

def delete_document(document_path):
    doc_ref = db.document(document_path).delete()
    # check doc_ref object after delete and return what is necessary


