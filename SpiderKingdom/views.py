from django.shortcuts import render
from django.shortcuts import HttpResponse
from Registry.models import Domain
from django.forms.models import model_to_dict
import json
# Create your views here.
def domain(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Domain.objects.create(**data)
        return HttpResponse(json.dumps({'status_code':200}))
    if request.method == "GET":
        queryset_data = Domain.objects.all().values()
        print(list(queryset_data))

        return HttpResponse(json.dumps({'status_code':200,'data':list(queryset_data)}))

