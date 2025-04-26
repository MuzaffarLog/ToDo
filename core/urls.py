from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import UpdateView

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/update/', UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
]


urlpatterns += [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]