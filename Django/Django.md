# vs 라이브러리

건축에 비유하면 구조를 만드는 골조가 *프레임워크*라면 그 외 자재들이 *라이브러리*라고 볼 수 있다.

# 웹 프레임워크

웹 개발에 필요한 기본적인 구조와 코드(클래스, 함수 등)가 만들어져 있음

- 제공 프레임워크 : URL파싱, 응답 생성, 요청 파싱, 세션 관리, 데이터베이스 연동, 관리자 페이지...
- 개발 영역 : 비즈니스 로직, 데이터 영역...

# 가상환경 설정

1. 파일 생성

   ```
   (terminal)
   virtualenv (파일명)
   ```

2. 활성화

   ```
   (terminal)
   source (파일명)/bin/activate
   ```

   -> 터미널 상에서 _(파일명) kangshinhyeon@MacBook-Pro-3_ 으로 바뀜

3. django 설치

   ```
   (terminal)
   pip3 install django
   ```

# project 생성

```
(terminal)
django-admin startproject (project 명)
```

# app 생성

```
(terminal)
cd (project)
django-admin startapp (app 명)
```

app 생성 이후 생성된 파일 내부에 *templates*라는 이름의 폴더를 만들어줘야 함

# app -> project에 등록

project를 생성할 때 project명과 같은 이름으로 하위에 폴더 하나가 생성되는데 그파일 안에 settings.py에 들어가서
내가 생성한 app의 이름을 *INSTALLED_APPS*에 등록해줘야 함

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',
    'fc_user'
]
```

# (db) model 작성

app 내의 models.py 파일

# model 생성

```
(terminal)
python3 manage.py makemigrations
```

-> migrations 파일에 initial.py가 생성이 되는데, 필드값을 읽어 db 생성을 위한 설정값들이 나옴

# db 생성

```
(terminal)
python3 manage.py migrate
```

-> 이전에 settings에 등록해 둔 app들이 사용할 table을 자동으로 생성

# project 실행 (서버 실행)

```
(terminal)
python3 manage.py runserver
```

관리자 페이지로 이동하고 싶을 경우
제공된 주소 뒤에 /admin을 붙이면 됨
ex) http://127.0.0.1:8000/admin

서버 종료 : ctrl+c

# admin id & password 생성

```
(terminal)
python3 manage.py createsuperuser
```

# admin에 app추가

app의 admin.py 파일

# 회원가입 페이지 만들기

1. templates 파일에 회원가입 페이지를 띄울 register.html를 만들고 작성
   기본적인 틀은 bootstrap을 이용하였음 (프론트엔드 오픈 소스 툴킷)

2. template과 view 연결
   view.py 작성

3. url 설정 (http://127.0.0.1:8000/fc_user/register)
   project -> url.py 작성 (app자체에서 url을 관리할 수 있게)  
   app -> url.py 생성 후 작성 (register url 추가)
