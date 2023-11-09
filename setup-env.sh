#!/usr/bin/env sh

# setup env variables
. /.env

# config for 'File Inclusion'
sed -i "s/allow_url_include = Off/allow_url_include = On/" /etc/php/7.0/apache2/php.ini

# config for 'Insecure CAPTCHA'
sed -i "0,/'';/{s/'';/'$CAPTCHA_PUBLIC';/}" /var/www/html/config/config.inc.php
sed -i "0,/'';/{s/'';/'$CAPTCHA_PRIVATE';/}" /var/www/html/config/config.inc.php
