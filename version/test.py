
import unittest
from compare_version import version
class TestsForStrings(unittest.TestCase):

    # -------------------TESTS for Greater Function-----------------------
    def test1_ForGreater(self):
        strings = version('1.1', '1.3')
        self.assertEqual(strings, '1.1 is less than 1.3')

    def test2_ForGreater(self):
        strings = version('-1.1', '-1.3')
        self.assertEqual(strings, '-1.1 is less than -1.3')

    def test3_ForGreater(self):
        strings = version('1.1', '0')
        self.assertTrue(strings, '1.1 is greater than 0')

    # -------------------TESTS for Lesser Function-------------------------
    def test1_ForLesser(self):
        strings = version('1.1', '1.3')
        self.assertEqual(strings, '1.1 is less than 1.3')

    def test2_ForLesser(self):
        strings = version('-1.1', '-1.3')
        self.assertEqual(strings, '-1.1 is less than -1.3')

    def test3_ForLesser(self):
        strings = version('1.1', '0')
        self.assertTrue(strings, '1.1 is less than 0')

    # ------------TESTS for Equal Function-----------------------------
    def test1_ForEqual(self):
        strings = version('1.1', '1.1')
        self.assertEqual(strings, '1.1 is equal to 1.1')

    def test2_ForEqual(self):
        strings = version('1.1', '1.1')
        self.assertEqual(strings, '1.1 is equal to 1.1')

    def test3_ForNotEqual(self):
        strings = version('0', '0.0')
        self.assertEqual(strings, '0 is equal to 0.0')


# main method
if __name__ == '__main__':
    unittest.main()