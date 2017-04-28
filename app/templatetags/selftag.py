# encoding: utf-8
from django import template
import  binascii
register = template.Library()

@register.filter(name='cut11')
def cut1(value, arg):
    seconds=int(value)
    hour = str(seconds/3600) or '00'
    mins = str(seconds%3600/60) or '00'
    sec =  str(seconds%3600%60)
    return hour+':'+mins+':'+sec

@register.filter(name='banary_to_str')
def binary_to_string(value,arg):
    #if type(value) in [int,float]:
    #print '........',value
    if type(value) in [int,float] or (not value.count('-')):
        seconds=int(float(value))
        hour = str(seconds/3600) or '00'
        mins = str(seconds%3600/60) or '00'
        sec =  str(seconds%3600%60)
        return (len(hour)<2 and '0'+hour or hour)+':'+(len(mins)<2 and '0'+mins or mins)+':'+(len(sec)<2 and '0'+sec or sec)
    else:
        return value




