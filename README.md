# Pre-requisite:

## Installation for python 2.7 and tools related in Raspberry Pi 3 OS
```
sh env_install.sh 
```
## Manual Installation
```
$ sudo apt-get update
$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev
$ sudo apt-get install tcpflow
$ sudo apt-get install python-tk
$ sudo apt-get install git
$ sudo apt-get install tshark
$ sudo apt-get install curl
$ curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
$ sudo python get-pip.py
```
## MacOS user can use brew instead of apt-get
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install python
```
## Installation for GTK3 backend for matplotlib (if unavailable)
```
$ sudo apt-get install python-gi-cairo
```
## Enable WIFI connection of WLAN0 on RaspBerry Pi in file /etc/network/interfaces
```
allow-hotplug wlan0
iface wlan0 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

## Setup WIFI in same subnet of broker server in file /etc/wpa_supplicant/wpa_supplicant.conf
```
network={
	ssid="TP-LINK_11EAB8"
	psk="1234567890123"
	key_mgmt=WPA-PSK
}
```
