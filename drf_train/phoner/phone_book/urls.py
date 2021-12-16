from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns

from phone_book import views

router = DefaultRouter()
router.register(r'phonenotes', views.NotesViewSet)
router.register(r'user', views.UserViewSet)

schema_view = get_schema_view(title='Train API')

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),

]


