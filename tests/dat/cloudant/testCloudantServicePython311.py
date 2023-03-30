"""Python test fixture to check that cloudant sdk loads"""
import json
import uuid

#from simplejson.decoder import JSONDecoder as json_decoder
# from cloudant.document import Document

# from cloudant.client import Cloudant
# from cloudant.client import CloudantClientException

from ibmcloudant.cloudant_v1 import Document, CloudantV1
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

#def test_create_doc(db, _id, data):
def test_create_doc(client, db, id, data):
    """Test document create with id"""
    doc = Document(
        id=id,
        type=data["type"],
        agentId=data["agentId"]
    )
    try:
        response = client.post_document(db=db,document=doc).get_result()
        if response["ok"]:
            print(f'SUCCESS CREATE: Document with id {id}: {data}')
    except:
        raise ValueError(f'FAILED CREATE: Document not created with id {id}')


def test_update_doc(client, db, _id, doc_updates):
    """Test document update by Id."""
    try:
        doc_old = test_fetch_doc_by_id(client, db, _id)
        doc = Document(
            id=_id,
            lastname=doc_updates["lastname"],
            rev=doc_old["_rev"]
        )
        response = client.post_document(db=db, document=doc).get_result()
        if response["ok"]:
            print(f'SUCCESS UPDATE: Document with id {_id}: {doc_updates}')
    except:
        print('FAILED UPDATE')
        raise


def test_get_doc_by_id(client, db, _id):
    """Test document get by Id."""
    try:
        response = client.get_document(
            db=db,
            doc_id=_id
        ).get_result()

        if "error" in response: 
            raise ValueError(f'Document with id {_id} not found')
        else:
            print(f'SUCCESS GET: Document with id {_id}: {response}')
    except:
         print('FAILED GET:')
         raise
    

def test_fetch_doc_by_id(client, db, _id):
    """Test document fetch by Id."""
    try:
        response = client.get_document(
            db=db,
            doc_id=_id
        ).get_result()
        if "error" in response: 
            raise ValueError(f'Document with id {_id} not found')
        else:
            print(f'SUCCESS GET: Document with id {_id}: {response}')
            return response
    except:
        print('FAILED FETCH:')
        raise

def test_delete_doc_by_id(client, db, id):
    """Test document delete by Id."""
    try:
        doc = test_fetch_doc_by_id(client, db, id)
        response = client.delete_document(
            db=db,
            doc_id=doc["_id"],
            rev=doc["_rev"]
        ).get_result()
        if "ok" in response:
            print(f'SUCCESS DELETE Document with id {id}: {response}')
    except:
        print('FAILED DELETE')
        raise

def main(dict):
    user = dict.get("username", "<username from credentials>")
    passwd = dict.get("password", "<password from credentials>")
    host = dict.get("host", "<host from credentials>")
    db_name = "test_cloud_functions_python_3_ibm_runtime"
    authenticator = BasicAuthenticator(user, passwd)
    client = CloudantV1(authenticator=authenticator)
    client.set_service_url('https://{0}'.format(host))
    
    # try to delete the database if exists
    try:
        response = client.delete_database(db=db_name).get_result()
        if "error" in response:
            print("failed to delete")
        else:
            print('DB was deleted!!')
    except:
        print("failed to delete")

    # try to create database
    try:
        response = client.put_database(db=db_name).get_result()
        if "ok" in response:
            print('SUCCESS DB exists!!')
    except:
        print("failed to create")

        

    """Sample document"""
    _id = str(uuid.uuid4())
    data = {"agentId": "Suzzy", "type": "User"}
    update_data = {"lastname":"Queue"}

    """Run tests"""
    
    test_create_doc(client, db_name, _id, data)
    test_update_doc(client, db_name, _id, update_data)
    test_get_doc_by_id(client, db_name, _id)
    doc = test_fetch_doc_by_id(client, db_name, _id)
    test_delete_doc_by_id(client, db_name, doc['_id'])

    return doc


if __name__ == "__main__":
    # execute only if run as a script
    print(main({}))