FROM python:3.8
WORKDIR /home

RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -yq libgl1-mesa-glx \
&& apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

COPY . .

EXPOSE 5005

CMD ["python", "run.py"]