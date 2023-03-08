#!/bin/sh
echo Running install script\n\n

echo Removing old install if exists
rm -rf /opt/pi-keyboard-api

echo Install necessary packages
apt-get update \
    && apt-get install --no-install-recommends -y python3.9 python3-pip git \
    && apt-get autoclean

echo Getting github repo
git clone https://github.com/ErlendT/pi-keyboard-api.git

echo Installing python requirements
pip3 install  -r pi-keyboard-api/requirements.txt

echo Installing pi-keyboard-api
mkdir -p /opt/pi-keyboard-api
cp -r pi-keyboard-api/app /opt/pi-keyboard-api/app
cp pi-keyboard-api/README.md /opt/pi-keyboard-api/README.md
cp pi-keyboard-api/LICENSE /opt/pi-keyboard-api/LICENSE

echo Register start-up script at init.d
cp pi-keyboard-api/init.sh /etc/init.d/pi-keyboard-api.sh
sudo chmod +x /etc/init.d/pi-keyboard-api.sh
sudo chown root:root /etc/init.d/pi-keyboard-api.sh
sudo update-rc.d pi-keyboard-api.sh defaults

echo Running cleanup
rm -r pi-keyboard-api

echo Rebooting
reboot