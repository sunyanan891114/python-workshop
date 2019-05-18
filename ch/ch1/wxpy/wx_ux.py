#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import requests
import re
import json
from wxpy import *

sys.path.append("plugIn")
sys.path.append("helper")

from storyAttachment import StoryAttachment

bot = Bot(console_qr=True, cache_path=True)

workshop = bot.chats().search(u'Workshop 额靠重意雷')[0]
print workshop


@bot.register(workshop)
def print_others(msg):
    print msg.text
    if re.match('^UI\d{6}$', msg.text):
        StoryAttachment(re.sub('UI', "", msg.text), msg.chat).start()
    elif msg.is_at:
        txt = msg.text + ""
        return auto_reply(txt.replace(u"@小鸡", ""))


# 调用青人客机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    result = json.loads(
        requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + text).content
    )
    return result["content"].replace("{br}", "\r\n")


print bot.groups()

if __name__ == "__main__":
    embed()
