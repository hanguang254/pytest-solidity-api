'''
@Project ：pytest-API-Project 
@File ：conftest.py
@Author ：le
@Date ：2022/8/23 10:18 
'''
import pytest
from common import get_token
from common import ReadYaml
from data.get_local import get_yaml_path

"""
conftest.py文件中Fixture的scope参数为session，那么所有的测试文件执行前（后）执行一次conftest.py文件中的Fixture。
conftest.py文件中Fixture的scope参数为module，那么每一个测试文件执行前（后）都会执行一次conftest.py文件中Fixture。
conftest.py文件中Fixture的scope参数为class，那么每一个测试文件中的测试类执行前（后）都会执行一次conftest.py文件中Fixture。
conftest.py文件中Fixture的scope参数为function，那么所有文件的测试用例执行前（后）都会执行一次conftest.py文件中Fixture。
"""
@pytest.fixture(scope='session')
def login_token():
    yamlpath = get_yaml_path("Alogin.yaml")
    data  = ReadYaml.ReadYaml().red_yaml(yamlpath)
    # print(data)
    token = get_token.login_Token().get_token(data)

    yield token




if __name__ == '__main__':
    # login_token
    # print(s)
    pass