FROM python:3.5-alpine
LABEL maintainer="jcito@csail.mit.edu"
ENV ver 1
RUN pip install praw==4.4.0

VOLUME /home
