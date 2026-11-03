# Doctor Bye Bye

Dr. Bye Bye has retired from St. Codd's Hospital.

The hospital insists that retired records can never be displayed. Can you
recover Dr. Bye Bye's private farewell note anyway?

## Local setup

Build and run the supplied source with Docker:

```bash
docker build -t doctor-bye-bye -f deploy/Dockerfile .
docker run --rm -p 8080:8080 \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=8m \
  -e 'FLAG=FortID{redacted}' \
  doctor-bye-bye
```

The service is available at `http://127.0.0.1:8080`.
