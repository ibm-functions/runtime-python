# IBM Functions Python 3.9 Runtime Container

## Migrating from Python:3.7 to Python:3.9
  - Replaced `cloudant` with `ibmcloudant`  
    - The `cloudant` sdk has moved to the new `ibmcloudant` sdk. It includes a number of breaking changes. See [migration guide](https://github.com/cloudant/python-cloudant/blob/master/MIGRATION.md) for more information.
    - [pypi cloudant](https://pypi.org/project/cloudant/)
  - Replaced `watson-developer-cloud` with `ibm-watson`
    - The `watson-developer-cloud` sdk has renamed to the new `ibm-watson` sdk and includes breaking changes.
    - [pypi ibm-watson](https://pypi.org/project/ibm-watson/)
    - [github ibm-watson](https://github.com/watson-developer-cloud/python-sdk)

# 1.1.1
Changes:
  - update baseimage tag to get latest security fixes and new python base (b74ffb7)
  - Python version as of deployment time >=3.9.16

## 1.1.0
Changes:
  - Update to new parent image to get latest security fixes and to update to action proxy version 1.18@1.17.1.
  - Python version as of deployment time >=3.9.15
  
## 1.0.1
Changes:
  - update pip packages in requirements.txt
  - lxml 4.7.1 -> 4.9.1
  - twisted 21.7.0 -> 22.4.0
  - PyJWT 2.3.0 -> 2.4.0
  - Pillow = 9.0.0 -> 9.0.1
  - Update to new parent image to get latest security fixes

Python version:
- [3.9.13](https://www.python.org/downloads/release/python-3913/)

## 1.0.0
Changes:
  - update all packages to their lates versions 

Python version:
  - [3.9.9](https://www.python.org/downloads/release/python-399/)

Python packages:
  - The file [requirements.txt](requirements.txt) lists the packages we guarantee to be included in this runtime.<br/>
    Ensure that you only use packages mentioned there.<br/>
    Other python packages might be part of this runtime, but only due to indirect dependencies of the above listed packages. These indirectly included packages are candidates to be removed at any time in case they are not required by the referring package anymore.
