from django.shortcuts import render
import requests
import json

# Create your views here.
def homepage(request):
    cases_request = requests.get("https://api.covid19api.com/summary")
    case = json.loads(cases_request.content)
    return render(request, 'home.html', {'case':case})


def countries(request):
    cases_request = requests.get("https://api.covid19api.com/summary").json()
    return render(request, 'countries.html', {'case':cases_request['Countries']})


def country(request):
    if request.method == 'POST':
        country_name = request.POST['country']
        country_name = country_name.capitalize()
        cases_request = requests.get("https://api.covid19api.com/summary").json()
        cases = cases_request['Countries']
        for case in cases:
            if case['Country'] == country_name:
                return render(request, 'country_wise.html', {'country':case, 'country_name':country_name})


    else:
        return render(request, 'country_wise.html', {'country_name':country_name})


    return render(request, 'country_wise.html', {})
