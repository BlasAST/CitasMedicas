FROM python:3.13.1

RUN apt-get update \
&& pip install flask \
&& pip install flask_session \
&& pip install mysql-connector-python

WORKDIR /app
EXPOSE 5000
CMD [ "python","app.py" ]