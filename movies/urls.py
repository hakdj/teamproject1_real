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
    ## 재현님
    path('AgeChart', views.AgeChart, name='AgeChart'),
    path('ages', views.ages, name='ages'),

    path('ScatterPlot', views.ScatterPlot, name='ScatterPlot'),
    path('sp', views.sp, name='sp'),
    # 추가 기능 구현 0722
    path('imrate', views.imrate, name='imrate'),
    path('imdbrate', views.imdbrate, name='imdbrate'),

    ## 현수님
    path('tp', views.tp, name='tp'),
    path('chs1', views.chs1, name='chs1'),
    path('tablechs', views.tablechs, name='tablechs'),
    path('tablechs2', views.tablechs2, name='tablechs2'),

    ## 운기님
    path('matrix', views.matrix, name='matrix'),

    ## 청하님
    path('tp1', views.tp1, name='tp1'),
    path('TP1', views.TP1, name='TP1'),
    path('tp32', views.tp32, name='tp32'),
    path('TP32', views.TP32, name='TP32'),


    path('geo', views.geo, name='geo'),
    path('pr', views.wspr, name='pr'),
    path('chart', views.chart, name='chart'),

]