'''
@Project  ：pytest-solidity-api 
@File     ：test_stats
@Author   ：le
@Date     ：2025/9/1 17:57
'''
import os

import pytest
from dotenv import load_dotenv
from pywin32_testutil import find_test_fixture

from common.Logger import Log
from common.ReadYaml import ReadYaml
from common.RequestsUitl import RequestsUitl
from common.rpc_account import RpcConnect
from data.get_local import get_yaml_path

# 读取用例
yaml_path= get_yaml_path("stats.yaml")
data = ReadYaml().red_yaml(yaml_path)

class Test_stats:

    def setup_method(self, method):
        class_name = self.__class__.__name__        # Test_add
        method_name = method.__name__               # test_one
        file = os.path.basename(__file__)
        log = Log(file, suffix=f"{class_name}_{method_name}")
        self.logger = log.Logger()
        self.logger.info(f"开始执行用例：{class_name}.{method_name}")

    def teardown_method(self, method):
        self.logger.info("用例执行结束")



    @pytest.mark.parametrize('value',data)
    def test_stats(self,value):
        try:
            self.logger.info(value)
            url = ReadYaml().get_url(value)
            method = ReadYaml().get_method(value)
            expected = ReadYaml().get_expected(value)['code']
            data = ReadYaml().get_data(value)
            # print(url,method,expected)
            res = RequestsUitl().requests_send(url=url,method=method,data={}).json()
            # print(res)
            assert expected == ReadYaml().find_value(res,"code"),self.logger.exception("不符合预期")
            self.logger.info("用例通过测试")
        except AssertionError as a:
            self.logger.exception(a)
            raise
        except Exception as e:
            # 全部错误日志
            self.logger.exception(e)
            raise