# Ultimative PHP

The final all-in-one migration gateway verifies administrator access,
recovery answers, a compatibility code, and a portable legacy profile.

## Local setup

Build and run the supplied source with Docker:

```sh
docker build -t ultimative-php -f deploy/Dockerfile .
docker run --rm -p 8080:8080 \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=1m \
  -e 'FLAG=FortID{redacted}' \
  ultimative-php
```

The service is available at `http://127.0.0.1:8080`.
