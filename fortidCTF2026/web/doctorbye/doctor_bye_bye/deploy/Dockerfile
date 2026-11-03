FROM python:3.12-slim@sha256:dddfd7e07f9d15aeeca61529320492139d21cac7f0070c00609243e51e4e0016

RUN useradd --create-home --uid 1000 challenge
WORKDIR /challenge

COPY src/ /challenge/src/
COPY --chmod=0555 deploy/entrypoint.sh /usr/local/bin/doctor-bye-bye-entrypoint
RUN chown -R root:root /challenge \
    && chmod -R a-w /challenge

USER challenge
EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/doctor-bye-bye-entrypoint"]
