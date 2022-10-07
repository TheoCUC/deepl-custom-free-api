FROM selenium/standalone-chrome
COPY ./code /code
RUN sudo apt-get update &&\
		sudo apt-get install -y python3 python3-pip &&\
		pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple &&\
		pip3 install -r /code/requirements.txt
CMD ["python3", "/code/main.py"]
