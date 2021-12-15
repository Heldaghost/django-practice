from django.conf.urls import url
from django.urls import path

from phone_book import views

urlpatterns = [
    path('notes/', views.phone_notes_list),
    path('notes/<int:pk>', views.note_detail),
]
