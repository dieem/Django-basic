from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    posts = Post.objects  
    # Post.objects 는 admin 페이지에서 확인했던 blog 안의 data
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')
    posts_num = paginator.get_page(page) # 출력 원하는 page

    return render(request, 'home.html', {'blogs':posts, 'posts':posts_num})
    # return render(request, 'home.html', {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()  # 입력한 시간 자동으로 입력
    post.save()
    return redirect('/' + str(post.id))

def delete(request, post_id):
    post_num = get_object_or_404(Post, pk=post_id)
    post_num.delete()
    return redirect('/')

def new(request):
    return render(request, 'new.html')