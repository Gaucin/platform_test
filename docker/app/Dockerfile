FROM python:3.8.12-alpine3.14

ENV PYTHONUNBUFFERED 1

ARG APP=/app
ARG APP_USER=user
ARG SECRET_KEY
ARG STATIC_ROOT=/static
ARG MEDIA_ROOT=/media

RUN apk add --no-cache --virtual .build-deps build-base \
    linux-headers postgresql-dev
RUN apk add --no-cache libffi-dev jpeg-dev zlib-dev \
    zeromq-dev \
    openssl-dev \
    postgresql-client \
    postgresql-libs

RUN addgroup -S ${APP_USER} && adduser -S -G ${APP_USER} ${APP_USER}

ENV PATH="/home/${APP_USER}/.local/bin:${PATH}"
ENV SECRET_KEY ${SECRET_KEY}
ENV STATIC_ROOT ${STATIC_ROOT}
ENV MEDIA_ROOT ${MEDIA_ROOT}

WORKDIR ${APP}

COPY . ${APP}

RUN mkdir -p ${STATIC_ROOT} ${MEDIA_ROOT}

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

RUN chown -R ${APP_USER}:${APP_USER} ${APP} ${STATIC_ROOT} ${MEDIA_ROOT}

RUN apk --purge del .build-deps

# USER ${APP_USER}

ENTRYPOINT [ "/app/docker/app/docker-entrypoint.sh" ]

CMD ["runserver"]
