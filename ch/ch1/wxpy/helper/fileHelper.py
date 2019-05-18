#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import os
import uuid
import filetype


class FileHelper():
    def download(self, url, path):
        attachment = requests.get(url)
        fh = open(path, 'wb')
        try:
            fh.write(attachment.content)
            return path
        except IOError:
            print u'存储文件时出错'
        finally:
            fh.close()

    def delete(self, path):
        os.remove(path)

    def file_extension(self, path):
        return os.path.splitext(path)[1]

    def wx_file_type(self, path):
        if filetype.image(str(path)) is not None:
            return 'img'
        if filetype.video(str(path)) is not None:
            return 'vid'
        return 'fil'

    def generate_file_path(self, filename):
        newname = str(uuid.uuid1()) + self.file_extension(filename)
        img_dir = os.path.abspath(os.path.join(os.getcwd(), "../wxpy/images"))
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
        return img_dir + '/' + newname
