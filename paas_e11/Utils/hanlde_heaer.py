import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from Utils.handle_json import read_json

def get_header():
    data=read_json("/config/header.json")
    return data