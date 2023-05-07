# coding:utf-8
import os
import pytest

current_path = os.path.dirname(os.path.abspath(__file__))  # 当前路径(使用 abspath 方法可通过dos窗口执行)
json_report_path = os.path.join(current_path, '../report/json')  # json报告路径
html_report_path = os.path.join(current_path, '../report/html')  # html报告路径
# pytest.main(['-s', 'test_00_apk.py', '-v', f'--alluredir={json_report_path}',
#              '--clean-alluredir'])  # 执行pytest下的用例并生成json文件
pytest.main(['-s', '-v', f'--alluredir={json_report_path}', '--clean-alluredir'])  # 执行pytest下的用例并生成json文件
os.system(f'allure generate {json_report_path} -o {html_report_path} --clean')  # 把json文件转成html报告
