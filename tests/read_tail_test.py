# -*- coding: utf-8 -*-

import unittest
import sqlite3
import sys

sys.path.append("../sqliteminor/")
sys.path.append("../temp/")

import sqliteminor 
import setup_db



class ReadTailTest(unittest.TestCase):

	def setUp(self):

		self.conn = setup_db.setup_db()

		self.read_tail_comp = [(13, u'Alder Buckthorn'), (14, u'Common Hawthorn'), (15, u'Common Hazel'), (16, u'Midland Hawthorn'), \
								(17, u'Redwood (Cupressaceae)'), (18, u'Guelder Rose')]

		self.sm = sqliteminor.SQLiteMinor(self.conn, "trees")
		self.read_tail_result = self.sm.read_tail(6, "tree_id", "tree_id, name")

	def test_some_method(self):

		self.assertEqual(self.read_tail_result, self.read_tail_comp)	

	def test_result(self):
		self.assertEqual(self.sm.result, "OK")


	def tearDown(self):

		self.sm.__del__()


if __name__ == '__main__':
	unittest.main()








