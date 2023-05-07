 #!/usr/bin/env python3

from rearrange_names import  rearrange
import unittest 

class Test_Rearrrange(unittest.TestCase):
    def test_rerrange(self):
        testcase="walter, white"
        expected="white walter"
        self.assertEqual(rearrange(testcase),expected)
        
    def test_emtpy(self):    
        testcase=""
        expected=""
        self.assertEqual(rearrange(testcase),expected)

    def test_double_name(self):
        testcase="jamaica, G butler."
        expected="G butler. jamaica"
        self.assertEqual(rearrange(testcase),expected)

    def test_one_name(self):
        testcase="jamaica."
        expected="jamaica."
        self.assertEqual(rearrange(testcase),expected)

unittest.main()



