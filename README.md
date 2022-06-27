## Stacks
- Python3
- Django
- DRF
- dj-rest-auth, django-allauth
- MySql

<br>
<br>


## Project Structure
[API Documentation](https://documenter.getpostman.com/view/14112304/Uz5AsKJu)

```
.
├── Dockerfile
├── Dockerfile-dev
├── README.md
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── common
│   └── permissions.py
├── configs
│   ├── asgi.py
│   ├── base.py
│   ├── config.py
│   ├── dev.py
│   ├── local.py
│   ├── prod.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements
│   ├── requirements-dev.txt
│   └── requirements.txt
├── tests
│   ├── test_comment.py
│   ├── test_post.py
│   └── test_user.py
└── users
    ├── adapter.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    ├── models.py
    ├── serializers.py
    ├── urls.py
    └── views.py

```
- `api`: 블로그 관련 API 기능 코드는 전부 이 api 모듈에 포함 되어 있습니다.
- `users`: 로그인, 회원가입 등 유저와 관련된 API 기능 코드를 포함 힙니다.
- `tests`: Unit test 파일들을 담고 있는 모듈입니다.
- `config.py`: 서버와 API를 실행시키기 위한 설정 값이 정의 되어 있는 파일입니다.

<br>
<br>

## Local Setting
1. 가상환경은 venv를 사용하였습니다.
2. 가상환경 실행 후 requirements.txt가 있는 위치로 이동해 다음 명령어를 실행합니다.
	```
	pip install -r requirements
	```
3. config_sample.py의 세부 내용을 수정하고 config.py로 변경합니다.

4. local에 mysql을 설치하고 다음 명령어를 통해 root 계정으로 DB를 생성합니다.
    ```
    create database blog character set utf8mb4 collate utf8mb4_general_ci;
    ```

5. managy.py가 있는 위치로 이동 후 다음 명령어로 DB를 생성합니다.
    ```
    python managy.py makemigrations
    python managy.py migrate
    ```

6. managy.py가 있는 위치로 이동 후 서버를 킵니다.
    ```
    python managy.py runserver --settings=configs.local
    ```