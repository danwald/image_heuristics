#!/usr/bin/env bash

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

apt-get update --quiet > /dev/null
apt-get install -y build-essential python-dev python-setuptools liblapack-dev liblapack3gf libgtk2.0-dev gfortran libblas3gf liblapack3gf libopencv-dev libopencv-highgui-dev libcvaux-dev python-opencv python-setuptools python-virtualenv libjpeg-dev libzlib1g-dev libfreetype6-dev

echo "Manually linking libs for PIL to find"
ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
ln -s /usr/lib/`uname -i`-linux-gnu/libzlib.so /usr/lib/
ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
