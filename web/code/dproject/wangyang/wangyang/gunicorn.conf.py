# coding: utf-8

worker = 2
bind = '0.0.0.0:8000'
accesslog = "/var/log/gunicorn/access.log"
access_log_format = '%(p)s %(h)s - %(t)s [%(D)s] "%(r)s" %(s)s %(b)s'
errorlog = "/var/log/gunicorn/error.log"
loglevel = "info"
worker_class = "gevent"
max_requests = 500
keepalive = 600
timeout = 10
