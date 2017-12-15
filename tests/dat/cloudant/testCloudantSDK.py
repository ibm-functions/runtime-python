"""Python test fixture to check that cloudant sdk loads"""

from cloudant.client import Cloudant


def main(dict):
    client = Cloudant("test-user", "test", url='https://{0}'.format("host.cloudant.com"))
    return {"_user": client._user,
            "server_url": client.server_url}


if __name__ == "__main__":
    # execute only if run as a script
    print(main({}))
