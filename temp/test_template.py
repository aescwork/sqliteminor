# -*- coding: utf-8 -*-

import unittest
import sqlite3
import sys

sys.path.append("../sqliteminor/")
sys.path.append("../temp/")

import sqliteminor 
import setup_db


class ASampleTest(unittest.TestCase):

	def setUp(self):
		
		conn = setup_db.setup_db()
		self.sm = sqliteminor.SQLiteMinor(self.conn, table_name)


	def test_some_method(self):

		self.assertEqual(someval, compval)	

	def test_result(self):
		self.assertEqual(self.sm.result, "OK")


	def tearDown(self):

		self.sm.__del__()


if __name__ == '__main__':
	unittest.main()








