# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#data struct

#天融系统
class TianRong:
    def __init__(self,item_list=[]):
        self.asum=''; #汇总
        self.customer_tel = ''; #客户电话
        self.phone_lc = '';     #来电地区
        self.hot_line = '';     #热线号码
        self.ivr = '';          #IVR
        self.queue_no = '';     #队列号
        self.queue_name = '';   #队列名
        self.worker_id = '' ;   #座席工号
        self.worker_name = '';  #座席姓名
        self.worker_tel = '';   #座席电话
        self.start_time = '';   #开始时间
        self.call_time = '';    #通话时间
        self.call_duration = '';    #通话时长
        self.call_stat = '';    #接听状态
        self.out_hood = '';     #挂机方
        self.spend_time = '';   #总时长
        self.tape = '';         #录音
        self.tel_bill = '';     #话费
        self.custom_fields = '';    #自定义字段
        self.remark = '';           #备注
        self.is_in_doc = '';    #是否在案例库
        self.quality_score = '';    #质检评分
        self.quality_remark = '';   #质检备注
        self.load_data(item_list)


    def load_data(self,item_list):
        if not item_list:
            return None
        self.asum = ''
        self.customer_tel = item_list[0]
        self.phone_lc = item_list[1]
        self.hot_line = item_list[2]
        self.ivr = item_list[3]
        self.queue_no = item_list[4]
        self.queue_name = item_list[5]
        self.worker_id = item_list[6]
        self.worker_name = item_list[7]
        self.worker_tel = item_list[8]
        self.start_time = item_list[9]
        self.call_time = item_list[10]
        self.call_duration = item_list[11]
        self.call_stat = item_list[12]
        self.out_hood = item_list[13]
        self.spend_time = item_list[14]
        self.tape = item_list[15]
        self.tel_bill = item_list[16]
        self.custom_fields = item_list[17]
        self.remark = item_list[18]
        self.is_in_doc = item_list[19]
        self.quality_score = item_list[20]
        self.quality_remark = item_list[21]
