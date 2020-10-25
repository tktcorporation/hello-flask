FROM python:3.9

RUN pip install Flask

WORKDIR /app

ADD . .

# ENTRYPOINT [ "/bin/bash" ]

CMD ["/bin/bash", "-c", "flask run -h 0.0.0.0"]
