FROM python:3
USER root

RUN apt-get update
RUN apt-get install -y vim less
RUN apt-get install -y zsh less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# dash
RUN pip install dash==1.14.0
RUN pip install pandas

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

EXPOSE 8001
CMD ["bash"]
