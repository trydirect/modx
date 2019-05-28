#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import docker
import requests

client = docker.from_env()

# Testing Modx build

time.sleep(20)  # we expect all containers are up and running in 20 secs

for c in client.containers.list():
    print("{}: {}" .format(c.name, c.status))
    if 'running' not in c.status:
        print(c.logs())

# # NGINX
nginx = client.containers.get('modx')
nginx_cfg = nginx.exec_run("/usr/sbin/nginx -T")
assert nginx.status == 'running'
print(nginx_cfg.output.decode())
assert 'server_name _;' in nginx_cfg.output.decode()
assert "error_log /proc/self/fd/2" in nginx_cfg.output.decode()
assert "location = /.well-known/acme-challenge/" in nginx_cfg.output.decode()
assert 'HTTP/1.1" 500' not in nginx.logs()


db = client.containers.get('modxdb')
assert db.status == 'running'
cnf = db.exec_run("/usr/sbin/mysqld --verbose  --help")
print(cnf.output.decode())
db_log = db.logs()
assert "mysqld: ready for connections" in db_log.decode()


# PHP-FPM
php = client.containers.get('modx')
print(php.logs())
assert php.status == 'running'
php_conf = php.exec_run("php-fpm7.1 -t")
print(php_conf.output.decode())
php_proc = php.exec_run("sh -c 'ps aux |grep php-fpm'")
# print(php_proc.output.decode())
assert 'configuration file /etc/php/7.1/fpm/php-fpm.conf test is successful' in php_conf.output.decode()
assert 'php-fpm: master process (/etc/php/7.1/fpm/php-fpm.conf)' in php_proc.output.decode()
assert 'php-fpm: pool www' in php_proc.output.decode()
assert 'modx' in php_proc.output.decode()

# check redirect to web installer
response = requests.get('http://localhost/setup')
assert "Loading..." in response.text

