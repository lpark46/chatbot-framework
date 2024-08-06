from django.contrib import admin
from django.urls import path
from django.urls import re_path
from kakao_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^keyboard/?$', views.keyboard), # 예시 1
    re_path(r'^message', views.message), # 예시 2
    path('test-db/', views.test_db_connection),
]
