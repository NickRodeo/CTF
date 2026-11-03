#!/bin/sh
set -eu

: "${FLAG:?FLAG is required}"

umask 077
printf '%s' "$FLAG" > /tmp/flag
chmod 0400 /tmp/flag
unset FLAG

export FLAG_FILE=/tmp/flag
exec python3 /challenge/src/app.py
