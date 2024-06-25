from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend_view, name='recommend'),
    path('school/<int:school_id>/', views.school_detail_view, name='school_detail'),
]
