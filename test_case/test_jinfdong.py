import unittest

from common.myunit import MyUnit


class FangJingDong(MyUnit):
    def testJingDong(self):
        list = []
        # 读出所有的接口测试用例
        count = self.excelUtils.getCaseCount()
        print('-----------',count)
        # 遍历所有的用例，执行
        for row in range(1, count):
            dict = {}
            # 根据行获取需要的内容
            # 根据行获取url
            url = self.dataUtils.getRequestUrl(row)
            # 获取请求方式
            method = self.dataUtils.getRequestMethod(row)
            # 获取请求参数
            params = self.dataUtils.getRequestParams(row)
            # 获取请求头
            headers = self.dataUtils.getRequestHeaders(row)
            # 获取预期结果
            expetedResult = self.dataUtils.getExpectResult(row)
            # 将用例信息封装到字典中
            dict["id"] = row
            dict["name"] = self.dataUtils.getCaseName(row)
            dict["url"] = url

            # 执行相应的请求
            actualResult = self.requestUtils.doRequest(url, method=method, data=params, headers=headers)
            # =====判断预期结果是否和实际结果一致====
            actualStatus = actualResult["code"]
            actualMsg = actualResult["msg"]


            if str(actualStatus) in expetedResult and actualMsg in expetedResult:
                print("---通过---")
                dict["is_pass"] = True
                self.dataUtils.setIsPassed(row, True)
                # 通过的个数加一
                self.reportUtils.pass_case_count += 1
                self.dataUtils.setActualResult(row, actualResult)
            else:
                dict["is_pass"] = False
                self.dataUtils.setIsPassed(row, False)
                # 往表格中写入实际结果
                self.dataUtils.setActualResult(row, actualResult)
            # 将字典装到列表中
            list.append(dict)
        # 对总用例个数进行赋值
        self.reportUtils.sum_case_count = count - 1
        # 执行导出报告
        self.reportUtils.export_report(list)

# Permission denied: '../data/fangjingdong.xls' 当打开测试用例文档的时候 拒绝访问
if __name__ == '__main__':
    unittest.main()