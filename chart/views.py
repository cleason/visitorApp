from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Visitor
import json

# Create your views here.

def googleChart(request):
    #h_var : The title for horizontal axis
    h_var = 'Click'
    #v_var : The title for horizontal axis
    v_var = 'Visitors'
    data = [[h_var,v_var]]
    visitors = Visitor.objects.all()
    for visitor in visitors:
        data.append([visitor.click,visitor.viewer])
    h_var_JSON = json.dumps(h_var)
    v_var_JSON = json.dumps(v_var)
    modified_data = json.dumps(data)
    return render(request,"charts.html",{'values':modified_data, 'h_title':h_var_JSON,'v_title':v_var_JSON})