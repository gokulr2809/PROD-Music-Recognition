from msilib.schema import File
from django.shortcuts import render
from django.http import HttpResponse
from python.code.rec import * 
from python.code.main import *
import json

def index(request):
    return render(request,'index.html',{"con": 'True'})   
def history(request):
    return render(request,'history.html')
   
def rec_func(request):
    if request.method == 'GET':
        File_name = recorder()
        output = final(File_name)
        print(output.type)
        return render(request,'process.html',{"con": 'False',"output":output})

        