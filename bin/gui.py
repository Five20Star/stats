#coding:utf-8
import os
import sys
import wx
import multiprocessing
import django
sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stats.settings")
django.setup()
from statistics.data_source import DataSource
from statistics.stat_data import StatData
       

def read_data():

    def btn_click(tNone):
        wildcard = "xls Files (*.xls*)|*.xls*" 
        dlg = wx.FileDialog(None, "Choose a file", "D:/", "", wildcard, wx.FD_MULTIPLE)
        if dlg.ShowModal() == wx.ID_OK:
            c = dlg.GetPaths()
            dt=StatData(c)
            rs=dt.get_tr_rs()
        dlg.Destroy()

    app = wx.App() 
    window = wx.Frame(None, title = u"拓扑信息", size = (400,300)) 
    panel = wx.Panel(window)
    # la=wx.StaticText(panel,1, label='balue', pos=(120,130))
    btn = wx.Button(panel, 1, label=u"文件读取", pos=(120,100))
    btn.Bind(wx.EVT_BUTTON,btn_click)
    window.Show(True)
    app.MainLoop()

if __name__=='__main__':
    p2 = multiprocessing.Process(target = read_data)
    p2.start()
    os.system('python ../manage.py runserver 0.0.0.0:8080')
