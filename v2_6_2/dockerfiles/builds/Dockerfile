FROM ubuntu:16.04

LABEL maintainer="info@optimum-web.com"
ENV MODX_VERSION 2.6.2

RUN groupadd -r -g 2000 modx; useradd -r -u 2000 -g 2000 -m -c "app account" -d /home/modx -s /bin/bash modx

RUN apt-get update -y -qq ; apt-get install -y -qq software-properties-common; \
    LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php -y; apt-get update -y -qq; \
    apt-get install -y -qq nginx sudo supervisor cron unzip \
    php7.1 php7.1-fpm php7.1-mysql  php7.1-cli php7.1-cgi php7.1-gd php7.1-zip php7.1-xml  php7.1-mcrypt php7.1-curl;  \
    rm -rf /etc/nginx/sites-available/default; rm -rf /etc/nginx/sites-enabled/default;  mkdir /run/php; \
    mkdir -p /opt/letsencrypt

COPY ./archives/modx-${MODX_VERSION}-pl.zip /usr/src
RUN unzip -qq /usr/src/modx-${MODX_VERSION}-pl.zip -d /usr/src
RUN ls -la /usr/src
ADD ./configs/php/fpm/php.ini /etc/php/7.1/fpm/php.ini
ADD ./configs/php/www.conf /etc/php/7.1/fpm/pool.d/www.conf
ADD ./configs/supervisord/modx.conf /etc/supervisor/conf.d/modx.conf
ADD ./scripts/letsencrypt-auto /opt/letsencrypt/letsencrypt-auto

RUN chmod +x /opt/letsencrypt/letsencrypt-auto; /opt/letsencrypt/letsencrypt-auto  --os-packages-only --install-only --non-interactive;
RUN apt-get clean; apt-get autoclean; apt-get autoremove -y -qq;  apt-get clean -y -qq;
