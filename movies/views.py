import json

from django.http import HttpResponse
from django.shortcuts import render

from analysis.sjh import MyAnalysis
from analysis.chs import CHS
from analysis.myanalysis import Api, Titanic, Open, Naver

## 페이지 메인 세션
def index(request):
    return render(request, 'index.html')

#-----------------------------------------------------------------------------#
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


## 현수님 코드 구현
def tp(request):
    context = {
        'section': 'tp.html'
    }
    return render(request, 'index.html', context)

def chs1(request):
    year=request.GET['year'];
    data = CHS().chs1(year);
    return HttpResponse(json.dumps(data), content_type='application/json');

## 운기님 코드 구현
def matrix(request):
    context = {
        'section': 'matrix.html'
    }
    return render(request, 'index.html', context)


## 남은거. 마지막에 다 돌아가고난 뒤 지워야 에러 안남

def tables(request):
    context = {
        'section': 'tables.html'
    }
    return render(request, 'index.html', context)

def db1(request):
    context = {
        'section': 'db1.html'
    }
    return render(request, 'index.html', context)

def db5(request):
    context = {
        'section': 'db5.html'
    }
    return render(request, 'index.html', context)

def geo(request):
    context = {
        'section': 'geo.html'
    }
    return render(request, 'index.html', context)

def chart(request):
    feature = request.GET['feature']
    print(feature)
    result = Titanic().t1(feature)
    return HttpResponse(json.dumps(result), content_type='application/json')

def db2s(request):
    result = Naver().n1()
    return HttpResponse(json.dumps(result), content_type='application/json')

def db3s(request):
    startdt = request.GET['sd']
    enddt = request.GET['ed']
    result = Open().o1(startdt, enddt)
    return HttpResponse(json.dumps(result), content_type='application/json')


def wspr(request):
    # open API로부터 데이터를 가져온다
    lst = Api().covid19()
    context = {
        'section': 'ws_practice.html',
        'result': lst
    }
    return render(request, 'index.html', context)


