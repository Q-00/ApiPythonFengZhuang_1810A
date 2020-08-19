import json


# 数据工具类
from utils.excelutils import ExcelUtils
from utils.varutils import VarUtils


class DataUtils:
    def __init__(self):
        # 用到excelUtils对象
        self.excelutils = ExcelUtils()

    # 获取用例id
    def getCaseId(self, row):
        return self.excelutils.getExcelData(row, VarUtils.ID)

    # 获取用例名称
    def getCaseName(self, row):
        return self.excelutils.getExcelData(row, VarUtils.REQUEST_NAME)

    # 获取请求方式
    def getRequestMethod(self, row):
        return self.excelutils.getExcelData(row, VarUtils.REQUEST_METHOD)

    # 获取请求地址
    def getRequestUrl(self, row):
        return self.excelutils.getExcelData(row, VarUtils.REQUEST_URL)

    # 获取请求参数 通过loads将字符串转换成字典
    def getRequestParams(self, row):
        return json.loads(self.excelutils.getExcelData(row, VarUtils.REQUEST_PARAMS))

    # 获取请求头
    def getRequestHeaders(self, row):
        result = self.excelutils.getExcelData(row, VarUtils.REQUEST_HEADERS)
        if result == None or result == "" or result == "否":
            return None
        else:
            return result

    # 获取预期结果
    def getExpectResult(self, row):
        str = self.excelutils.getExcelData(row, VarUtils.EXPECT_RESULT)
        return str

    # 设置实际结果 ---将字典转换成json字符串
    def setActualResult(self, row, dict):
        str = json.dumps(dict, indent=4, ensure_ascii=False, sort_keys=True)
        print('------str-----',str)
        self.excelutils.writeExcelData(row, VarUtils.ACTUAL_RESULT, str)

    # 设置是否通过 boolean类型
    def setIsPassed(self, row, flag):
        if flag == True:
            self.excelutils.writeExcelData(row, VarUtils.IS_PASSED, "通过")
        else:
            self.excelutils.writeExcelData(row, VarUtils.IS_PASSED, "不通过")

