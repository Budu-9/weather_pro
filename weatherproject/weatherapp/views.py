import os
from dotenv import load_dotenv
from django.shortcuts import render
import requests
import datetime

load_dotenv()

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Lagos'

    appid = os.getenv('appid')
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()

    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today

    return render(request, 'weatherapp/index.html', {'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city})
