# 从仓库拉取 带有 python 的 Linux 环境
FROM python:3.6.8

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 添加这两行
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev -y

# 创建 code 文件夹并将其设置为工作目录
RUN mkdir /code
WORKDIR /code
# 更新 pip
#RUN pip install pip -U -i https://mirrors.aliyun.com/pypi/simple/
# 将 requirements.txt 复制到容器的 code 目录
ADD requirements.txt /code/
# 安装库 并使用阿里源安装
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
# 将当前目录复制到容器的 code 目录
ADD . /code/