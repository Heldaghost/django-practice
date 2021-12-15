from django.contrib import admin
from django.urls import path

from photo_hosting.views import *

urlpatterns = [
    path('', HomePosts.as_view(), name='home'),
    path('user/<slug:user_slug>', user_profile, name='profile'),
    path('add-page/', add_posts, name='add_page'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('add-col-page/', add_col, name='add_col_page'),
    path('edit-profile', edit_profile, name='edit_profile'),
    path('switch_data/', switch_data, name='switch_data'),
    path('like_post/', like_post, name='like_post'),
    path('view_modal/', view_modal, name='view_modal'),
    path('add_comment/', add_comment, name='add_comment'),
    path('edit_post/', edit_post, name='edit_post'),
    path('delete_post/', delete_post, name='delete_post'),
    path('search/', search, name='search'),
    path('edit_collection/', edit_collection, name='edit_collection'),
    path('delete_cols/', delete_col, name='delete_cols'),
    path('admin/', admin.site.urls, name='admin'),
    path('like_col/', like_col, name='like_col')

]
