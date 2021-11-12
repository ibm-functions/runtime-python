"""Python test fixture to check that watson sdk loads"""

from watson_developer_cloud import DiscoveryV1

def main(dict):
    load_successful = False
    if DiscoveryV1.default_url == "https://gateway.watsonplatform.net/discovery/api":
        load_successful = True

    return {
        "load_successful" : load_successful
    }

if __name__ == "__main__":
    # execute only if run as a script
    print(main({}))
