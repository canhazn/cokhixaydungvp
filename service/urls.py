from . import views
from django.urls import path

urlpatterns = [
    path('', views.serviceList, name='service_list'),
    # path('<slug:slug>/', views.postDetail, name='post_detail'),
    # path('tag/<slug:slug>/', views.tagDetail, name='tag_detail'),
]