FROM python:3.7

ADD . /code
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sanic 
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pycryptodome

EXPOSE 8001

WORKDIR /code

CMD ["python", "main.py"]
