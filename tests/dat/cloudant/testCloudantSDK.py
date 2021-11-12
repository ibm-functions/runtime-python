"""Python test fixture to check that cloudant sdk loads"""

from cloudant.client import Cloudant


def main(dict):
    load_successful = False
    client = Cloudant("test-user", "test", url='https://{0}'.format("host.cloudant.com"))
    if client._user == "test-user" and client.server_url == "https://host.cloudant.com":
        load_successful = True
    return {
        "load_successful" : load_successful
    }


if __name__ == "__main__":
    # execute only if run as a script
    print(main({}))
