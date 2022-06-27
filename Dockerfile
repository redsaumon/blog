FROM python:3.8

WORKDIR /app/

# Install Production Depedencies First 
COPY requirements/ /app/requirements/
RUN pip install  --upgrade pip --no-cache-dir -r requirements/requirements-dev.txt

# Bundle app source
COPY . /app/


## Run the application on the port 8080
EXPOSE 8000   

# gunicorn 사용해서 서버를 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "configs.wsgi:application"]