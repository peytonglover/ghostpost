"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from homepage.views import *

urlpatterns = [
    path('', index, name='index'),
    path('upvotes/<int:post_id>/', upvoteview),
    path('downvotes/<int:post_id>/', downvoteview),
    path('sortbyvotes/', sortbyvotes),
    path('addpost/', addpost, name='addpost'),
    path('boasts/', boast, name='boast'),
    path('roasts/', roast, name='roast'),
    path('admin/', admin.site.urls),
]
