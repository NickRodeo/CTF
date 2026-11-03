#!/bin/sh
set -eu

case "${FLAG:-}" in
  FortID\{*\}) ;;
  *)
    echo "FLAG must use the FortID{...} format" >&2
    exit 1
    ;;
esac

umask 077
printf '%s\n' "$FLAG" > /tmp/flag
chmod 0400 /tmp/flag
unset FLAG

exec php -S 0.0.0.0:8080 -t /var/www/html

