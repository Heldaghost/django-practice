from datetime import datetime, timezone

from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.contrib.auth import login, logout
from photo_hosting.forms import *
# Create your views here.
from django.views.generic import ListView

from photo_hosting.models import *


# class HomeNews(ListView):
#     model = Posts
#     template_name = 'news/wall.html'
#     context_object_name = 'posts'
#     paginate_by = 3
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Главная'
#         context['mixin_prop'] = self.get_prop()
#         return context

def add_comment(request):
    if request.method == 'GET':
        Comments.objects.create(user_id=request.user.pk, post_id=request.GET['post_id'],
                                content=request.GET['comment'])
        return render(request, 'photo_hosting/comment_list.html',
                      context={'comments': Comments.objects.filter(post_id=request.GET['post_id'])})
    else:
        return HttpResponse("Request method is not a GET")


def view_modal(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = Posts.objects.get(pk=post_id)
        return render(request, 'photo_hosting/modal_part.html', {'post': post})

    else:
        return HttpResponse("Request method is not a GET")


def like_post(request):
    if request.method == 'GET':

        post_id = request.GET['post_id']
        if not Likes.objects.filter(user_id=request.user.pk, post_id=post_id):
            Likes.objects.create(user_id=request.user.pk, post_id=post_id)
        else:
            Likes.objects.get(user_id=request.user.pk, post_id=post_id).delete()

        return HttpResponse(Likes.objects.filter(post_id=post_id).count().__str__())

    else:
        return HttpResponse("Request method is not a GET")


def switch_data(request):
    if request.method == 'GET':
        # user = User.objects.get(pk=1)
        # user.userprofile.likes_set.get()
        post_id = request.GET['post_id']
        col_name = 'none'
        if post_id == 'cols':
            data = Collections.objects.filter(user_id=request.user.pk)
        elif post_id == 'posts':
            data = Posts.objects.filter(user_id=request.user.pk)
        elif post_id == 'likes':
            data = Posts.objects.filter(likes__user=request.user.pk)
        elif Collections.objects.get(pk=post_id):
            data = Posts.objects.filter(collection_id=Collections.objects.get(pk=post_id))
            col_name = Collections.objects.get(pk=post_id).title
            post_id = 'col'

        return render(request, 'photo_hosting/switch_part.html',
                      {'data': data, 'post_id': post_id, 'col_name': col_name})

    else:
        return HttpResponse("Request method is not a GET")


def edit_profile(request):
    obj = get_object_or_404(User, username=request.user.username)
    obj_prof = obj.userprofile
    if request.method == 'POST':
        form_us = EditUserForm(request.user, request.POST, request.FILES)
        form_prof = EditProfileForm(request.user, request.POST, request.FILES)
        if form_us.is_valid() & form_prof.is_valid():
            obj.username = form_us.cleaned_data.get('usrname')
            obj.first_name = form_us.cleaned_data.get('first_name')
            obj.last_name = form_us.cleaned_data.get('last_name')
            obj.email = form_us.cleaned_data.get('email')
            obj_prof.description = form_prof.cleaned_data.get('description')
            obj_prof.avatar = form_prof.cleaned_data.get('avatar')
            obj_prof.birth_date = form_prof.cleaned_data.get('birth_date')
            obj.save(force_update=True)
            obj_prof.save()

            return redirect('/')
    else:
        form_us = EditUserForm(request.user)
        form_prof = EditProfileForm(request.user)
    return render(request, 'photo_hosting/edit_profile.html',
                  {'form_us': form_us, 'form_prof': form_prof, 'title': f'User settings for {request.user.username}'})


def add_col(request):
    if request.method == 'POST':
        form = AddCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user.userprofile

            instance.save()
            form.save_m2m()

            return redirect('/')
    else:
        form = AddCollectionForm()
    return render(request, 'photo_hosting/add_collection.html', {'form': form, 'title': 'New collection'})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Succezss registration')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed')
    else:
        form = UserRegisterForm()
    return render(request, 'photo_hosting/register.html', context={'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'photo_hosting/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect(to='/')


def home_posts(request):
    cols = Collections.objects.all()
    posts = Posts.objects.order_by('-created_at')

    context = {'title': 'Wall', 'posts': posts, 'cols': cols}
    return render(request, 'photo_hosting/wall.html', context=context)


def user_profile(request, user_slug):
    user_info = UserProfile.objects.get(user__username=user_slug)
    likes_for_user = [item.likes_set.count() for item in user_info.posts_set.all()]
    if user_info.birth_date:
        age = ((datetime.now(timezone.utc) - user_info.birth_date).days / 365.25).__round__()
    else:
        age = None
    posts = Posts.objects.filter(user__user__username=user_slug)
    context = {'posts': posts, 'info': user_info, 'title': 'Profile', 'age': age, 'sum_likes': sum(likes_for_user)}
    return render(request, 'photo_hosting/profile.html', context=context)


def add_posts(request):
    if request.method == 'POST':
        form = PostsForm(request.user.pk, request.POST, request.FILES)
        tagslist = request.POST.get("tags")
        tagslist = [r for r in tagslist.split(',')]
        if form.is_valid():
            print(form.cleaned_data)
            instance = form.save(commit=False)
            instance.user_id = request.user.pk
            instance.slug = slugify(instance.title)
            instance.save()
            form.save_m2m()

            return redirect('/')
    else:
        form = PostsForm(user_id=request.user.pk)
    return render(request, 'photo_hosting/add_post.html', {'form': form, 'title': 'New post'})
