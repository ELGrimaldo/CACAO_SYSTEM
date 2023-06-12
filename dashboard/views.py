from django.shortcuts import render
from django.http import HttpResponse

from .manageData import list_files, CacaoData

# Create your views here.


def index(request):
    context = {'boxes':{}}

    counter = 1
    for file in list_files():
        data = CacaoData(file)
        data = data.get_data()
        mq2 = list(data['mq2_smooth'].values())
        mq3 = list(data['mq3_smooth'].values())
        mq7 = list(data['mq7_smooth'].values())
        mq9 = list(data['mq9_smooth'].values())
        mq135 = list(data['mq135_smooth'].values())

        
        file = file.split('.')[0]
        context['boxes'][f'Box{counter}'] = {
            'MQ-2': mq2,
            'MQ-3': mq3,
            'MQ-7': mq7,
            'MQ-9': mq9,    
            'MQ-135': mq135
            }
        
        counter +=1
    return render(request, 'pages/dashboard.html', context)

def boxes(request):
    return render(request, 'pages/boxes.html')

def connection(request):
    return render(request, 'pages/connection.html')

def base(request):
    return render(request, 'pages/base.html')