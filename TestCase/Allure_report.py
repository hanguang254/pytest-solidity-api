import os
import pytest

file_name= "OW_test.py"
# 获取绝对路径
current_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.dirname(current_path)
json_report_path = os.path.join(project_path, 'logout', 'json')
html_report_path = os.path.join(project_path, 'logout', 'html')

os.makedirs(json_report_path, exist_ok=True)
os.makedirs(html_report_path, exist_ok=True)
# 执行测试用例生成测试报告与打开测试报告
pytest.main(["-sv", "--alluredir=%s" % json_report_path, "--clean-alluredir", f"{file_name}"])     #测试用例文件
os.system("allure generate --clean %s -o %s" % (json_report_path, html_report_path))
os.system(f'allure open "{html_report_path}"')

