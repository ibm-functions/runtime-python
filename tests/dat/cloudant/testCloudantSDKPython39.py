"""Python test fixture to check that cloudant sdk loads"""
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import sys


def packageAvailable(package):
    if package in sys.modules:
        return True
    else:
        return False

def main(args):
    load_successful = False
    if packageAvailable("ibmcloudant.cloudant_v1") and packageAvailable("ibm_cloud_sdk_core.authenticators"):
        load_successful = True

    return {
        "load_successful" : load_successful
    }

if __name__ == "__main__":
    # execute only if run as a script
    print(main({}))
