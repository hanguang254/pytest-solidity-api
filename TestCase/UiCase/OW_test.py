'''
@Project  ：pytest-solidity-api 
@File     ：OW_test
@Author   ：le
@Date     ：2025/8/25 11:32
'''
import shutil
import subprocess
from time import sleep
# 导入selenium的web驱动
from selenium import webdriver
# 导入selenium的chrome服务
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

# 导入驱动管理的chrome管理
from webdriver_manager.chrome import ChromeDriverManager
import os
import pytest
from dotenv import load_dotenv
from common.Logger import Log
from common.ReadYaml import ReadYaml
from common.rpc_account import RpcConnect
import allure
from data.get_local import get_yaml_path


# 读取用例
yaml_path= get_yaml_path("contractApi.yaml")
data = ReadYaml().red_yaml(yaml_path)

class Test_OW:

    def setup_method(self, method):
        class_name = self.__class__.__name__        # Test_add
        method_name = method.__name__               # test_one
        file = os.path.basename(__file__)
        log = Log(file, suffix=f"{class_name}_{method_name}")
        self.logger = log.Logger()
        self.logger.info(f"开始执行用例：{class_name}.{method_name}")

        # 获取chrome驱动
        self.logger.info("启动浏览器驱动")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10) #隐性等待
        self.driver.get("https://xone.org/")
        self.driver.maximize_window() #放大窗口
        sleep(3)


    def teardown_method(self, method):
        self.logger.info("用例执行结束")
        # 关闭浏览器
        self.driver.quit()

    @allure.story("用例一")
    def test_one(self):
        try:
            Button  = self.driver.find_element("xpath",'//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/button')
            #获取按钮文案
            value = Button.text.strip()
            assert value == "Start buildin" ,self.logger.error(f"断言错误实际值为{value}")
        except AssertionError:
            # 把断言错误重新抛出，pytest 会判定为 FAIL
            raise
        except Exception as e:
            # 全部错误日志
            self.logger.exception(e)
            raise
    @allure.story("用例二")
    def test_two(self):
        self.logger.info("用例二")

