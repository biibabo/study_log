# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 7:32 PM
# @Author  : junbo.zhao
# @File    : createvm.py
import datetime
import pytest
import requests
from requests import Timeout

from pytest_api_yaml.case.test.read_yaml import yamlUtil
from pytest_api_yaml.config.conf import *

vm_path = "//pytest_api_yaml-1/case/vm/ucloudvm.yaml"

lists = []


class TestCreatevm:

    @pytest.mark.parametrize('datas1', yamlUtil(vm_path).read_yaml())
    # 创建ucloud云主机
    # @pytest.mark.skip(reason='跳过')
    def test_01_WorkflowCreateVM(self, datas1, test_testcookie):
        url = test_url
        data = datas1['test_createavm']['json']
        headers = {'Referer': test_Referer,
                   'Origin': test_Origin,
                   "Cookie": test_testcookie}

        r = requests.post(url=url, json=data, headers=headers)
        print(r.json())
        SerialNum = r.json()["Data"]["SerialNum"]
        lists.append(SerialNum)
        print(lists)
        print(globals()["lists"])

    # 获取云主机状态
    # @pytest.mark.skip(reason='跳过')
    # @func_set_timeout(60)
    def test_GetWorkflowInstProcess(self, test_testcookie):
        for i in lists:
            url = test_url
            data = {"SerialNum": i}
            headers = {'Referer': test_Referer,
                       'Origin': test_Origin,
                       "Cookie": test_testcookie}
            # r = requests.post(url=url, json=data, headers=headers)
            # print(r.json())
            try:
                start_time = datetime.datetime.now()
                timeout = 40
                while True:
                    r = requests.post(url=url, json=data, headers=headers, timeout=30)
                    NodeStatus = r.json()["Data"]["Nodes"][-1]["NodeStatus"]
                    NodeKey = r.json()["Data"]["Nodes"][-1]["NodeKey"]
                    NodeKeys = (
                        '14544yw', '1sbo0c7', '1ctt07k', '1q3a3x9', '01nfd8n')
                    if r.json()["Data"]["Nodes"] == []:
                        print("流程加载中")
                    elif NodeStatus == 2 and NodeKey in NodeKeys:
                        print("\n云主机创建成功")
                        break
                    elif (datetime.datetime.now() - start_time).seconds > timeout:
                        raise Timeout
                    else:
                        print('创建中')
            except:
                raise BaseException
            print("当前创建云主机流程状态为：", r.json()["Data"]["Nodes"][-1]["NodeTitle"])
            cmpUuids = r.json()["Data"]["Nodes"][-1]["Context"]["CreateVMResponse"]["ResourceIds"]
            globals()['cmpUuids'] = cmpUuids
            print(globals()['cmpUuids'])

































