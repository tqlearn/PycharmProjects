#coding:utf-8
import os
import sys
base_path = os.getcwd()
sys.path.append(os.path.dirname(base_path))
_global_dict={}
def _init():
    global _global_dict
    _global_dict = {}

def set_value(name, value):
    _global_dict[name] = value

def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue