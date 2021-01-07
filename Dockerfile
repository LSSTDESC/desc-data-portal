FROM ubuntu:latest
RUN apt-get update --quiet -y && \
    apt-get install -y python3-flask python3-pip
WORKDIR /app
COPY web /app
RUN pip3 install -r requirements.txt && \
    chmod o+rw portal/data/app.db

EXPOSE 5000

#ENV FLASK_ENV development
ENV FLASK_APP portal/__init__.py
#ENTRYPOINT ["flask"]
CMD ["flask", "run", "--host=0.0.0.0"]
RUN chmod +x /app/docker-entrypoint.sh
ENTRYPOINT ["/app/docker-entrypoint.sh"]


