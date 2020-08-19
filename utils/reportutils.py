import time


class ReportUtils:
    # 定义总用例个数
    sum_case_count = 0
    # 定义通过的用例个数
    pass_case_count = 0

    # 导出一个测试报告...list是列表,是结果数据的列表
    def export_report(self, list):
        # 打开文件
        filename = time.strftime("%Y%m%d%H%M%S", time.localtime())+".html"
        stream = open(file=filename, mode="w", encoding="UTF-8")
        stream.write(
            '<!DOCTYPE html><html><head><meta charset="UTF-8">'
            '<title></title></head><body><table border="1" cellpadding="10"  align="center" '
            'bgcolor="aquamarine"><caption ><h2>自动化接口测试报告</h2></caption><tr>'
            '<th>用例编号</th><th >'
            '用例名称</th><th>url地址</th><th>是否通过</th></tr>')

        for case in list:
            # 获取编号id信息
            id = case["id"]
            # 获取用例名称
            name = case["name"]
            # 获取url地址
            url = case["url"]
            # 是否通过
            is_pass = case["is_pass"]
            is_pass_str = None
            if is_pass == True:
                is_pass_str = "通过"
            else:
                is_pass_str = "不通过"

            stream.write('<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>' % (id, name, url, is_pass_str))

        stream.write(
            '<tr><th colspan="2">总结</th><th colspan="2">'
            '<font color="red">总用例个数:%d个 通过了%d个</font>'
            '</th></tr></table></body></html>' % (
                self.sum_case_count,self.pass_case_count))
