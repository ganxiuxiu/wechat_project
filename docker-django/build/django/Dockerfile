#定义该镜像使用的基础镜像为
#从仓库拉取 带有 python 的 Linux 环境
FROM python:3.6.7-slim-jessie

LABEL version="v0.0.2"
# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1
COPY sources.list /etc/apt
WORKDIR /usr/src/app
# 添加这两行
#RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
#RUN apt-get clean
RUN apt-get update \
   #&& apt-get install -y --no-install-recommends mysql-client default-libmysqlclient-dev \
   #&& mkdir /code \
    && apt-get install -y --no-install-recommends libxml2-dev build-essential

ADD requirements.txt ./
RUN pip uninstall uwsgi \
    && pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
# ADD . /code/


#开放的端口
EXPOSE 8000