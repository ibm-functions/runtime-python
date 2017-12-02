# IBM Cloud Functions runtime for nodejs

[![Build Status](https://travis-ci.org/ibm-functions/runtime-python.svg?branch=master)](https://travis-ci.org/ibm-functions/runtime-python)

The runtime provides [python v3](python3/) with a set of [python packages](python/requirements.txt)

The runtime provides the following npm packages for [IBM Cloud](https://bluemix.net):
- IBM DB2/DashDB and IBM Informix [ibm_db@2.2.1](https://www.npmjs.com/package/ibm_db)
- IBM Cloudant [cloudant@1.10.0](https://www.npmjs.com/package/cloudant)

### How to use as a docker Action
To use as a docker action
```
bx wsk action update myAction myAction.js --docker ibmfunctions/action-python-v3
```
This works on any deployment of Apache OpenWhisk or IBM Cloud Functions

### Future: IBM Cloud Functions (based on Apache OpenWhisk)
To use as a python kind action
```
bx wsk action update myAction myAction --kind python:3
```
Tip: Not available yet in the IBM Cloud

### Working with the local git repo 
Prerequisite: *Export* OPENWHISK_HOME to point to your incubator/openwhisk cloned directory.

```
./gradlew nodejs8:distDocker
```
This will produce the image `whisk/action-python-v3`

Build and Push image
```
docker login
./gradlew python3:distDocker -PdockerImagePrefix=$prefix-user -PdockerRegistry=docker.io
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


To run all tests: `./gradlew tests:test` this include tests depending on credentials

To run all tests except those which do not rely on credentials `./gradlew tests:testWithoutCredentials`

To run a single test-class: `./gradlew tests:test --tests <SomeGradleTestFilter>`


# License
[Apache 2.0](LICENSE.txt)