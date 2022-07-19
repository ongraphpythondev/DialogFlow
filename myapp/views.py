# from unittest import result
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
# import requests
# Create your views here.
def home(requests):
    return render(requests,'index.html')
@csrf_exempt
def webHook(requests):
    req = json.loads(requests.body)
    weather = req['queryResult']['intent']['displayName']
    # print(req)
    if weather=='weather':
        import requests as re
        api_key = '1a1c81af300a919cbc5225327e83dca2'
        if req['queryResult']['parameters']['geo-city'] != '':
            location = req['queryResult']['parameters']['geo-city']
        else:
            location = req['queryResult']['parameters']['geo-country']
        # location = 'japan'
        current = re.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(location, api_key)).json()
        desc = current['weather'][0]['description']
        temp = current['main']['temp']
        # print(current)
        fulfillmentText = {'fulfillmentText': f'The weather in {location} is {desc} and the temperature is {temp}'}
        result = req.get('queryResult')
        if result.get('action')=='get.address':
            fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.'}
        return JsonResponse(fulfillmentText,safe=False)

