from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SensorData
from datetime import datetime

# Create your views here.
def streamlit_view(request):
    return render(request, 'streamlit.html')

def index(request):
    return render(request, 'chart.html')

def boxes(request):
    return render(request, 'data.html')

def connection(request):
    return render(request, 'cuttest.html')

def base(request):
    return render(request, 'base.html')

@csrf_exempt
def receive_data(request):
    """ Handles incoming sensor data from an ESP32. """

    # If it's a POST request, then extract the HTTP request data (sensor reading)
    if request.method == 'POST':
        mq2 = request.POST.get('mq2')
        mq3 = request.POST.get('mq3')
        mq7 = request.POST.get('mq7')
        mq9 = request.POST.get('mq9')
        mq135 = request.POST.get('mq135')

        # Then, store sensor reading in database
        SensorData.objects.create(mq2, mq3, mq7, mq9, mq135)
        
        # Log the received data in the server
        print("[SERVER LOG] Data received: \n" + 
                            "MQ2: " + mq2 + ", " +
                            "MQ3: " + mq3 + ", " +
                            "MQ7: " + mq7 + ", " +
                            "MQ9: " + mq9 + ", " +
                            "MQ135: " + mq135)
        
        # Finally, return a success message
        return HttpResponse("[FROM SERVER] Data received successfully")
    
    # If it's not a POST request, return an error message
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
