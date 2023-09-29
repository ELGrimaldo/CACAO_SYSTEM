from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SensorData
from datetime import datetime

# Create your views here.
def streamlit_view(request):
    return render(request, 'streamlit.html')

def index(request):
    return render(request, 'dashboard.html')

def boxes(request):
    return render(request, 'boxes.html')

def connection(request):
    return render(request, 'connection.html')

def base(request):
    return render(request, 'base.html')

@csrf_exempt
def receive_data(request):
    """ Handles incoming sensor data from an ESP32. """

    if request.method == 'POST':
        box_no = request.POST.get('box_no')
        mq2 = request.POST.get('mq2')
        mq3 = request.POST.get('mq3')
        mq7 = request.POST.get('mq7')
        mq9 = request.POST.get('mq9')
        mq135 = request.POST.get('mq135')

        if box_no == '1':
            BoxOne.objects.create(mq2 = mq2,
                                  mq3 = mq3,
                                  mq7 = mq7,
                                  mq9 = mq9,
                                  mq135 = mq135)
            
        elif box_no == '2':
            BoxTwo.objects.create(mq2 = mq2,
                                  mq3 = mq3,
                                  mq7 = mq7,
                                  mq9 = mq9,
                                  mq135 = mq135)
            
        elif box_no == '3':
            BoxThree.objects.create(mq2 = mq2,
                                    mq3 = mq3,
                                    mq7 = mq7,
                                    mq9 = mq9,
                                    mq135 = mq135)
            
        elif box_no == '4':
            BoxFour.objects.create(mq2 = mq2,
                                   mq3 = mq3,
                                   mq7 = mq7,
                                   mq9 = mq9,
                                   mq135 = mq135)
        
        print("[SERVER LOG] Data received successfully from box no. " + box_no + ": \n" + 
                            "MQ2: " + mq2 + ", " +
                            "MQ3: " + mq3 + ", " +
                            "MQ7: " + mq7 + ", " +
                            "MQ9: " + mq9 + ", " +
                            "MQ135: " + mq135)
        
        return HttpResponse("[FROM SERVER] Your sent data from box no. " + box_no + ": \n" + 
                            "MQ2: " + mq2 + ", " +
                            "MQ3: " + mq3 + ", " +
                            "MQ7: " + mq7 + ", " +
                            "MQ9: " + mq9 + ", " +
                            "MQ135: " + mq135)
    else:
        return HttpResponse("[FROM SERVER] Invalid request method")
