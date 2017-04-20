#coding:utf-8
from pyexcel_xls import get_data,save_data
from collections import OrderedDict






class StatData(object):
    
    def __init__(self):
        self
    def load_data(self):
        pass
    def get_json(self):
        pass

if __name__=='__main__':
    data=get_data('青牛系统4月份数据.xls')
    for it in data[u'Sheet1']:
        print it
