#!/usr/bin/env bash

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

sudo apt-get update --quiet > /dev/null
sudo apt-get install -y build-essential setuptool liblapack-dev liblapack3 liblapack3gf libgtk2.0-dev gfortran libblas3gf	liblapack3gf libopencv-dev libopencv-highgui-dev libcvaux-dev python-opencv python-setuptools python-virtualenv

 
