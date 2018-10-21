"""Python test fixture to check that cloudant sdk loads"""
import json
import uuid

#from simplejson.decoder import JSONDecoder as json_decoder
from cloudant.document import Document

from cloudant.client import Cloudant
from cloudant.client import CloudantClientException

def test_create_doc(db, _id, data):
    """Test document create with id"""
    data['_id'] = _id
    doc = db.create_document(data)
    if doc.exists():
        print(f'SUCCESS CREATE: Document with id {_id}: {data}')
    else:
        print(f'FAILED CREATE: Document not created with id {_id}')

def test_update_doc(db, _id, doc_updates):
    """Test document update by Id."""
    orig_doc = Document(db, _id)
    if not orig_doc.exists():
        print(f'Document with id {_id} not found')
    try:
#        with Document(db, _id, decoder=json_decoder) as orig_doc:
        with Document(db, _id) as orig_doc:
            orig_doc.update(doc_updates)
            print(f'SUCCESS UPDATE: Document with id {_id}: {orig_doc}')
    except Exception as e:
        print(f'FAILED UPDATE: {e}')

def test_fetch_doc_by_id(db, _id):
    """Test document fetch by Id."""
    doc = Document(db, _id)
#    doc = Document(db, _id, decoder=json_decoder)
    if not doc.exists():
        print(f'Document with id {_id} not found')
    else:
        try:
            doc.fetch()
            print(f'SUCCESS FETCH: Document with id {_id}: {doc}')
        except Exception as e:
            print(f'FAILED FETCH: {e}')

def test_get_doc_by_id(db, _id):
    """Test document get by Id."""
    try:
        doc = db[_id]
        if not doc.exists():
            print(f'Document with id {_id} not found')
        else:
            print(f'SUCCESS GET: Document with id {_id}: {doc}')
    except Exception as e:
        print(f'FAILED GET: {e}')


def main(dict):
    user = dict.get("username", "<username from credentials>")
    passwd = dict.get("password", "<password from credentials>")
    host = dict.get("host", "<host from credentials>")
    db_name = "test_cloud_functions_python_3_ibm_runtime"

    client = Cloudant(user, passwd, url='https://{0}'.format(host), connect=True)

    try:
        client.delete_database(db_name)
    except CloudantClientException as ex:
        if ex.status_code != 404:
            raise CloudantClientException(ex.status_code, db_name)

    my_database = client.create_database('my_database')
    if my_database.exists():
        print('SUCCESS DB exists!!')

    """Sample document"""
    _id = str(uuid.uuid4())
    data = {"agentId": "Suzzy", "type": "User"}
    update_data = {"new_field":"new_value"}

    """Run tests"""
    test_create_doc(my_database, _id, data)
    test_update_doc(my_database,_id, update_data)
    test_fetch_doc_by_id(my_database,_id)
    test_get_doc_by_id(my_database,_id)


if __name__ == "__main__":
    # execute only if run as a script
    main({})