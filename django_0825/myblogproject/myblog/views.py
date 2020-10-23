from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from faker import Faker
# from .forms import PostForm
from .form import PostForm

# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})
    
    # posts에 담긴 데이터들을 'posts'라는 이름으로 넘겨준다
    # Queryset: 모델로부터 전달받은 객체 목록
    # Method: 쿼리셋을 처리해주는 방법

def create10(request):
    ifake = Faker()
    for i in range(10):
        post = Post()
        post.title = ifake.name()
        post.body = ifake.sentence()
        post.pub_date = timezone.datetime.now()
        post.save()
    return redirect('/')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

# def new(request):
#     # 새로운 폼 추가
#     form = PostForm()
#     return render(request, 'new.html', {'form': form})

def new(request):
    # POST는 글 "등록" 의미
    if request.method == "POST":
        # 작성된 데이터를 PostForm으로 넘겨주기 위함
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():   # 값들이 올바른지 확인
            post = form.save(commit=False)   # 바로 Post 모델에 저장 X
            post.pub_date = timezone.now()   # 작성 날짜, 시간 추가
            post.save()
            return redirect('/' + str(post.id))
    else:
        form = PostForm()
        return render(request, 'new.html', {'form': form})

def edit(request, post_id):
    # 현재 게시물 정보 받아오기
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)   # instance=post 수정할 모델의 객체 정보
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/' + str(post.id))
    else:
        form = PostForm(instance=post)
    return render(request, 'new.html', {'form': form})

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('/')

def comments_create(request, post_id):
    #댓글을 달 게시물에 대한 정보 가져오기
    post = Post.objects.get(pk=post_id)
    #form 태그에서 넘어온 댓글 내용 가져오기
    content = request.POST.get('content')
 
    #댓글 생성 및 저장 
    comment = Comment(post=post, content=content)
    comment.save()
    
    #댓글 생성후, 디테일 페이지로 redirect시킴
    return redirect('/' + str(post.id))

def comments_delete(request, post_id, comment_id):   # comment delete에는 게시글 정보와 댓글의 정보 둘 다 필요
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    
    return redirect('/'+str(post_id))

def comments_update(request, post_id, comment_id):
    # post와 comment 정보 가져오기
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()   # 수정된 내용 저장
        return redirect('/'+str(post_id))
    
    else:
        return render(request, 'comments_update.html', {'post':post, 'comment':comment})

# 좋아요 기능 함수
def like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)   # 리스트에서 유저 제거, 좋아요 기능 비활성화
    else:
        post.like_users.add(request.user)   # 리스트에 유저 추가, 좋아요 기능 활성화
    
    return redirect('/' + str(post.id))