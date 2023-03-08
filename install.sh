#!/bin/sh

# remove previous install
rm -rf /opt/pi-keyboard-api

# install necessary packages
apt-get update \
    && apt-get install --no-install-recommends -y python3.9 python3-pip git \
    && apt-get autoclean

# download git repo
git clone https://github.com/ErlendT/pi-keyboard-api.git

# install python requirements
pip3 install  -r pi-keyboard-api/requirements.txt

# install necessary sources and config files
mkdir -p /opt/pi-keyboard-api
cp -r pi-keyboard-api/app /opt/pi-keyboard-api/app
cp pi-keyboard-api/README.md /opt/pi-keyboard-api/README.md
cp pi-keyboard-api/LICENSE /opt/pi-keyboard-api/LICENSE

# register start-up script at init.d
cp pi-keyboard-api/init.sh /etc/init.d/pi-keyboard-api.sh
sudo chmod +x /etc/init.d/pi-keyboard-api.sh
sudo chown root:root /etc/init.d/pi-keyboard-api.sh
sudo update-rc.d pi-keyboard-api.sh defaults

# remove downloaded sources
rm -r pi-keyboard-api

reboot