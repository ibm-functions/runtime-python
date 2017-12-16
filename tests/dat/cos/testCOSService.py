"""Python test fixture to check that cos sdk loads and connect to COS Service"""

import ibm_boto3
from ibm_botocore.client import Config


def main(args):
    auth_endpoint = 'https://iam.bluemix.net/oidc/token'
    service_endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'

    api_key = args["__bx_creds"]["cloud-object-storage"]["apikey"]
    service_instance_id = args["__bx_creds"]["cloud-object-storage"]["resource_instance_id"]

    cos = ibm_boto3.client('s3',
                           ibm_api_key_id=api_key,
                           ibm_service_instance_id=service_instance_id,
                           ibm_auth_endpoint=auth_endpoint,
                           config=Config(signature_version='oauth'),
                           endpoint_url=service_endpoint)

    bucket = "ibm-functions-devops-testing"
    key = "testdata.txt"
    response = cos.get_object(Bucket=bucket, Key=key, ResponseContentType="application/text")
    text = response["Body"].read().decode("utf-8")

    return {"data": text}


if __name__ == "__main__":
    # execute only if run as a script
    input = {
        "__bx_creds": {
            "cloud-object-storage": {
                "apikey": "<apikey from credentials>",
                "resource_instance_id": "<resource_instance_id from credentials>"
            }
        }
    }
    print(main(input))
