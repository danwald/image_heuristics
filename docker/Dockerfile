FROM        phusion/baseimage:0.9.16

MAINTAINER Danny Crasto <danwald79@gmail.com>

WORKDIR /opt
RUN apt-get update && apt-get install -y build-essential python-dev python-setuptools\
                      liblapack-dev liblapack3gf libgtk2.0-dev gfortran libblas3gf\
                      libopencv-dev libopencv-highgui-dev libcvaux-dev python-opencv python-pip\
                      git-core libc-dev nginx vim libtiff4-dev libjpeg8-dev zlib1g-dev\
                      libfreetype6-dev liblcms1-dev libwebp-dev byobu

RUN git clone https://github.com/danwald/image_heuristics.git ih -b phusioning &&\
        pip install -r /opt/ih/requirements/requirements.txt &&\
        mkdir -p /etc/service/ih && mkdir -p /etc/service/nginx &&\
        cp /opt/ih/docker/services/uwsgi.run /etc/service/ih/run;\
        cp /opt/ih/docker/services/nginx.run /etc/service/nginx/run;\
        chmod +x /etc/service/ih/run;\
        chmod +x /etc/service/nginx/run;\
        rm /etc/nginx/sites-enabled/default

EXPOSE 80

CMD ["/sbin/my_init"]
