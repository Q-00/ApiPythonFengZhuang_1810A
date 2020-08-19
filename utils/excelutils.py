
import xlrd
from xlutils.copy import copy

class ExcelUtils:
    # 初始化的函数
    def __init__(self, excel_file="../data/fangjingdong.xls",table_index=0):
        #打开工作簿
        workbook = xlrd.open_workbook(excel_file)
        # 获取对应的表
        self.table = workbook.sheets()[table_index]
        self.excel_file = excel_file
        self.workbook = workbook
    # 能够获取当前多少个测试用例...nrows
    def getCaseCount(self):
        return self.table.nrows

    # 获取单元格内容
    def getExcelData(self, row, col):
        return self.table.cell_value(row, col)

    # 写入单元格内容
    def writeExcelData(self, row, col, value):
        #先重新打开工作簿
        read_data = xlrd.open_workbook(self.excel_file)
        #copy复制保留
        write_data = copy(read_data)
        #获取第一个工作表
        sheet_data = write_data.get_sheet(0)
        #写入内容
        sheet_data.write(row, col, value)
        #保存
        write_data.save(self.excel_file)

