#!/usr/bin/env python3



from rearrange_names import rearrange
import unittest


class TestRearrange(unittest.TestCase):
	def test_basic(self):
		testcase="lovelace, ada"
		expected="ada lovelace"
		self.assertEqual(rearrange(testcase),expected)

	def test_empty(self):
		testcase=""
		expected=""
		self.assertEqual(rearrange(testcase),expected) 

	def test_double(self):
		testcase="likelife, nonsense me."
		expected="nonsense me. likelife"
		self.assertEqual(rearrange(testcase),expected)

	def test_one_name(self):
		testcase="Julian"
		expected="Julian"
		self.assertEqual(rearrange(testcase),expected)

	def test_raises_error(self):
		testcase="Julian"
		expected="False"
		self.assertRaise(ValueError,rearrange(testcase),expected)


unittest.main()
		
