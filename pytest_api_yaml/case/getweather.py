# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 3:31 PM
# @Author  : junbo.zhao
# @File    : getweather.py
import pytest
import requests


class Testweather:
    def test_weather_sh(self):
        r = requests.get('http://www.weather.com.cn/data/sk/101020100.html')
        # print(r.content.decode('utf-8'))
        r.encoding = 'utf-8'
        print("城市:", r.json())
        city = r.json()['weatherinfo']['city']
        temp = r.json()['weatherinfo']['temp']
        WD = r.json()['weatherinfo']['WD']
        WS = r.json()['weatherinfo']['WS']
        SD = r.json()['weatherinfo']['SD']
        AP = r.json()['weatherinfo']['AP']
        njd = r.json()['weatherinfo']['njd']
        WSE = r.json()['weatherinfo']['WSE']
        time = r.json()['weatherinfo']['time']
        sm = r.json()['weatherinfo']['sm']
        isRadar = r.json()['weatherinfo']['isRadar']
        print("城市:", r.json()['weatherinfo']['city'], "风向:", r.json()['weatherinfo']['WD'], "温度：",
              r.json()['weatherinfo']['temp'])

    @pytest.mark.skip(reason='跳过')
    def test_weather_gz(self):
        r = requests.get('http://www.weather.com.cn/data/sk/101280101.html')
        # print(r.content.decode('utf-8'))
        r.encoding = 'utf-8'  # 将编码格式转为utf-8
        print("城市:", r.json()['weatherinfo']['city'], "风向:", r.json()['weatherinfo']['WD'], "温度：",
              r.json()['weatherinfo']['temp'])
