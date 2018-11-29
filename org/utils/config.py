# coding=utf-8
import os
from configparser import ConfigParser


class Config:
    CNF_PATH = "auto.ini"
    conf: ConfigParser = None

    def __init__(self):

        curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.conf = ConfigParser()
        self.conf.read(curr_dir + os.sep + ".." + os.sep + ".." + os.sep + Config.CNF_PATH)

    def get(self, sections, key):
        return self.conf.get(sections, key)

    def get_android(self, key):
        return self.get('android', key)
