"""config URL Configuration

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
from django.urls import path

from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('db1', views.db1, name='db1'),
    path('AgeChart', views.AgeChart, name='AgeChart'),
    path('tp', views.tp, name='tp'),
    path('ScatterPlot', views.ScatterPlot, name='ScatterPlot'),
    path('db5', views.db5, name='db5'),
    path('matrix', views.matrix, name='matrix'),
    path('geo', views.geo, name='geo'),
    path('pr', views.wspr, name='pr'),
    path('chart', views.chart, name='chart'),
    path('ages', views.ages, name='ages'),
    path('chs1', views.chs1, name='chs1'),
    path('sp', views.sp, name='sp'),
    path('tables', views.tables, name='tables')



]