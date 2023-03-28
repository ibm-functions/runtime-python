"""Python test fixture to check that watson sdk loads"""

from ibm_watson.discovery_v1 import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import sys

def packageAvailable(package):
    if package in sys.modules:
        return True
    else:
        return False

def main(dict):
    load_successful = False
    if packageAvailable("ibm_watson.discovery_v1") and packageAvailable("ibm_cloud_sdk_core.authenticators"):
        load_successful = True

    return {
        "load_successful" : load_successful
    }


if __name__ == "__main__":
    # execute only if run as a script
    print(main({}))
