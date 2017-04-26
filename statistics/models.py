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
        self.asum = item_list[0]
        self.customer_tel = item_list[1]
        self.phone_lc = item_list[2]
        self.hot_line = item_list[3]
        self.ivr = item_list[4]
        self.queue_no = item_list[5]
        self.queue_name = item_list[6]
        self.worker_id = item_list[7]
        self.worker_name = item_list[8]
        self.worker_tel = item_list[9]
        self.start_time = item_list[10]
        self.call_time = item_list[11]
        self.call_duration = item_list[12]
        self.call_stat = item_list[13]
        self.out_hood = item_list[14]
        self.spend_time = item_list[15]
        self.tape = item_list[16]
        self.tel_bill = item_list[17]
        self.custom_fields = item_list[18]
        self.remark = item_list[19]
        self.is_in_doc = item_list[20]
        self.quality_score = item_list[21]
        self.quality_remark = ''
class QingNiu:
    def __init__(self,item_list=[]):
        self.serial_no = '' #流水号
        self.worker_id = '' #座席工号
        self.worker_name = '' #座席姓名
        self.workder_tel= '' #坐席号码
        self.customer_call_out = '' #被叫客户号码
        self.start_time = '' #开始时间
        self.end_time = ''  #结束时间
        self.ring_duration = '' #振铃时长(小时)
        self.call_duration = '' #通话时长(小时)
        self.ex_post = '' #事后时长(小时)
        self.all_duration = '' #总时长(小时)
        self.end_type = '' #结束类型(小时)
        self.load_data(item_list)
    def load_data(self,item_list):
        if not item_list:
            return None
        self.serial_no = item_list[1]
        self.worker_id = item_list[2]
        self.worker_name = item_list[3]
        self.workder_tel= item_list[4]
        self.customer_call_out = item_list[5]
        self.start_time = item_list[6]
        self.end_time = item_list[8]
        self.ring_duration = item_list[9]
        self.call_duration = item_list[10]
        self.ex_post = item_list[11]
        self.all_duration = item_list[12]
        self.end_type = item_list[14]
class GuDe:
    def __init__(self,item_list=[]):
        if not item_list:
            return None
        self.worker_id = item_list[0]   #工号
        self.worker_name = item_list[1] #姓名
        self.dept = item_list[2]        #部门
        self.connection_nums = item_list[3]    #通话总数
        self.total_connection = item_list[4]    #接通总数
        self.total_inconnection = item_list[5]  #未接通总数
        self.connect_radio = item_list[6]       #总接通率
        self.call_in_times = item_list[7]       #呼入总数
        self.call_in_ctimes = item_list[8]      #呼入接通数
        self.call_in_uctims = item_list[9]      #呼入未接数
        self.call_in_radio = item_list[10]       #呼入接通率

        self.call_out_times = item_list[11]     #外呼总数
        self.call_out_ctimes = item_list[12]    #外呼接通数
        self.call_out_uctims = item_list[13]    #外呼未接数
        self.call_out_radio = item_list[14]     #外呼接通率
        
        self.call_duration = item_list[15]      #通话总时长
        self.call_in_duration = item_list[16]   #呼入通话总时长
        self.call_in_avg_duraion = item_list[17]    #呼入通话平均时长
        self.call_out_duration = item_list[18]      #外呼通话总时长
        self.call_out_avg_duraion = item_list[19]   #外呼通话平均时长
        self.call_out_invalid_nums = item_list[20]  #外呼无效数(30秒以内）
        self.call_out_valid_nums = item_list[21]    #外呼有效数（20秒以上）
        self.call_out_valid_radio = item_list[22]   #外呼有效率（20秒以上）
        self.call_in_connect_duraion = item_list[23]    #呼入接通总时长
        self.call_in_connect_avg_duraion = item_list[24]    #呼入接通平均时长
        self.call_in_inconnect_duration = item_list[25]     #呼入未接总时长
        self.call_in_inconnect_avg_duration = item_list[26] #呼入未接平均时长
       
        self.call_out_connect_duraion = item_list[27]   #外呼接通总时长
        self.call_out_connect_avg_duraion = item_list[28]   #外呼接通平均时长
        self.call_out_inconnect_duration = item_list[29]    #外呼未接总时长
        self.call_out_inconnect_avg_duration = item_list[30]    #外呼未接平均时长
