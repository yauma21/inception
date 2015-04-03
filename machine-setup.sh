#!/bin/bash
set -e
sudo apt-get update && sudo apt-get install curl python-pip
curl https://raw.githubusercontent.com/ivanmoore/setup/master/setup.sh | bash
curl https://raw.githubusercontent.com/ivanmoore/setup/master/setup.bat | bash
sudo pip install -r requirements.txt
wget http://download.go.cd/gocd-deb/go-server-14.2.0-377.deb
sudo dpkg -i go-server-14.2.0-377.deb
wget http://download.go.cd/gocd-deb/go-agent-14.2.0-377.deb
sudo dpkg -i go-agent-14.2.0-377.deb
sudo /etc/init.d/go-agent start
ssh-keygen -t rsa -C "ivan@teamoptimization.com"
cat ~/.ssh/id_rsa.pub

