FROM python:3.9

ARG project_dir=/app

WORKDIR ${project_dir}

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

CMD ["/bin/bash", "-c", "flask run -h 0.0.0.0"]
