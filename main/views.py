from django.shortcuts import render, redirect
from django.db.models import Max
from .models import User, Post
from .forms import UserForm, PostForm


def index(request):
    users_with_recent_posts = User.objects.annotate(
        most_recent_post=Max('post__created_at')
    ).order_by('-most_recent_post')
    users_and_posts = [(user, user.post_set.order_by('-created_at').first()) for user in users_with_recent_posts]

    if 'query' in request.GET:
        query = request.GET.get('query')
        user = User.objects.filter(username=query).first()
        users = User.objects.filter(username__icontains=query)
        if user:
            return redirect('profile', username=user.username)
        else:
            users = User.objects.filter(username__icontains=query)
            return render(request, 'index.html', {'users_and_posts': users_and_posts, 'users': users})

    return render(request, 'index.html', {'users_and_posts': users_and_posts})

def remark(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # if User.objects.filter(username = username).first():
            #     form.add_error(form.username, "This username is already taken")
            fullname = form.cleaned_data['fullname']
            age = form.cleaned_data['age']
            identifier = form.cleaned_data['identifier']
            user = User(username=username, fullname=fullname, age=age, identifier=identifier)
            user.save()
            return redirect('profile', username=username)
    else:
        form = UserForm()
    return render(request, 'remark.html', {'form': form})

def profile(request, username):
    user = User.objects.filter(username=username).first()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            post = Post(user=user, content=content)
            post.save()
            return redirect('profile', username=username)
    else:
        form = PostForm()
    return render(request, 'pf.html', {'user': user, 'posts': Post.objects.filter(user=user), 'form': form })

