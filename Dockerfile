FROM vulnerables/web-dvwa:latest

COPY ./.env .env
COPY ./setup-env.sh setup-env.sh
RUN chmod +x /setup-env.sh
RUN /setup-env.sh