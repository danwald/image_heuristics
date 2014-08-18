FROM ubuntu:14.04
MAINTAINER Danny Crasto <danwald79@gmail.com>

RUN apt-get update
RUN apt-get install -y build-essential python-dev python-setuptools \
                       liblapack-dev liblapack3gf libgtk2.0-dev gfortran libblas3gf \
                       liblapack3gf libopencv-dev libopencv-highgui-dev libcvaux-dev \
                       python-opencv python-setuptools python-pip zlib1g-dev git-core \
                       libc-dev nginx uwsgi vim libtiff4-dev libjpeg8-dev zlib1g-dev \
                       libfreetype6-dev liblcms1-dev libwebp-dev

RUN git clone https://github.com/danwald/image_heuristics.git -o /ih
RUN cd  ih
RUN pip install -r requirements/dev.txt
RUN ln -s service/ih.uwsgi /etc/uwsgi/apps-available/ih.ini
RUN sudo service uwsgi restart
RUN ln -s service/ih.nginx /etc/nginx/conf.d/ih.conf
RUN sudo service nginx restart
EXPOSE 80
