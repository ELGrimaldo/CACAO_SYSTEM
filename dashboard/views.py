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

def get_box_one_data(request, start, end):
    response = {}
    data = BoxOne.objects.filter(reading_id__gte=start, reading_id__lte=end).order_by('timestamp')
    if data.count() < 10:
        print(f"[Box 1] {data.count()}")
        response['status'] = 'INCOMPLETE'
    else:
        response.update(data.aggregate(
            mq2_ave = Avg('mq2'),
            mq3_ave = Avg('mq3'),
            mq7_ave = Avg('mq7'),
            mq9_ave = Avg('mq9'),
            mq135_ave = Avg('mq135')))
        response['status'] = 'COMPLETE'
    return JsonResponse(response)

def get_box_two_data(request, start, end):
    response = {}
    data = BoxTwo.objects.filter(reading_id__gte=start, reading_id__lte=end).order_by('timestamp')
    if data.count() < 10:
        print(f"[Box 2] {data.count()}")
        response['status'] = 'INCOMPLETE'
    else:
        response.update(data.aggregate(
            mq2_ave = Avg('mq2'),
            mq3_ave = Avg('mq3'),
            mq7_ave = Avg('mq7'),
            mq9_ave = Avg('mq9'),
            mq135_ave = Avg('mq135')))
        response['status'] = 'COMPLETE'
    return JsonResponse(response)

def get_box_three_data(request, start, end):
    response = {}
    data = BoxThree.objects.filter(reading_id__gte=start, reading_id__lte=end).order_by('timestamp')
    if data.count() < 10:
        print(f"[Box 3] {data.count()}")
        response['status'] = 'INCOMPLETE'
    else:
        response.update(data.aggregate(
            mq2_ave = Avg('mq2'),
            mq3_ave = Avg('mq3'),
            mq7_ave = Avg('mq7'),
            mq9_ave = Avg('mq9'),
            mq135_ave = Avg('mq135')))
        response['status'] = 'COMPLETE'
    return JsonResponse(response)

def get_box_four_data(request, start, end):
    response = {}
    data = BoxFour.objects.filter(reading_id__gte=start, reading_id__lte=end).order_by('timestamp')
    if data.count() < 10:
        print(f"[Box 4] {data.count()}")
        response['status'] = 'INCOMPLETE'
    else:
        response.update(data.aggregate(
            mq2_ave = Avg('mq2'),
            mq3_ave = Avg('mq3'),
            mq7_ave = Avg('mq7'),
            mq9_ave = Avg('mq9'),
            mq135_ave = Avg('mq135')))
        response['status'] = 'COMPLETE'
    return JsonResponse(response)
