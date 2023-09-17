from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
    return render(request, 'dashboard.html', context)

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
        mq2_value = request.POST.get('mq2_value')
        mq3_value = request.POST.get('mq3_value')
        mq7_value = request.POST.get('mq7_value')
        mq9_value = request.POST.get('mq9_value')
        mq135_value = request.POST.get('mq135_value')
        ph_value = request.POST.get('ph_value')
        temp_value = request.POST.get('temp_value')

        SensorData.objects.create(
            box_no=box_no,
            mq2_value=mq2_value,
            mq3_value=mq3_value,
            mq7_value=mq7_value,
            mq9_value=mq9_value,
            mq135_value=mq135_value,
            ph_value=ph_value,
            temp_value=temp_value,
            timestamp=datetime.datetime.now()
        )
        
        print("Data received successfully. " +
                            "Box no.: " + box_no + "\n" + 
                            "MQ2: " + mq2_value + " " +
                            "MQ3: " + mq3_value + " " +
                            "MQ7: " + mq7_value + " " +
                            "MQ9: " + mq9_value + " " +
                            "MQ135: " + mq135_value + " " +
                            "pH: " + ph_value + " " + 
                            "Temperature: " + temp_value)
        
        return HttpResponse("Data received successfully. " +
                            "Box no.: " + box_no + " " + 
                            "MQ2: " + mq2_value + " " +
                            "MQ3: " + mq3_value + " " +
                            "MQ7: " + mq7_value + " " +
                            "MQ9: " + mq9_value + " " +
                            "MQ135: " + mq135_value + " " +
                            "pH: " + ph_value + " " + 
                            "Temperature: " + temp_value)
    else:
        return HttpResponse("Invalid request method")
