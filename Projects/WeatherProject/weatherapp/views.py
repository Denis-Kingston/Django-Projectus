from django.shortcuts import render
# Create your views here.
# weather/views.py

import requests
from django.shortcuts import render

def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')  # Get the city name from the form
        api_key = '4f5e1867b999a5a67ce1ce445485a55d'  # Your OpenWeatherMap API keys
        # Make an API request to OpenWeatherMap
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        weather_data = response.json()
        # Extract relevant weather information (e.g., temperature, conditions)
        temperature = weather_data['main']['temp']
        conditions = weather_data['weather'][0]['description']
        # context
        context={'city': city, 'temperature': temperature, 'conditions': conditions}
        return render(request, 'weather/weather.html',context)

