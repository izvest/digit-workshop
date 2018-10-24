from django.shortcuts import render
import requests

def home(request):
    response = requests.get("http://data.foli.fi/siri/sm/T4/pretty").json()
    line = response["result"][0]["lineref"]
    time = round((response["result"][0]["expecteddeparturetime"]-response["result"][0]["recordedattime"])/60)
    return render(request, 'foli/home.html', {
        'line': line,
        'departure': time
    })