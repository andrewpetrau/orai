from django.shortcuts import render
import requests
# Create your views here.

def gauti_orus(miestas, api_raktas):
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={miestas}&appid={api_raktas}&units=metric&lang=lt"
    response = requests.get(URL)
    duomenys = response.json()
    
    if response.status_code == 200:
        oras = {
            "miestas": duomenys["name"],
            "temperatura": duomenys["main"]["temp"],
            "aprasymas": duomenys["weather"][0]["description"]
        }
        return oras
    else:
        print(duomenys["message"])
        return None

def oru_prognose(request):
    if request.method == "POST":
        miestas = request.POST.get('miestas')
        api_raktas = "2ba06a0879575db8a85370334faf2250"
        duomenys = gauti_orus(miestas, api_raktas)
        
        if duomenys:
            return render(request, 'oru_prognose.html', duomenys)
        else:
            return render(request, 'oru_prognose.html', {"klaida": "Nepavyko gauti orų duomenų arba miestas nebuvo rastas."})
    else:
        return render(request, 'oru_prognose.html')