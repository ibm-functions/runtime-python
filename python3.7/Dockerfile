FROM openwhisk/action-python-v3.7:16c6081

COPY requirements.txt requirements.txt

RUN  apt-get update \
     # Upgrade installed packages to get latest security fixes if the base image does not contain them already.
     && apt-get upgrade -y --no-install-recommends \
     # cleanup package lists, they are not used anymore in this image
     && rm -rf /var/lib/apt/lists/* \
     # We do not have mysql-server installed but mysql-common contains config files (/etc/mysql/my.cnf) for it.
     # We need to add some dummy entries to /etc/mysql/my.cnf to sattisfy vulnerability checking of it.
     && echo "\n[mysqld]\nssl-ca=/tmp/ca.pem\nssl-cert=/tmp/server-cert.pem\nssl-key=/tmp/server-key.pem\n" >> /etc/mysql/my.cnf \
     # install additional python modules
     && pip install --upgrade pip setuptools six && pip install --no-cache-dir -r requirements.txt \
     # Show actual python version in the build output.
     && echo "Actual python version is:" \
     && python --version \
     # Show actual /bin/proxy version in the build output, makes it easier to check if go security fixes need to be applied.
     && echo "Actual /bin/proxy version is:" \
     && /bin/proxy -version
