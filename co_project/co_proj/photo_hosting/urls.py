from django.urls import path

from photo_hosting.views import *

urlpatterns = [
    path('', home_posts, name='home'),
    path('user/<slug:user_slug>', user_profile, name='profile'),
    path('add-page/', add_posts, name='add_page'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('add-col-page/', add_col, name='add_col_page'),
    path('edit-profile', edit_profile, name='edit_profile'),
    path('switch_data/', switch_data, name='switch_data'),
    path('like_post/', like_post, name='like_post'),
    path('view_modal/', view_modal, name='view_modal')
]
