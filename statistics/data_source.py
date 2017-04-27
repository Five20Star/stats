#coding:utf-8
import os
from django.conf import settings
from pyexcel_xls import get_data,save_data
from collections import OrderedDict
from statistics.models import TianRong,QingNiu,GuDe

class DataSource(object):
    
    def __init__(self,dir_path):
        self.dir_path = os.listdir(dir_path)
        self.tianrong_rs = []
        self.qingniu_rs = []
        self.gude_rs = []
        self.load_data()

    def get_xlx_data(self,fpath):
        return get_data(fpath)

    def load_data(self):
        for it in self.dir_path:
            if u'青牛' in it:
                print '>>>>>>>>',it
                self.get_qingniu(settings.UPLOAD_PATH+'/'+it)
            elif u'古德' in it:
                print 'zzzzzzzzzz',it
                self.get_gude(settings.UPLOAD_PATH+'/'+it)
            elif u'天润' in it:
                print 'xxxxxxxxxxx',it
                self.get_tianrong(settings.UPLOAD_PATH+'/'+it)
    def get_tianrong(self,fpath):
        data=get_data(fpath)
        rs = data and data['Sheet1'] or []
        for it in rs[1:]:
            if not it[8]:
                continue
            tr=TianRong(it)
            self.tianrong_rs.append(tr)
        return self.tianrong_rs

    def get_qingniu(self,fpath):
        data=get_data(fpath)
        rs = data and data['Sheet1'] or []
        for it in rs[4:]:
            tr=QingNiu(it)
            self.qingniu_rs.append(tr)
        return self.qingniu_rs

    def get_gude(self,fpath):
        data=get_data(fpath)
        rs = data and data['Sheet1'] or []
        for it in rs[1:]:
            tr=GuDe(it)
            self.gude_rs.append(tr)
        return self.gude_rs






if __name__=='__main__':
    dt=DataSource('/home/sw/stats/upload')
