from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import login

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'board/post_list.html', {'posts': posts})
def get_client_ip(request):
    """비로그인 사용자의 IP 주소를 가져오는 함수"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 조회수 증가
    post.views += 1
    post.save()

    # 방문자 추적 (로그인한 사용자만)
    if request.user.is_authenticated:
        if not post.visitors.filter(id=request.user.id).exists():
            post.visitors.add(request.user)

    comments = post.comments.all()
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user  # 로그인한 사용자를 댓글 작성자로 설정
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'board/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 현재 로그인한 사용자를 작성자로 설정
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'board/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 작성자 변경 없이 현재 로그인한 사용자 유지
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'board/post_form.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')  # 회원가입 후 게시글 목록 페이지로 리디렉트
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})