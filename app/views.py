# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from statistics.stat_data import StatData
from app.models import Dta
import json

# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request, 'app/upload.html')

def cal(request):
    dt=StatData('/home/sw/stats/upload')
    rs=dt.get_tr_rs()
    return render(request, 'app/look.html')

def read_db(request):
    rs=Dta.objects.all().order_by('date')
    name_list= set([ it['name'] for it in rs.values('name')])
    return render(request,'app/detail2.html',{'db_list':rs,'name_list':name_list})

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

def read_db_by_name(request):
    name_list=request.POST.getlist('names')
    st=request.POST['st']
    ed=request.POST['ed']
    flag=int(request.POST['flag'])
    if not name_list.count('null'):
        rs=Dta.objects.filter(
            name__in=name_list,
            date__gte=st,
            date__lte=ed
        ).order_by('date')
    else:
        rs=Dta.objects.filter(
            date__gte=st,
            date__lte=ed
        ).order_by('date')        
    rs_list=[]
    for it in rs:
        rs_list.append({
            'dta_id':it.dta_id,
    	    'name':it.name,
    	    'worker_id':it.worker_id,
    	    'answer':it.answer,
    	    'unAnswer':it.unAnswer,
    	    'call_times':it.call_times,
    	    'call_duration':it.call_duration,
    	    'avg_call_duration':it.avg_call_duration,
	        'valid_call_times':it.valid_call_times,
    	    'valid_call_duration':it.valid_call_duration,
	        'valid_call_avg_duration':it.valid_call_avg_duration,
	        'valid_call_radio':it.valid_call_radio,

	        'gd_call_duration':it.gd_call_duration,
	        'gd_call_times':it.gd_call_times,
	        'gd_call_in_ctimes':it.gd_call_in_ctimes,
	        'gd_call_avg_duration':it.gd_call_avg_duration,
	        'gd_valid_call_nums':it.gd_valid_call_nums,
	        'gd_valid_call_duration':it.gd_valid_call_duration,
	        'gd_valid_call_avg_duration':it.gd_valid_call_avg_duration,
	        'gd_valid_call_radio':it.gd_valid_call_radio,

	        'qn_worker_no':it.qn_worker_no,
            'qn_call_times':it.qn_call_times,
	        'qn_call_duration':it.qn_call_duration,
	        'qn_avg_call_duration':it.qn_avg_call_duration,
	        'qn_valid_call_times':it.qn_valid_call_times,
	        'qn_valid_call_all_duration':it.qn_valid_call_all_duration,
	        'qn_valid_avg_call_duration':it.qn_valid_avg_call_duration,
	        'qn_valid_call_radio':it.qn_valid_call_radio,
	        'date':it.date
        })
    return HttpResponse(json.dumps({"rs_map":rs_list}))
