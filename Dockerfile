FROM ubuntu:20.04

RUN apt update  && apt install -y python3 && apt install -y pip

WORKDIR /usr/src/app 

## Install packages
COPY requirements.txt ./ 
RUN pip install -r requirements.txt

## Copy all src files
COPY . . 

## Run the application on the port 8080
EXPOSE 8000   

# gunicorn 사용해서 서버를 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog.wsgi:application"]