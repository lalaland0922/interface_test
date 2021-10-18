"""
@Time : 2021/7/20 21:06
@Author : ruslan
@Email : ruslan@163.com
@File : get_config.py
@Project : jrj_webAutoTest_26
@feature : 读取配置文件
@实现步骤：
"""
import os
import configparser
import sys


BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
config_file_path = os.path.abspath(os.path.join(BASE_DIR, 'common/config/config.ini'))


class Config:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.img_dir_path = self.read_config('img', 'img_dir_path')
        self.json_dir_path = self.read_config('report', 'json_dir_path')
        self.html_dir_path = self.read_config('report', 'html_dir_path')
        self.get_event_list_path = self.read_config('yaml', 'get_event_list_path')
        self.address = self.read_config('server', 'address')

    def read_config(self, field, key):
        try:
            self.cf.read(config_file_path, encoding='utf-8')
            result = self.cf.get(field, key).replace('base_dir', str(BASE_DIR))
            if ':' in result:
                result = result.replace('/', '\\')
        except Exception as e:
            print(e)
            sys.exit(1)
        return result


cf = Config()

if __name__ == '__main__':
    cf = Config()
    print('img_path: ', cf.img_dir_path)
    print('json_dir_path: ', cf.json_dir_path)
    print('html_dir_path: ', cf.html_dir_path)
    print('event yaml path: ', cf.get_event_list_path)
    print('address: ', cf.address)