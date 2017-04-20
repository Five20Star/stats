#coding:utf-8
from pyexcel_xls import get_data,save_data
from collections import OrderedDict
from statistics.models import TianRong

class DataSource(object):
    
    def __init__(self,fpath):
        self.fpath=fpath
        self.origin_data = []
        self.load_data()
        self.rs=[]

    def load_data(self):
        rs = self.fpath and get_data(self.fpath) or {}
        self.origin_data = rs and rs['Sheet1'] or []
    def get_json(self):
        for it in self.origin_data[1:100]:
            tr=TianRong(it)
            self.rs.append(tr)
        return self.rs
if __name__=='__main__':
    dt=DataSource('天润系统.xlsx')
    print dt.get_json()
