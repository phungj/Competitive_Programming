import unittest

from os import listdir
from os.path import isfile, join
from .G_Transportation import main

class TestMain(unittest.TestCase):
    def working_tests(self):
        for file in [f for f in listdir(".\\Kattis\\2021\\Week_6\\G\\tests\\working") if isfile(join(".\\Kattis\\2021\\Week_6\\G\\tests\\working", f))]:
            pass