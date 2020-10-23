from django.db import models
from django.conf import settings    # 좋아요 기능 위해 추가 (settings.AUTH_USER_MODEL)

# Create your models here.

# 모델을 정의하는 코드
# Post는 모델 이름을, models는 장고 모델임을 의미
class Post(models.Model): 
    title = models.CharField(max_length=200)
    # 이미지 추가
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    # 좋아요 기능 위해 추가 - M:N 관계
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')


    def __str__(self):
        return self.title

    # body의 20번째 글자 전까지만 보여줌
    def summary(self):
        return self.body[:20]

# 게시글에 댓글 작성, 1:N 구조
class Comment(models.Model):
    post = models.ForeignKey('myblog.Post', on_delete = models.CASCADE)
    # models.ForeignKey(): 외래키 설정, 게시물과 댓글 연결
    # 첫 번째 인자로 외래키 연결 테이블, 
    # 두 번째 인자로 게시물 삭제 시 어떻게 처리할지 옵션(CASCADE/PROTECT/SET_NULL)
    content = models.TextField()

    def __str__(self):
        return self.content