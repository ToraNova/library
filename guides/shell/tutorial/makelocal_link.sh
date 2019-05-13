#!/bin/bash

rm http_apache2.link -f
echo creating link for HTTP apache2 targeted on /var/www
ln -s /var/www http_apache2.link

rm http_apache2conf.link -f
echo creating link for HTTP apache2 config targeted on /etc/apache2
ln -s /etc/apache2 http_apache2conf.link
