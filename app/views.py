# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from statistics.stat_data import StatData


# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request, 'app/upload.html')

def cal(request):
    dt=StatData('/home/sw/stats/upload')
    rs=dt.get_tr_rs()
    return render(request, 'app/detail.html',{'rs_map':rs})
def upload_file(request):
    if request.method == "POST": 
        file_list =request.FILES.getlist("myfile")
        if not file_list:  
            return HttpResponse("no files for upload!")
        for f in file_list:
            destination = open(os.path.join(settings.UPLOAD_PATH,f.name),'wb+')
            for chunk in f.chunks():      # 分块写入文件  
                destination.write(chunk)  
            destination.close()  
        return render(request,'app/success.html')
