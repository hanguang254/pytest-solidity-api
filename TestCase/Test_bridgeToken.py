'''
@Project  ：pytest-yaml-api-template 
@File     ：Test_bridgeToken
@Author   ：le
@Date     ：2025/7/24 9:22
'''
import os

import pytest
from dotenv import load_dotenv
from common.Logger import Log
from common.ReadYaml import ReadYaml
from common.rpc_account import RpcConnect

data = ReadYaml().red_yaml("../data/contractApi.yaml")

class Test_bridgeToken:

    def setup_method(self, method):
        class_name = self.__class__.__name__        # Test_add
        method_name = method.__name__               # test_one
        file = os.path.basename(__file__)
        log = Log(file, suffix=f"{class_name}_{method_name}")
        self.logger = log.Logger()
        self.logger.info(f"开始执行用例：{class_name}.{method_name}")

        # 获取env变量
        load_dotenv()
        self.BSC_TEST_RPC = os.getenv("BSC_TEST_RPC")
        self.key = os.getenv("KEY")
        # 判断环境变量是否为空
        if not self.BSC_TEST_RPC:
            self.logger.error("环境变量 BSC_TEST_RPC 为空，跳过测试")
            pytest.skip("缺少 BSC_TEST_RPC 配置，跳过用例执行")
        if not self.key:
            self.logger.error("环境变量 KEY 为空，跳过测试")
            pytest.skip("缺少 KEY 配置，跳过用例执行")
        self.web3 = RpcConnect().connect_rpc(url=self.BSC_TEST_RPC,log=self.logger)
        self.account = RpcConnect().account(web3=self.web3,key=self.key)

    def teardown_method(self, method):
        self.logger.info("用例执行结束")

    @pytest.mark.parametrize('key',data)
    def test_one(self,key):
        try:
            self.logger.info(key)
            self.logger.info("这是 test_one 的日志")
            balance = self.web3.eth.get_balance("0x84A92C50eafA5A38c35e7123bf394695830c17D1")
            self.logger.info(f"测试地址:{self.account.address}")
            self.logger.info(f"余额:{self.web3.from_wei(balance,"ether")}")


        except Exception as e:
            # 全部错误日志
            self.logger.exception(e)



if __name__ == '__main__':
    pytest.main(['Test_bridgeToken.py', '-qsv'])