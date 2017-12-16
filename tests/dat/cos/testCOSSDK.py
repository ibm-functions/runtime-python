"""Python test fixture to check that cos sdk loads"""

import ibm_boto3
from ibm_botocore.client import Config


def main(dict):
    api_key = 'API_KEY'
    service_instance_id = 'RESOURCE_INSTANCE_ID'
    auth_endpoint = 'https://iam.bluemix.net/oidc/token'
    service_endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'

    cos = ibm_boto3.resource('s3',
                             ibm_api_key_id=api_key,
                             ibm_service_instance_id=service_instance_id,
                             ibm_auth_endpoint=auth_endpoint,
                             config=Config(signature_version='oauth'),
                             endpoint_url=service_endpoint)

    return {"message": "ibm_boto3 loaded",
            "meta-model": cos.meta.resource_model.name}


if __name__ == "__main__":
    # execute only if run as a script
    print(main({}))
