from django.shortcuts import render

# Create your views here.
def homepage(request):
    import requests
    import json

    cases_request = requests.get("https://api.covid19api.com/summary")
    case = json.loads(cases_request.content)
    return render(request, 'home.html', {'case':case})




def example(request):
    import requests
    import json

    cases_request = requests.get("https://api.covid19api.com/summary").json()
    return render(request, 'example.html', {'case':cases_request})

def countries(request):
    import requests
    import json
    cases_request = requests.get("https://api.covid19api.com/summary").json()
    return render(request, 'countries.html', {'case':cases_request['Countries']})


def example2(request):
    import requests
    import json
    # grab crpto price
    price_request = requests.get("https://api.covid19api.com/summary")
    price = json.loads(price_request.content)
    return render(request, 'example2.html', {'price':price})
