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

#
# Change USB to HID device using isticktoit script
# http://www.isticktoit.net/?p=1383
#
echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules

sudo touch /usr/bin/isticktoit_usb
sudo chmod +x /usr/bin/isticktoit_usb

cp /etc/rc.local /etc/rc.local.bak
sudo cat<<EOF > /etc/rc.local
#!/usr/bin/env bash
/usr/bin/isticktoit_usb
chmod 777 /dev/hidg0
exit 0
EOF
chmod 755 /etc/rc.local

sudo cat<<EOF > /usr/bin/isticktoit_usb
#!/bin/bash
cd /sys/kernel/config/usb_gadget/
mkdir -p isticktoit
cd isticktoit
echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB # USB2
mkdir -p strings/0x409
echo "fedcba9876543210" > strings/0x409/serialnumber
echo "Tobias Girstmair" > strings/0x409/manufacturer
echo "iSticktoit.net USB Device" > strings/0x409/product
mkdir -p configs/c.1/strings/0x409
echo "Config 1: ECM network" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/MaxPower

# Add functions here
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc
ln -s functions/hid.usb0 configs/c.1/
# End functions

ls /sys/class/udc > UDC
EOF

reboot