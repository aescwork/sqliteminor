import sys
import unittest
sys.path.append("..//")
import somemodule as sm


class InstantiationTest(unittest.TestCase):

	def setUp(self):
		self.s= sm.SomeModule("")


	def testMemberResult(self):
		self.assertEqual(self.s.result, "NONE")
			

	def testMemberStatus(self):
		self.assertEqual(self.s.status, "NONE")

	
	def tearDown(self):
		self.s.__del__()

if __name__ == '__main__':

	unittest.main()
