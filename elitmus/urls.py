"""elitmus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.index,name='index'),
    path('',views.index2,name='index2'),
    path('login/',views.login_html,name='login_html'),
    path('signup/',views.signup_html,name='signup_html'),
    path('sec/',views.signup,name='form'),
    path('secs/',views.my_login,name='login'),
    path('rest/', include('api.urls')),
    path('fong/',views.fokati,name='fokati'),
    path('logout/',views.my_logout,name='logout'),
    path('add_data/',views.add_data,name='add_data'),
    
]
