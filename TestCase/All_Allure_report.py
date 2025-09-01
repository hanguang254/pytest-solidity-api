import os
import pytest

# 获取当前脚本所在目录
current_path = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录
project_path = os.path.dirname(current_path)

# 定义 allure 报告的保存目录
json_report_path = os.path.join(project_path, 'logout', 'json')
html_report_path = os.path.join(project_path, 'logout', 'html')

# 确保目录存在
os.makedirs(json_report_path, exist_ok=True)
os.makedirs(html_report_path, exist_ok=True)

# 执行 testcase 目录下所有用例，并生成 allure 报告
pytest.main([
    "-sv",
    "--alluredir=%s" % json_report_path,
    "--clean-alluredir",
    os.path.join(project_path, "TestCase")   # 执行 testcase 下的所有用例
])

# 生成并打开 allure 报告
os.system("allure generate --clean %s -o %s" % (json_report_path, html_report_path))
os.system(f'allure open "{html_report_path}"')