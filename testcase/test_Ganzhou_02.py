# coding:utf-8

import pytest
from common.basepage import Browser_engine
from common.log import Log
from pages import Ganzhou_pages_01
import sys
import time
from config import datas_path
from common.get_parameter import Data
from common.basepage import Retry


class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b


