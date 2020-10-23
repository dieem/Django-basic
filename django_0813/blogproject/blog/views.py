from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})
    
    # posts에 담긴 데이터들을 'posts'라는 이름으로 넘겨준다
    # Queryset: 모델로부터 전달받은 객체 목록
    # Method: 쿼리셋을 처리해주는 방법

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()  # 입력한 시간이 자동으로 넘어감
    post.save()
    return redirect('/' + str(post.id)) # redirect는 요청이 들어오면 저쪽 url로 보내줌
