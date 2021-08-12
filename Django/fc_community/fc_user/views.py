from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fcuser
from django.contrib.auth.hashers import make_password, check_password


def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)

    return HttpResponse('Home')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # 아이디, 패스워드 입력
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        else:
            # Fcuser에서 username과 같을 경우 가져옴
            fcuser = Fcuser.objects.get(username=username)

            # password와 fc_user에서 가져온 password가 같을 경우 -> 로그인 처리
            if check_password(password, fcuser.password):
                request.session['user'] = fcuser.id
                return redirect('/')  # 세션 완료 후 홈으로 이동
            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'

        return render(request, 'login.html', res_data)


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


def register(request):
    # url을 통해 웹사이트에 들어와 요청하는 경우
    if request.method == 'GET':
        return render(request, 'register.html')  # 다시 register.html 요청
    # 회원가입 등록 버튼을 눌러 요청하는 경우
    elif request.method == 'POST':
        username = request.POST.get('username', None)  # for -> input의 name
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)

        res_data = {}

        # 예외처리
        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fc_user = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )

            fc_user.save()

        return render(request, 'register.html', res_data)
