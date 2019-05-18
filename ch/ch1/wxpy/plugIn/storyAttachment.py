# !/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import sys
from wxpy import ResponseError

sys.path.append("helper")
from restHelper import RestTemplate
from fileHelper import FileHelper


class StoryAttachment():
    def __init__(self, storyId, chat):
        self.storyId = storyId
        self.chat = chat
        self.restTemplate = RestTemplate()
        self.fileHelper = FileHelper()
        self.attachmentApi = "http://tracker.paas.cmbchina.cn/tracker/attachment/queryAttachFile?referenceId=" + storyId + "&type=story"
        # self.attachmentApi = "http://localhost:3000/tracker/attachment/queryAttachFile?referenceId=" + storyId + "&type=story"

    def start(self):
        try:
            response = self.restTemplate.getCmbTracker(self.attachmentApi)
            attachments = json.loads(response.content)["list"]
        except Exception as e:
            print e.message
            self.chat.send(u'对不起，卡号' + self.storyId + u'错误，请核对后再试')
        else:
            if not attachments:
                self.chat.send(u'对不起，卡号' + self.storyId + u'暂无UI附件')
                return
            self.chat.send(u'卡号' + self.storyId + u'UI附件即将发送，注意查收！')
            for item in attachments:
                self.send(item)

    def send(self, attachment):
        try:
            path = self.fileHelper.download(attachment["url"],
                                            self.fileHelper.generate_file_path(attachment["fileName"]))
            content = '@' + self.fileHelper.wx_file_type(path) + '@' + path;
        except Exception as e:
            print e.message
            self.chat.send(u'附件获取出错')
        else:
            try:
                self.chat.send(content)
            except ResponseError as e:
                print(e.err_code, e.err_msg)
                self.chat.send(content)
            finally:
                self.fileHelper.delete(path)
