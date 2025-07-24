'''
@Project ：pytest-API-Project 
@File ：RequestsUitl.py
@Author ：le
@Date ：2022/8/19 9:43 
'''
import requests
from common import ReadYaml


class RequestsUitl:
    """
    封装请求方法
    """
    def __init__(self):
        self.session=requests.session()


    def requests_send(self,method,url,data,**kwargs):
        """
        :param method:请求方法
        :param url: 请求地址
        :param data: 请求数据
        :param kwargs: 多余参数
        :return: 返回响应值
        """
        method = method.upper()  #请求方法大写
        try:

            if method == 'GET':
                response = self.session.request(method=method,url=url,data=data,**kwargs)

            elif method == 'POST':
                response =self.session.request(method=method,url=url,json=data,**kwargs)

            #请求方法接着下面更新
            elif method == 'DELETE':
                response =self.session.request(method=method,url=url,data=data,**kwargs)

            elif method == 'PUT':
                response = self.session.request(method=method, url=url,data=data,**kwargs)

            else:
                 print('无此请求方法，请写入方法函数')

            return response

        except Exception as e:
            print('错误：{}'.format(e))



if __name__ == '__main__':
    data = ReadYaml.ReadYaml().red_yaml('../data/Alogin.yaml')
    # # print(data)
    #
    # method = ReadYaml.ReadYaml().get_method(data)
    # print('请求方法：',method)
    # url = ReadYaml.ReadYaml().get_url(data)
    # print('请求地址：',url)
    # get_data=ReadYaml.ReadYaml().get_data(data)
    # print('请求参数：',get_data)
    # res = RequestsUitl().requests_send(method=method,url=url,data=get_data)
    # print(res.json())