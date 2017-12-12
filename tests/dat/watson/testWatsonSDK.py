"""Python test fixture to check that watson sdk loads"""

from watson_developer_cloud import DiscoveryV1

def main(dict):
    return {"message": DiscoveryV1.VERSION_DATE_2017_11_07}

if __name__ == "__main__":
    # execute only if run as a script
    print(main({}))
