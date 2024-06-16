from django.contrib import admin
from django.urls import path
from enroll import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('send/', views.sendmail, name="sendmail"),
    path('', views.home, name="home"),
]
