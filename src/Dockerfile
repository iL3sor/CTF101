FROM php:7-apache

RUN apt update
RUN apt-get install -y zlib1g-dev libpng-dev libjpeg-dev
RUN docker-php-ext-install mysqli pdo pdo_mysql && docker-php-ext-enable mysqli pdo pdo_mysql
RUN docker-php-ext-configure gd --with-jpeg && \
    docker-php-ext-install gd

WORKDIR /var/www/html

COPY . .

RUN chown -R www-data:www-data /var/www