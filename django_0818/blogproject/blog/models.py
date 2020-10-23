from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    # body의 20번째 글자 전까지만 보여줌
    def summary(self):
        return self.body[:20]