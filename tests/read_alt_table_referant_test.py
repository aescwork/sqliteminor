# -*- coding: utf-8 -*-

import unittest
import os
import sys
sys.path.append("../sqliteminor/")
import sqliteminor 


class ASampleTest(unittest.TestCase):

	def setUp(self):
		path_to_db = "../fixtures/sqlm_test.db"
		self.sm = SQLiteMinor(path_to_db)


	def test_some_method(self):

		self.assertEqual(someval, compval)	

	def test_result(self):
		self.assertEqual(self.sm.result, "OK")


	def tearDown(self):

		self.sm.__del__()


if __name__ == '__main__':
	unittest.main()
