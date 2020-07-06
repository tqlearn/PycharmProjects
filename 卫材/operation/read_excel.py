#coding : utf-8
import xlrd
from xlutils.copy import copy
from excel_config import *
class ReadExcel(object):
    def __init__(self):
        self.filename = '..\config\case.xls'
        self.data = xlrd.open_workbook(self.filename)
        self.sheet = self.data.sheet_by_index(0)


    def get_data(self,row,col):
        self.sheet.cell_value(row,col)

    def get_rows(self):
        return self.sheet.nrows

    def write_value(self,row,col,value):
        data = xlrd.open_workbook(self.filename)
        write_data = copy(data)
        write_sheet = write_data.get_sheet(0)
        write_sheet.write(row,col,value)
        write_data.save(self.filename)

if __name__ == "__main__":
    read = ReadExcel()
    col = write_user_id()
    for row in range(1,read.get_rows()):
        read.write_value(row,col,'这是一条通过python插入到excel中的数据')
        if row == 20:
            break
