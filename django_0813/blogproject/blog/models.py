from django.db import models

# Create your models here.

# 모델을 정의하는 코드
# Post는 모델 이름을, models는 장고 모델임을 의미
class Post(models.Model): 
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
