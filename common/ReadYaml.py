'''
@Project ：pytest-API-Project 
@File ：ReadYaml.py
@Author ：le
@Date ：2022/8/19 10:33 
'''
import json
from string import Template
import yaml
import jsonpath


class ReadYaml():

    # #必须要一个参数  文件
    # def __init__(self,filename):
    #     self.filename=filename


    def red_yaml(self,filepath):
        """
        读取全部API
        进行数据处理
        """
        with open(filepath,'r',encoding='utf-8')as f:
            data=yaml.load(stream=f,Loader=yaml.FullLoader)
        return data

    def writer_yaml(self,filepath,data):
        # filepath写入绝对路径
        # data写入数据
        try:
            with open(filepath, "w", encoding="utf-8") as f:  # w是将文件数据清除后重新写入  a是内容追加写入
                yaml.dump(data=data, stream=f, allow_unicode=True)  # 单组数据写入,也可以批量写入
                # 批量写入 docments=[data1,data2]
                # print("数据已保存至token.yaml文件中")
        except Exception as e:
            print("写入数据错误，原因如下：{}".format(e))

    def template_yaml(self,filepath,data):
        """
        替换请求头
        :param filepath: 读取用例文件地址
        :param data: 替换的数据（比如token值）
        :return result:替换完的返回值
        目前是只有 token值替换还需更新维护
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            re = Template(f.read()).safe_substitute({'headers': data})
            # 转换格式
            result = yaml.safe_load(re)
        return result


    """
    使用参数直接调用下面方法
    只要yaml文件格式不变
    下列函数就无需修改
    """

    def get_name(self,data):
        try:
            # 请求地址
            if jsonpath.jsonpath(data,'$..name'):
                name=data['requests']['name']
            return name
        except Exception:
            print('错误：{}'.format(Exception))

    def get_url(self,data):
        try:
            #获取请求地址url
            if jsonpath.jsonpath(data,'$..url'):
                url=data['requests']['url']
            return url
        except Exception:
            print('错误：{}'.format(Exception))

    def get_method(self,data):
        try:
            #获取请求方式
            if jsonpath.jsonpath(data,'$..method'):
                method=data['requests']['method']
            return method
        except Exception:
            print('错误：{}'.format(Exception))


    def get_headers(self,data):
        try:
            #获取headers头部信息
            if jsonpath.jsonpath(data,'$..headers'):
                headers=data['requests']['headers']
            return headers
        except Exception:
            print('错误：{}'.format(Exception))


    def get_data(self,data):
        try:
            #提取请求参数
            if jsonpath.jsonpath(data,'$..data'):
                result=data['requests']['data']
            return result
        except Exception:
            print('错误：{}'.format(Exception))


    def get_expected(self,data):
        try:
            # 预期结果
            if jsonpath.jsonpath(data, '$..expected'):
                result = data['requests']['expected']
            return result
        except Exception:
            print('错误：{}'.format(Exception))





if __name__ == '__main__':

    res = ReadYaml().template_yaml('../data/CdkApi.yaml','X-token:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOiIxNjYzNzcyMTM3IiwiaWF0IjoiMTY2Mzc0MzMzNyIsInV1aWQiOiJhNWFmYzZmOC05YjlmLTQyMTQtYTFjOS1jZTVlOTg3ZWE0OGUifQ.dkH53sCYYBiYuzNq1Li0n0FHXQtrOgHVe7sM71p2-7c')
    print(res)
