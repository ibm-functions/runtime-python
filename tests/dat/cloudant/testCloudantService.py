"""Python test fixture to check that cloudant sdk loads"""

from cloudant.client import Cloudant
from cloudant.client import CloudantClientException


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

    data = {
        "_id": "p3",
        "firstname": "Suzzy",
        "lastname": "Queue"
    }
    my_document = my_database.create_document(data)
    if my_document.exists():
        print('SUCCESS DOC exist!!')

    my_document_read = my_database['p3']

    return my_document_read


if __name__ == "__main__":
    # execute only if run as a script
    print(main({}))
