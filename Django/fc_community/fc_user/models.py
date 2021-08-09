from django.db import models


class Fcuser(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    useremail = models.CharField(max_length=128,
                                 verbose_name='사용자 이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    # list 객체가 list up -> 기존 Fcuser object (1)이라 나왔던 이름을 보기 좋게 username으로 변경
    def __str__(self) -> str:
        return self.username

    class Meta:  # database에 tabel명 지정
        db_table = 'fcuser'
        # 모델 보여줄 때 확인하기 좋게 이름(verbose_name) 따로 지정
        verbose_name = '사용자'  # django는 기본적으로 모델을 보여줄때 복수형으로 보여줌 -> 사용자s
        # 복수형 s 제거
        verbose_name_plural = '사용자'
