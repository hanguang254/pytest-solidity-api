'''
@Project  ：pytest-solidity-api 
@File     ：get_local
@Author   ：le
@Date     ：2025/9/1 17:05
'''
import os


def get_yaml_path(filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    yaml_path = os.path.join(BASE_DIR, f"{filename}")
    return yaml_path

if __name__ == '__main__':
    get_yaml_path("contractApi.yaml")