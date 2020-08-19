import unittest

from utils.datautils import DataUtils
from utils.excelutils import ExcelUtils
from utils.reportutils import ReportUtils
from utils.requestutils import RequestUtils


class MyUnit(unittest.TestCase):
    def setUp(self):
        # 初始化工具类
        self.dataUtils = DataUtils()
        self.excelUtils = ExcelUtils()
        self.requestUtils = RequestUtils()
        # 定义报告工具类
        self.reportUtils = ReportUtils()

    def tearDown(self):
        pass