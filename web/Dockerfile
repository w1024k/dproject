FROM centos:7.4.1708
MAINTAINER yang.wang <w1024k@163.com>

ENV DJANGO_SETTINGS_MODULE wangyang.settings_aliyun
ENV C_FORCE_ROOT true

RUN yum -y install epel-release && \
    yum -y install python-pip && \
    yum -y install mysql-devel && \
    yum -y install gcc libffi-devel python-devel openssl-devel && \
    mkdir /root/.pip

#python 依赖包
COPY ./config/pip.conf /root/.pip/pip.conf
COPY ./requirement.txt /root/
COPY ./start.sh /root/start.sh
COPY ./code/dproject /root/dproject


RUN pip install -r /root/requirement.txt && \
    mkdir /var/log/django && \
    mkdir /var/log/gunicorn && \
    touch /var/log/django/error.log && \
    touch /var/log/gunicorn/error.log  && \
    mkdir -p /media/www/static && \
    mkdir -p /media/www/tmp && \
    mkdir -p /media/www/source

VOLUME /root/dproject/
VOLUME /var/log/
VOLUME /media/www/

EXPOSE 8000

WORKDIR /root/dproject/wangyang/
CMD ["/bin/sh","/root/start.sh"]