# IBM Functions Python 3.11 Runtime Container

## Migrating from Python:3.9 to Python:3.11
  - Replaced `cloudant` with `ibmcloudant`  
    - The `cloudant` sdk has moved to the new `ibmcloudant` sdk. It includes a number of breaking changes. See [migration guide](https://github.com/cloudant/python-cloudant/blob/master/MIGRATION.md) for more information.
    - [pypi cloudant](https://pypi.org/project/cloudant/)
  - Replaced `watson-developer-cloud` with `ibm-watson`
    - The `watson-developer-cloud` sdk has renamed to the new `ibm-watson` sdk and includes breaking changes.
    - [pypi ibm-watson](https://pypi.org/project/ibm-watson/)
    - [github ibm-watson](https://github.com/watson-developer-cloud/python-sdk)

## 1.4.2
Changes:
  - Bump to newer parent image (vulnerability fixes) f707898

Python version:
  - [3.11.9](https://www.python.org/downloads/release/python-3119/)

Python packages:
  - The file [requirements.txt](requirements.txt) lists the packages we guarantee to be included in this runtime.<br/>
    Ensure that you only use packages mentioned there.<br/>
    Other python packages might be part of this runtime, but only due to indirect dependencies of the above listed packages. These indirectly included packages are candidates to be removed at any time in case they are not required by the referring package anymore.

# 1.4.1
Changes:
  - Bump to newer parent image (vulnerability fixes) 1389697

Python version:
  - [3.11.8](https://www.python.org/downloads/release/python-3118/)

Python packages:
  - The file [requirements.txt](requirements.txt) lists the packages we guarantee to be included in this runtime.<br/>
    Ensure that you only use packages mentioned there.<br/>
    Other python packages might be part of this runtime, but only due to indirect dependencies of the above listed packages. These indirectly included packages are candidates to be removed at any time in case they are not required by the referring package anymore.

# 1.4.0 
Changes:
  - Bump to newer parent image (vulnerability fixes) c0a1e6d

Python version:
  - [3.11.7](https://www.python.org/downloads/release/python-3117/)

Python packages:
  - The file [requirements.txt](requirements.txt) lists the packages we guarantee to be included in this runtime.<br/>
    Ensure that you only use packages mentioned there.<br/>
    Other python packages might be part of this runtime, but only due to indirect dependencies of the above listed packages. These indirectly included packages are candidates to be removed at any time in case they are not required by the referring package anymore.

# 1.3.0 
Changes:
  - Bump to newer parent image (vulnerability fixes) 4546acf

Python version:
  - [3.11.6](https://www.python.org/downloads/release/python-3116/)

Python packages:
  - The file [requirements.txt](requirements.txt) lists the packages we guarantee to be included in this runtime.<br/>
    Ensure that you only use packages mentioned there.<br/>
    Other python packages might be part of this runtime, but only due to indirect dependencies of the above listed packages. These indirectly included packages are candidates to be removed at any time in case they are not required by the referring package anymore.

## 1.2.0
Changes:
  - Bump to newer parent image (vulnerability fixes) b5b65de

Python version:
  - [3.11.5](https://www.python.org/downloads/release/python-3115/)

Python packages:
  - The file [requirements.txt](requirements.txt) lists the packages we guarantee to be included in this runtime.<br/>
    Ensure that you only use packages mentioned there.<br/>
    Other python packages might be part of this runtime, but only due to indirect dependencies of the above listed packages. These indirectly included packages are candidates to be removed at any time in case they are not required by the referring package anymore.

## 1.1.0
Changes:
  - Bump to newer parent image (vulnerability fixes).
  - Bump tornado from 6.2 to 6.3.2 (vulnerability fixes).
  - Bump requests from 2.28.2 to 2.31.0 (vulnerability fixes).
  - Bump flask from 2.2.3 to 2.3.2 (vulnerability fixes).

Python version:
  - [3.11.3](https://www.python.org/downloads/release/python-3113/)

Python packages:
  - The file [requirements.txt](requirements.txt) lists the packages we guarantee to be included in this runtime.<br/>
    Ensure that you only use packages mentioned there.<br/>
    Other python packages might be part of this runtime, but only due to indirect dependencies of the above listed packages. These indirectly included packages are candidates to be removed at any time in case they are not required by the referring package anymore.

## 1.0.0
Changes:
 - actionloop proxy version 1.20@1.22.0
  - update all packages to their lates versions 

Python version:
  - [3.11.3](https://www.python.org/downloads/release/python-3113/)

Python packages:
  - The file [requirements.txt](requirements.txt) lists the packages we guarantee to be included in this runtime.<br/>
    Ensure that you only use packages mentioned there.<br/>
    Other python packages might be part of this runtime, but only due to indirect dependencies of the above listed packages. These indirectly included packages are candidates to be removed at any time in case they are not required by the referring package anymore.
