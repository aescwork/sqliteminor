# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append("../sqliteminor/")
sys.path.append("../temp/")

import sqliteminor
import setup_db

class ReadHeadTest(unittest.TestCase):

	def setUp(self):

		self.conn = setup_db.setup_db()

		self.read_head_comp = [(1, u'Ash'), (2, u'Yew'), (3, u'White Pine'), (4, u'Scots Pine'), (5, u'Elm'), (6, u'Sugar Maple')]
		self.sm = sqliteminor.SQLiteMinor(self.conn, "trees")
		self.read_head_output = self.sm.read_head(6, "tree_id, name")
		

	def test_read_head(self):

		self.assertEqual(self.read_head_output, self.read_head_comp)	


	def test_result(self):
		self.assertEqual(self.sm.result, "OK")


	def tearDown(self):

		self.sm.__del__()
		del(self.conn)

if __name__ == '__main__':
	unittest.main()










