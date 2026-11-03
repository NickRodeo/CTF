FROM php:8.3-cli

WORKDIR /var/www/html

COPY deploy/challenge.ini /usr/local/etc/php/conf.d/challenge.ini
COPY --chmod=0555 deploy/entrypoint.sh /usr/local/bin/ultimative-php-entrypoint
COPY src/ /var/www/html/

RUN chown -R root:root /var/www/html \
    && chmod -R a-w /var/www/html \
    && ln -s /tmp/flag /flag

USER www-data
EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/ultimative-php-entrypoint"]
