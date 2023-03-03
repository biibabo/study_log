# -*- coding: utf-8 -*-
# @Time    : 2023/2/2 6:21 PM
# @Author  : junbo.zhao
# @File    : read_yaml.py
import yaml


class yamlUtil:
    def __init__(self, yaml_path):
        """
        通过init把文件传入到这个类
        :param yaml_path:
        """
        self.yaml_path = yaml_path

    # 读取ymal文件
    def read_yaml(self):
        """
        读取yaml，将yaml反序列化，就是把我们yaml格式转换成dict格式
        :return:
        """
        with open(self.yaml_path, 'r', encoding="utf-8", errors='ignore') as f:
            value = yaml.load(f.read(), Loader=yaml.FullLoader)  # 文件流，加载方式
        return value
