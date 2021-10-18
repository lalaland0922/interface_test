"""
@Time : 2021/7/17 21:45
@Author : ruslan
@Email : ruslan@163.com
@File : run.py
@Project : jrj_webAutoTest_26
@feature : 
@实现步骤：
"""
import pytest
import os
from common.bases.get_config import cf
test_result_dir = cf.json_dir_path
test_report_dir = cf.html_dir_path


if __name__ == '__main__':
    args = ['-s', '-q', '--alluredir', test_result_dir]
    pytest.main(args)
    cmd = 'allure generate %s -o %s -c' % (test_result_dir, test_report_dir)
    os.system(cmd)