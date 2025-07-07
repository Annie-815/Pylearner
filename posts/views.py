from django.shortcuts import render,redirect
from posts.models import Post
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'posts/post_list.html', { 'posts': posts})
def post_page(request, slug):    
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', { 'post': post})
@login_required(login_url='users:login')
def create_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:list')  
    else:
        form = forms.CreatePost()
    return render(request, 'posts/create_post.html', { 'form': form})