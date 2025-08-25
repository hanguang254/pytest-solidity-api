'''
@Project  ：pytest-solidity-api 
@File     ：OW_test
@Author   ：le
@Date     ：2025/8/25 11:32
'''
from time import sleep

# 导入selenium的web驱动
from selenium import webdriver
# 导入selenium的chrome服务
from selenium.webdriver.chrome.service import Service

# 导入驱动管理的chrome管理
from webdriver_manager.chrome import ChromeDriverManager
import os
import pytest
from dotenv import load_dotenv
from common.Logger import Log
from common.ReadYaml import ReadYaml
from common.rpc_account import RpcConnect

data = ReadYaml().red_yaml("../data/contractApi.yaml")

class Test_OW:

    def setup_method(self, method):
        class_name = self.__class__.__name__        # Test_add
        method_name = method.__name__               # test_one
        file = os.path.basename(__file__)
        log = Log(file, suffix=f"{class_name}_{method_name}")
        self.logger = log.Logger()
        self.logger.info(f"开始执行用例：{class_name}.{method_name}")

        # 获取chrome驱动
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.baidu.com")

    def teardown_method(self, method):
        self.logger.info("用例执行结束")
        # 关闭浏览器
        self.driver.quit()



    def test_OW(self):
        try:
            pass

        except Exception as e:
            # 全部错误日志
            self.logger.exception(e)



if __name__ == '__main__':
    pytest.main(['Test_bridgeToken.py', '-qsv'])