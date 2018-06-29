FROM python:3.6.5-jessie

RUN mkdir md5_stream
WORKDIR md5_stream

COPY requirements.txt /md5_stream/

RUN pip install --upgrade pip -i http://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
RUN pip install -U -r requirements.txt -i http://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn

ENV FLASK_DEBUG=1
ENV FLASK_APP=/md5_stream/app.py
COPY app.py /md5_stream/
CMD flask run
