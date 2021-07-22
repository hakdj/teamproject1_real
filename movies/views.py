import json

from django.http import HttpResponse
from django.shortcuts import render

from analysis.sjh import MyAnalysis
from analysis.chs import CHS
from analysis.rch import RCH
from analysis.cwk import CorMatrix


## 페이지 메인 세션
def index(request):
    return render(request, 'index.html')


# -----------------------------------------------------------------------------#
## 재현님 코드 구현
def AgeChart(request):
    context = {
        'section': 'AgeChart.html'
    }
    return render(request, 'index.html', context)


def ages(request):
    ott = request.GET['ott']
    result = MyAnalysis().forage(ott)
    return HttpResponse(json.dumps(result), content_type='application/json')


def ScatterPlot(request):
    context = {
        'section': 'ScatterPlot.html'
    }
    return render(request, 'index.html', context)


def sp(request):
    ott = request.GET['ott']
    result = MyAnalysis().ImdbScatter(ott)
    return HttpResponse(json.dumps(result), content_type='application/json')


# -----------------------------------------------------------------------------#
## 현수님 코드 구현
def tp(request):
    context = {
        'section': 'tp.html'
    }
    return render(request, 'index.html', context)


def chs1(request):
    year = request.GET['year'];
    data = CHS().chs1(year);
    return HttpResponse(json.dumps(data), content_type='application/json');


def tablechs(request):
    data = CHS().chs2()
    context = {
        'section': 'tablechs.html',
        'data': data
    };
    return render(request, 'index.html', context)


def tablechs2(request):
    data = CHS().chs3()
    context = {
        'section': 'tablechs2.html',
        'data': data
    };
    return render(request, 'index.html', context)


# -----------------------------------------------------------------------------#
## 운기님 코드 구현
def matrix(request):
    context = {
        'section': 'matrix.html'
    }
    return render(request, 'index.html', context)


def imdbrate(request):
    context = {
        'section': 'imdbrate.html'
    }
    return render(request, 'index.html', context)


def imrate(request):
    ott = request.GET['ott']
    result = MyAnalysis().ImdbRate(ott)
    return HttpResponse(json.dumps(result), content_type='application/json')


# -----------------------------------------------------------------------------#
## 청하님 코드 구현
def tp1(request):
    context = {
        'section': 'tp1.html'
    }
    return render(request, 'index.html', context)


def TP1(request):
    data = RCH().TP1()
    return HttpResponse(json.dumps(data), content_type='application/json');


def tp32(request):
    context = {
        'section': 'tp32.html'
    }
    return render(request, 'index.html', context)


def TP32(request):
    ott = request.GET['ott']
    print(ott)
    data = RCH().TP32(ott)
    return HttpResponse(json.dumps(data), content_type='application/json');
