#coding:utf-8
from __future__ import unicode_literals
import os
import sys
import tkMyFileDialog
from Tkinter import *
import multiprocessing
sys.path.append('..')

def start_server():

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stats.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)

def read_data():
    from statistics.data_source import DataSource
    from statistics.stat_data import StatData

    frmMain = Tk()
    #frmMain.geometry("300x200")
    la=None
    def askopenfilenamelist():
        #print tkFileDialog.askopenfile(mode='r',parent=frmMain,multiple = 1)
        #print tkFileDialog.askopenfile(mode='r',parent=frmMain,multiple = 1)
        c=tkMyFileDialog.askopenexcelfiles(parent=frmMain,multiple=1,filetypes = [('all files', '.*'),('xlsx files', '.xlsx'),('xls','.xls')] )
        dt=StatData(c)
        rs=dt.get_tr_rs()
        la=Label(frmMain, text='\n'.join(c),fg='blue')
        la.pack()
        return c
    #la=Label(frmMain, text=';'.join(name_list))
    btn = Button(text="读取文件",command=askopenfilenamelist)
    btn.pack()
    frmMain.mainloop()
if __name__=='__main__':

    start_server()
    global p2
    p2 = multiprocessing.Process(target = read_data)
    if not p2.is_alive():
        p2.start()
    os.system('python ../manage.py runserver 0.0.0.0:8080 &')
