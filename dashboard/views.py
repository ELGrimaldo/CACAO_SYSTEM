from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from django.views.generic import TemplateView
from .prediction import predict
from django.db.models import Avg
from . models import CacaoImages
from . cacao_image_lib import CacaoImageFunctions

import pandas as pd

# Create your views here.
def streamlit_view(request):
    return render(request, 'streamlit.html')

def index(request):
    return render(request, 'chart.html')

def boxes(request):
    return render(request, 'data.html')

def cuttest(request):
    classification_data = CacaoImageFunctions.predictImages()
    print(classification_data)
    print("indicator")
    print(CacaoImageFunctions.getImages())
    
    
    
    return render(request, 'cuttest.html', {'classification_data': classification_data})

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

def get_box_data(request, start, end):
    """ Returns the moving average data of every 3000 rows and the prediction of fermentation degree of cacao beans """

    # To store the JSON response
    response = {
        'status': 'INCOMPLETE' # Initially, there is no data and prediction result, so the status should be incomplete yet.
    }

    # Should read 3000 contiguous rows of data
    # Start and end query indices comes from the argument passed in the URL request parameter by streamlit
    data = SensorData.objects.filter(reading_id__gte=start, reading_id__lte=end).order_by('timestamp')

    # If the row count is 3000, calculate the average of each column.
    # Then, use the average values to predict the fermentation degree of cacao beans
    # and store them in a JSON and return it as response.
    if data.count() == 3000:

        # Calculate the average of each column (mq2 to mq135)
        avgs = data.aggregate(
                mq2_ave = Avg('mq2'),
                mq3_ave = Avg('mq3'),
                mq7_ave = Avg('mq7'),
                mq9_ave = Avg('mq9'),
                mq135_ave = Avg('mq135'))
        
        # Store it in JSON
        response.update(avgs)
        
        # Use the averages in a data frame (so that it can be used for prediction)
        data = pd.DataFrame({
            'mq2': [response['mq2_ave']],
            'mq3': [response['mq3_ave']],
            'mq7': [response['mq7_ave']],
            'mq9': [response['mq9_ave']],
            'mq135': [response['mq135_ave']],
        })

        # Pass in the data frame to the prediction function
        prediction = "predict(data)"

        # Store the result in JSON
        response['prediction'] = int(prediction[0][0])

        # Change the status to complete now that there is data and prediction result
        response['status'] = 'COMPLETE'
    
    # If the row count is not exactly 3000 rows, just print the row count.
    else:
        print(f"[SERVER LOG] Data count: {data.count()}")
    
    return JsonResponse(response)


def file_upload_view(request):
    if request.method == 'POST':
        
        
        # print(request.FILES)
        
        my_file = request.FILES.get('file')
        
        CacaoImages.objects.create(upload=my_file)
        
        return HttpResponse('')
    
    return JsonResponse({'post': 'false'})