# local development
```
./gradlew python3:distDocker
docker login
./gradlew python3:distDocker -PdockerImagePrefix=<YourDockerId> -PdockerRegistry=docker.io
cd $OPENWHISK_HOME
bin/wskdev teardown -t <currentEnvironmentName>
cd ansible/environments/
ln -s /path/to/runtime-python3/ansible/environments/local ./local-ibm-py
cd ..
ansible-playbook -i environments/local-ibm-py setup.yml
ansible-playbook -i environments/local-ibm-py couchdb.yml -e mode=clean
ansible-playbook -i environments/local-ibm-py couchdb.yml
ansible-playbook -i environments/local-ibm-py initdb.yml
ansible-playbook -i environments/local-ibm-py wipe.yml
cd $OPENWHISK_HOME
./gradlew distDocker
cd ansible
ansible-playbook -i environments/local-ibm-py openwhisk.yml -e mode=clean
ansible-playbook -i environments/local-ibm-py openwhisk.yml
ansible-playbook -i environments/local-ibm-py postdeploy.yml

```

Create a python action and put it in file `test.py`:   
```  
def main(args):  
  return {"message":"Successfully called Simple Python Action"}  
```  

Run:   
```  
wsk -i action create test test.py --kind "python-ibm:3"  
wsk -i action invoke test -b  
```  
