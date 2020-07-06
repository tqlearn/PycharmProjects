#coding : utf-8
import xlrd

class ReadExcel(object):
    filename = "..\config\APIcase.xlsx"
    excel = xlrd.open_workbook(filename)
    sheet = excel.sheet_by_index(0)

    def get_excel_data(self,row,col):
        data = self.sheet.cell_value(row,col)
        return data

    def get_excel_rows(self):
        row = self.sheet.nrows
        return row

    def get_cols(self,col):
        col = self.sheet.col_values(col)
        return col

if __name__ == "__main__" :
    re = ReadExcel()
    print(re.get_excel_data(1,1))