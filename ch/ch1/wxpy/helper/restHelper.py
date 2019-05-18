#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests


class RestTemplate():

    def postCmbTracker(self, url):
        return requests.post(url,
                             headers={
                                 'Accept': 'application/json, text/plain, */*',
                                 'Referer': 'http://devops.paas.cmbchina.cn/',
                                 'Origin': 'http://devops.paas.cmbchina.cn',
                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
                             })

    def getCmbTracker(self, url):
        return requests.get(url,
                            headers={
                                'Accept': 'application/json, text/plain, */*',
                                'Referer': 'http://devops.paas.cmbchina.cn/',
                                'Origin': 'http://devops.paas.cmbchina.cn',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
                            })
