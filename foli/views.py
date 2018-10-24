from django.shortcuts import render
from django.http import Http404
import requests

def home(request):
    response = requests.get("http://data.foli.fi/siri/sm/T83/pretty").json()
    line1 = response["result"][0]["lineref"]
    time1 = round((response["result"][0]["expecteddeparturetime"]-response["result"][0]["recordedattime"])/60)
    line2 = response["result"][1]["lineref"]
    time2 = round((response["result"][1]["expecteddeparturetime"]-response["result"][0]["recordedattime"])/60)
    line3 = response["result"][2]["lineref"]
    time3 = round((response["result"][2]["expecteddeparturetime"]-response["result"][0]["recordedattime"])/60)
    return render(request, 'foli/home.html', {
        'line': line1,
        'departure': time1,
        'line2': line2,
        'departure2': time2,
        'line3': line3,
        'departure3': time3,
    })

def stop_detail(request, stop_id):
    try:
        url = "http://data.foli.fi/siri/sm/" + str(stop_id)
        response = requests.get(url).json()
        line1 = response["result"][0]["lineref"]
        time1 = round((response["result"][0]["expecteddeparturetime"]-response["result"][0]["recordedattime"])/60)
        dest1 = response["result"][0]["destinationdisplay"]
        line2 = response["result"][1]["lineref"]
        time2 = round((response["result"][1]["expecteddeparturetime"]-response["result"][0]["recordedattime"])/60)
        dest2 = response["result"][1]["destinationdisplay"]
        line3 = response["result"][2]["lineref"]
        time3 = round((response["result"][2]["expecteddeparturetime"]-response["result"][0]["recordedattime"])/60)
        dest3 = response["result"][2]["destinationdisplay"]
    except:
        raise Http404('Stop does not exist')
    
    return render(request, 'foli/stop.html', {
        'stop_id': stop_id,
        'line': line1,
        'departure': time1,
        'dest1': dest1,
        'line2': line2,
        'departure2': time2,
        'dest2': dest2,
        'line3': line3,
        'departure3': time3,
        'dest3': dest3,
    })