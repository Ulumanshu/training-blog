from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, DeleteView, CreateView, UpdateView)
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset


class PostListView(ListView):
    model = Post
    template_name = 'blog/base.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

    def get(self, request):       
        visits_count = request.session.get('visits_count', 0)
        request.session['visits_count'] = visits_count + 1
        # Render the HTML template passing data in the context.            
        if self.request.user.is_authenticated:
            posts = Post.objects.all().order_by('-published_date')
        else:
            posts = Post.objects.filter(public=True).order_by('-published_date')
        context = {
            'visits_count': visits_count,
            'posts': posts,
        }    
        return render(request, 'blog/post_list.html', context=context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['public', 'title', 'text']
    template_name = 'blog/post_edit.html'
    login_url = '/login'

    def post(self, request):
        if request.method == "POST":
            visits_count = request.session.get('visits_count', 0)
            request.session['visits_count'] = visits_count + 1
            form = PostForm(data=request.POST, user=request.user)
            if form.is_valid():                
                form.save()
                if self.request.user.is_authenticated:
                    posts = Post.objects.all().order_by('-published_date')
                else:
                    posts = Post.objects.filter(public=True).order_by('-published_date')
                context = {
                    'visits_count': visits_count,
                    'posts': posts,
                }    
                return render(request, 'blog/post_list.html', context=context)
            
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blog/post_edit.html'
    login_url = '/login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

#      -- using class based views instead of function based --
#
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

# def post_new(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})    

# @login_required (login_url='/login')
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             if request.user.is_authenticated:
#             	post.author = request.user	
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('/', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})    


# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})
