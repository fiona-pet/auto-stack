# coding=utf-8
import unittest

from org.utils.config import Config


class TestConfig(unittest.TestCase):
    config: Config = Config()

    def test_get(self):
        self.assertEquals(self.config.get('android', 'platformName'), 'Android')

    def test_get_android(self):
        self.assertEquals(self.config.get_android('platformName'), 'Android')
