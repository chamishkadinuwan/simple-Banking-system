import bankapp
import unittest
class testapplication(unittest.Testcase):
    def test_one(self) :
        a = bankapp.loan_cal()
        self.assertEqual(a,20138.8888888889)