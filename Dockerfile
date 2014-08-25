FROM ubuntu:14.04
MAINTAINER Danny Crasto <danwald79@gmail.com>

RUN apt-get update
RUN apt-get install -y build-essential python-dev python-setuptools \
                       liblapack-dev liblapack3gf libgtk2.0-dev gfortran libblas3gf \
                       liblapack3gf libopencv-dev libopencv-highgui-dev libcvaux-dev \
                       python-opencv python-setuptools python-pip zlib1g-dev git-core \
                       libc-dev nginx uwsgi vim libtiff4-dev libjpeg8-dev zlib1g-dev \
                       libfreetype6-dev liblcms1-dev libwebp-dev

RUN git clone https://github.com/danwald/image_heuristics.git ih -b dockerize
RUN pip install -r /ih/requirements/requirements.txt
RUN ln -sf /ih/service/ih.uwsgi /etc/uwsgi/apps-available/ih.ini
RUN ln -sf /ih/service/ih.uwsgi /etc/uwsgi/apps-enabled/ih.ini
RUN service uwsgi restart
RUN ln -sf /ih/service/ih.nginx /etc/nginx/conf.d/ih.conf
RUN service nginx restart
WORKDIR /ih
EXPOSE 80
