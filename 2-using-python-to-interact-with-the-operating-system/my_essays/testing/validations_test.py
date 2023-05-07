#!/usr/bin/env python3



from validations import validate_user
import unittest

class TestValidate_User(unittest.TestCase):

	def test_valid(self):
		username='stephane'
		minlen=5
		self.assertEqual(validate_user(username,minlen),True)
		
	def test_too_short(self):
		username='stev'
		minlen=5
		self.assertEqual(validate_user(username,minlen),False)

	def test_invalid_chars(self):
		username='invalid_user'
		minlen=1
		self.assertEqual(validate_user(username,minlen),False)
		
	def test_invalid_minlen(self):
		username='invalid_user'
		minlen=-1
		self.assertRaises(ValueError,validate_user,username,minlen)
		
unittest.main()


