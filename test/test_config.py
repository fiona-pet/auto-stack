# coding=utf-8
import unittest

from org.utils.config import Config


class TestConfig(unittest.TestCase):
    def test_get(self):
        config = Config()
        print(config.get('android', 'platformName'))
        # self.assertEquals(config.get('android', 'platformName'), 'True')
