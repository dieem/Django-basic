# forms, Post 모델 import
from django import forms
from .models import Post

# PostForm: 만들 폼 이름
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # 폼 필드
        fields = ('title', 'body', 'image')