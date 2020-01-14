from django.shortcuts import render
import requests

def home(request):
    response = requests.get("https://api.breezometer.com/air-quality/v2/current-conditions?lat=26.3683&lon=-80.1289&key=26d253d0e9ef431c8656762275de4471&features=health_recommendations,breezometer_aqi")
    data = response.json()
    data1 = data['data']
    data2 = data1['indexes']
    data3 = data2['baqi']
    weatherresponse = requests.get("https://api.aerisapi.com/observations/boca,fl?client_id=Dcbk6XyhB7RQNRqmmsCcN&client_secret=vBOMeeL2INJasmXRQSeUCGMraXSzfxQOMJY4Ppwl")
    dat = weatherresponse.json()
    dat1 = dat["response"]
    dat2 = dat1['ob']

    return render(request, 'directory.html', {
        'datetime': data3['aqi'],
        'recc' : data1['health_recommendations'],
        'aqi': dat2['tempF'],

        'aqi2': dat2['weather'],
        'aqi3': dat2['windSpeedMPH'],
        'aqi4': dat2['feelslikeF'],


        
    })
