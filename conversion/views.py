from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

def conversion_page(request):
    return render(request, "conversion/index.html")

@api_view(['POST'])
def convert_value(request):
    data = request.data
    try:
        sensor_min = float(data.get('sensor_min'))
        sensor_max = float(data.get('sensor_max'))
        output_min = float(data.get('output_min'))
        output_max = float(data.get('output_max'))
        value = float(data.get('value'))
        direction = data.get('direction')

        if direction == 'sensor_to_output':
            result = output_min + ((value - sensor_min) * (output_max - output_min)) / (sensor_max - sensor_min)
        elif direction == 'output_to_sensor':
            result = sensor_min + ((value - output_min) * (sensor_max - sensor_min)) / (output_max - output_min)
        else:
            return Response({"error": "Invalid conversion direction"}, status=400)

        return Response({"converted_value": result})
    except Exception as e:
        return Response({"error": str(e)}, status=400)
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

def conversion_page(request):
    return render(request, "conversion/index.html")

@api_view(['POST'])
def convert_value(request):
    data = request.data
    try:
        sensor_min = float(data.get('sensor_min'))
        sensor_max = float(data.get('sensor_max'))
        output_min = float(data.get('output_min'))
        output_max = float(data.get('output_max'))
        value = float(data.get('value'))
        direction = data.get('direction')

        if direction == 'sensor_to_output':
            result = output_min + ((value - sensor_min) * (output_max - output_min)) / (sensor_max - sensor_min)
        elif direction == 'output_to_sensor':
            result = sensor_min + ((value - output_min) * (sensor_max - sensor_min)) / (output_max - output_min)
        else:
            return Response({"error": "Invalid conversion direction"}, status=400)

        return Response({"converted_value": result})
    except Exception as e:
        return Response({"error": str(e)}, status=400)
# views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Simple page to return the HTML form
def conversion_page(request):
    return render(request, "conversion/index.html")

# Conversion logic API
@api_view(['POST'])
def convert_value(request):
    data = request.data
    try:
        sensor_min = float(data.get('sensor_min'))
        sensor_max = float(data.get('sensor_max'))
        output_min = float(data.get('output_min'))
        output_max = float(data.get('output_max'))
        value = float(data.get('value'))
        direction = data.get('direction')

        if direction == 'sensor_to_output':
            result = output_min + ((value - sensor_min) * (output_max - output_min)) / (sensor_max - sensor_min)
        elif direction == 'output_to_sensor':
            result = sensor_min + ((value - output_min) * (sensor_max - sensor_min)) / (output_max - output_min)
        else:
            return Response({"error": "Invalid conversion direction"}, status=400)

        return Response({"converted_value": result})
    except Exception as e:
        return Response({"error": str(e)}, status=400)

