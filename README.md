# IBM Cloud Functions Runtime for Python
[![Build Status](https://travis-ci.org/ibm-functions/runtime-python.svg?branch=master)](https://travis-ci.org/ibm-functions/runtime-python)

- The runtime provides [python v3.7](python3.7/) with a set of [python packages](python3.7/requirements.txt), see [python3.7/CHANGELOG.md](python3.7/CHANGELOG.md)
- The runtime provides [python v3.6](python3.6/) with a set of [python packages](python3.6/requirements.txt), see [python3.6/CHANGELOG.md](python3.6/CHANGELOG.md)

Some of the python packages are to be used on [IBM Cloud](https://cloud.ibm.com):
- IBM DB2/DashDB and IBM Informix - Python SDK [ibm_db](https://pypi.python.org/pypi/ibm_db)
- IBM Cloudant - Python SDK [cloudant](https://pypi.python.org/pypi/cloudant)
- IBM Watson Developer Cloud - Python SDK [watson-developer-cloud](https://pypi.python.org/pypi/watson-developer-cloud)
- IBM Cloud Object Storage - Python SDK [ibm-cos-sdk](https://pypi.python.org/pypi/ibm-cos-sdk)
- IBM Cloud SQL Query service - Python Client [ibmcloudsql](https://pypi.org/project/ibmcloudsql/)

Docker runtime is based on Debian/Ubuntu

### Hello Action
Write a function using [Apache OpenWhisk](https://apache.openwhisk.org) Serverless programming inteface
```python
def main(args):
    name = args.get("name", "stranger")
    greeting = "Hello " + name + "!"
    print(greeting)
    return {"greeting": greeting}
```

### IBM Cloud Functions (based on Apache OpenWhisk)
To use as a python kind action
```
bx wsk action update helloPython hello.py --kind python:3.7
```

### How to use as a docker Action locally
To use as a docker action
```
bx wsk action update helloPython hello.py --docker ibmfunctions/action-python-v3.7
```
This works on any deployment of Apache OpenWhisk or IBM Cloud Functions



### Working with the local git repo
Prerequisite: *Export* OPENWHISK_HOME to point to your `openwhisk` cloned directory.

```
./gradlew python3:distDocker
```
This will produce the image `whisk/action-python-v3.7`

Build and Push image
```
docker login
./gradlew python3.7:distDocker -PdockerImagePrefix=$prefix-user -PdockerRegistry=docker.io
```

Deploy OpenWhisk using ansible environment that adds the new king `python:3`
Assuming you have OpenWhisk already deploy localy and `OPENWHISK_HOME` pointing to root directory of OpenWhisk core repository.

Set `ROOTDIR` to the root directory of this repository.

Redeploy OpenWhisk
```
cd $OPENWHISK_HOME/ansible
ANSIBLE_CMD="ansible-playbook -i ${ROOTDIR}/ansible/environments/local"
$ANSIBLE_CMD setup.yml
$ANSIBLE_CMD couchdb.yml
$ANSIBLE_CMD initdb.yml
$ANSIBLE_CMD wipe.yml
$ANSIBLE_CMD openwhisk.yml
```

To use as docker action push to your own dockerhub account
```
docker tag whisk/action-python-v3 $user_prefix/action-python-v3
docker push $user_prefix/action-python-v3
```
Then create the action using your the image from dockerhub
```
wsk action update myAction myAction.py --docker $user_prefix/action-python-v3
```
The `$user_prefix` is usually your dockerhub user id.


### Testing
Install dependencies from the root directory on $OPENWHISK_HOME repository
```
./gradlew install
```

Using gradle to run all tests
```
./gradlew :tests:test
```
Using gradle to run some tests
```
./gradlew :tests:test --tests *ActionContainerTests*
```
Using IntelliJ:
- Import project as gradle project.
- Make sure working directory is root of the project/repo


#### Using container image to test
To use as docker action push to your own dockerhub account
```
docker tag whisk/action-python-v3 $user_prefix/action-python-v3
docker push $user_prefix/action-python-v3
```
Then create the action using your the image from dockerhub
```
wsk action update myAction myAction.py --docker $user_prefix/action-python-v3
```
The `$user_prefix` is usually your dockerhub user id.


## Maintenance Tasks

### Updating Python 3.7 runtime
- Check if there is a new version for Python 3.7 [python:3.7-stretch](https://hub.docker.com/_/python/).
  - If there is a new version check that the tag used in [python3.7/Dockerfile](python3.7/Dockerfile) is using the latest tag for [openwhisk/actionloop-python-v3.7](https://hub.docker.com/r/openwhisk/actionloop-python-v3.7/tags)
  - Update the ibm image [python3.7/Dockerfile](python3.7/Dockerfile) FROM usign the new upstream tag
- Check if there are new pip packages available
  - Use the latest released image to check the outdated pip packages
  ```
  docker run --rm -it ibmfunctions/action-python-v3.7:1.6.0 sh -c "pip list --outdated"
  ```
  - Update [python3.7/requirements.txt](python3.7/requirements.txt)
  - Update [python3.7/CHANGELOG.md](python3.7/CHANGELOG.md)

### Updating Python 3.6 runtime
- Check if there are new pip packages available
  - Use the latest released image to check the outdated pip packages
  ```
  docker run --rm -it ibmfunctions/action-python-v3.6:1.17.0 sh -c "pip list --outdated"
  ```
  - Update [python3.6/requirements.txt](python3.6/requirements.txt) only minor and patch levels.
  - Update [python3.6/CHANGELOG.md](python3.6/CHANGELOG.md)

### Pushing new versions for runtimes
- After the PR is merged and the master pass Travis CI, checkout master.
- Create tag for each runtime and push upstream
```
git tag 3.7@<new version>
git push upstream 3.7@<new version>
```
- After the image is deployed to production update the `latest` tag for each runtime.
```
git tag 3.7@latest -f
git push upstream 3.7@latest -f
```


# License
[Apache 2.0](LICENSE.txt)
