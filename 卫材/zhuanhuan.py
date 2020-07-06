import json
import xlrd
from xlutils.copy import copy
import os
class OpenExcel(object):
    def __init__(self,filname=None,index=None):
        self.filname = filname
        if self.filname==None:
            self.file = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            #self.filname=self.file+"\\dataconfig\\Anyang_interface.xlsx"
            self.filname='D:\\test.xls'
            self.book = xlrd.open_workbook(self.filname)
        else:
            self.book = xlrd.open_workbook(self.filname)
        self.name = self.get_sheet(index)
    def get_sheet(self,index=None):
        sheetname = None
        if index != None:
            sheetname = self.book.sheets()[index]
        else:
            sheetname = self.book.sheets()[0]
        return sheetname
    def get_lines(self,index=None):
        #lines = self.name.nrows
        if index!=None:
            lines = self.get_sheet(index).nrows
        else:
            lines = self.name.nrows
        return lines
    def get_value(self,row,col,index=None):
        if index == None:
            value = self.name.cell(row,col).value
        else:
            value = self.get_sheet(index).cell(row,col).value
        return value
    def get_row_values(self,row):
        row_values = self.name.row_values(row)
        return row_values
    def get_col_values(self,col):
        col_values = self.name.col_values(col)
        return col_values
    def set_values(self,row,col,val,index=None):
        if index == None:
            read = xlrd.open_workbook(self.filname)
            write_data = copy(read)
            w = write_data.get_sheet(0)
            w.write(row,col,val)
            write_data.save(self.filname)
        else:
            read = xlrd.open_workbook(self.filname)
            write_data = copy(read)
            w = write_data.get_sheet(1)
            w.write(row, col, val)
            write_data.save(self.filname)

def test01():
    res = OpenExcel()
    data = open('test.json')
    data = data.read()
    data = json.loads(data)
    print(data)
    print(type(data))
    for i in range(len(data['date'])):
        uid = data['date'][i]['uid']
        print(uid)
        start_time = data['date'][i]['start_time']
        end_time = data['date'][i]['end_time']
        tt = data['date'][i]['tt']
        pf = data['date'][i]['pf']
        browser = data['date'][i]['browser']
        viewer_province = data['date'][i]['viewer_province']
        created_time = data['date'][i]['created_time']
        i = i+1
        res.set_values(i,0,uid)
        res.set_values(i, 1, start_time)
        res.set_values(i, 2, end_time)
        res.set_values(i,3,tt)
        res.set_values(i, 4, pf)
        res.set_values(i, 5, browser)
        res.set_values(i, 6, viewer_province)
        res.set_values(i,7,created_time)


if __name__ == '__main__':
    test01()
