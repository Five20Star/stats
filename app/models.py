# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BlogPost(models.Model):
        kid = models.AutoField(primary_key=True)
        name = models.TextField()
        sex  = models.TextField()
        desci = models.TextField()
        class Meta:
            db_table='BlogPost'
class Dta(models.Model):
    dta_id=models.AutoField(primary_key=True)
    name=models.TextField()
    worker_id=models.TextField()
    answer=models.TextField(default='---')
    unAnswer=models.TextField(default='---')
    call_times=models.TextField(default='---')
    call_duration=models.TextField(default='---')
    avg_call_duration=models.TextField(default='---')
    valid_call_times=models.TextField(default='---')
    valid_call_duration=models.TextField(default='---')
    valid_call_avg_duration=models.TextField(default='---')
    valid_call_radio=models.TextField(default='---')

    gd_call_duration=models.TextField(default='---')
    gd_call_times=models.TextField(default='---')
    gd_call_in_ctimes=models.TextField(default='---') 
    gd_call_avg_duration=models.TextField()
    gd_valid_call_nums=models.TextField(default='---')
    gd_valid_call_duration=models.TextField(default='---')
    gd_valid_call_avg_duration=models.TextField(default='---')
    gd_valid_call_radio=models.TextField()

    qn_worker_no=models.TextField(default='---')
    qn_call_duration=models.TextField(default='---')
    qn_call_times=models.TextField(default='---')
    qn_avg_call_duration=models.TextField(default='---')
    qn_valid_call_times=models.TextField(default='---')
    qn_valid_call_all_duration=models.TextField(default='---')
    qn_valid_avg_call_duration=models.TextField(default='---')
    qn_valid_call_radio=models.TextField(default='---')

    date=models.TextField(default='---')
    created_at=models.DateTimeField()

    class Meta:
        db_table='Dta'
