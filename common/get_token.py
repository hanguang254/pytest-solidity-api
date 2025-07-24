
import jsonpath
from common import ReadYaml
from common import RequestsUitl


class login_Token():

    """
    :param data: yaml文件读取值

    """
    def get_token(self,data):
        """
        :param data: 读取的用例参数
        :return: 返回token值
        """
        try:
            method=ReadYaml.ReadYaml().get_method(data)      #请求方法
            url=ReadYaml.ReadYaml().get_url(data)            #请求地址
            get_data=ReadYaml.ReadYaml().get_data(data)      #请求参数
            # json格式响应
            result = RequestsUitl.RequestsUitl().requests_send(method=method,url=url,data=get_data).json()
            #通过jsonpath搜索键值对
            if jsonpath.jsonpath(result,'$..token') :
                #token值
                r=result['data']['token']
                token = {'X-token':r} #{直接引用到头部请求  # header}
                # print(token)
                #将token写入yaml文件
                ReadYaml.ReadYaml().writer_yaml('../data/token.yaml',{'X-token':r})
                return token
            else:
                print("无token值！")

        except Exception as e:
            print('错误原因：',e)

    def template_token(self,filepath,apifilepath):
        """
        这个方法每个用例都会执行一次
        替换token值
        :param filepath: 登录用例文件地址
        :param apifilepath: 测试接口用例文件地址
        :return: 返回替换好的用例
        """
        #读取登录参数
        data = ReadYaml.ReadYaml().red_yaml(filepath)
        #获取最新的token
        token = login_Token().get_token(data)
        #替换headers的token值
        all_api = ReadYaml.ReadYaml().template_yaml(apifilepath,token)

        return all_api


if __name__ == '__main__':
    # api = ReadYaml.ReadYaml().red_yaml('../data/Alogin.yaml')
    # print(api)
    # res = login_Token().get_token(api)
    # print(res)

    #temlate_token 使用
    res = login_Token().template_token('../data/Alogin.yaml','../data/CdkApi.yaml')
    print(res)