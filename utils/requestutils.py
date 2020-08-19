import requests


class RequestUtils(object):
    # 执行get请求
    def __doGet(self, url, params, headers=None):
        result = None
        if headers == None:
            result = requests.get(url, params=params).json()
        else:
            result = requests.get(url, params=params, headers=headers).json()
        return result

    # 执行post请求
    def __doPost(self, url, data, headers=None):
        #判断是否有请求头
        result = None
        if headers == None:
            result = requests.post(url, data=data).json()
        else:
            result = requests.post(url, data=data, headers=headers).json()
        return result
    #执行外界调用
    def doRequest(self, url, method, data, headers):
        if method == "GET":
            return self.__doGet(url, params=data, headers=headers)
        elif method == "POST":
            return self.__doPost(url, data=data, headers=headers)
        else:
            raise Exception("没有声明请求方式，请在接口用例中声明")

