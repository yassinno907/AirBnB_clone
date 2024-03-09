#!/usr/bin/python3

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    def create(self):
        return HBNBCommand()

    def test_quit(self):
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
