FROM ubuntu:14.04
MAINTAINER Danny Crasto <danwald79@gmail.com>

WORKDIR /opt
RUN mkdir -p /var/run/uwsgi/ih
RUN apt-get update
RUN apt-get install -y build-essential python-dev python-setuptools liblapack-dev\
                       liblapack3gf libgtk2.0-dev gfortran libblas3gf libopencv-dev\
                       libopencv-highgui-dev libcvaux-dev python-opencv python-pip\
                       git-core libc-dev nginx vim libtiff4-dev libjpeg8-dev zlib1g-dev\
                       libfreetype6-dev liblcms1-dev libwebp-dev byobu

RUN git clone https://github.com/danwald/image_heuristics.git ih
RUN pip install -r /opt/ih/requirements/requirements.txt
RUN ln -sf /opt/ih/service/ih.nginx /etc/nginx/sites-available/ih.conf
RUN ln -sf /opt/ih/service/ih.nginx /etc/nginx/sites-enabled/ih
RUN rm /etc/nginx/sites-enabled/default
RUN service nginx restart
WORKDIR /opt/ih
RUN uwsgi --ini service/ih.uwsgi

EXPOSE 80
