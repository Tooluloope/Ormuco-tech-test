import unittest
from Overlap import if_overlap


class TestsForOverLap(unittest.TestCase):

  def test_OverLap_1(self):
        result = if_overlap((1, 5), (2, 6))
        self.assertEqual(result, True)

  def test_OverLap_2(self):
      result = if_overlap((3, 5), (16, 1))
      self.assertEqual(result, True)

  def test_OverLap_3(self):
      result = if_overlap((-2, -7), (-2, -7))
      self.assertEqual(result, True)

  def test_OverLap_4(self):
      result = if_overlap((-1, 4), (0, 0))
      self.assertEqual(result, False)

  def test_OverLap_5(self):
      result = if_overlap((-1, -2), (0, -2))
      self.assertEqual(result, True)

  def test_OverLap_6(self):
      result = if_overlap((0, 0), (0, 0))
      self.assertEqual(result, True)

  def test_OverLap_7(self):
      result = if_overlap((1, 1), (1, 1))
      self.assertEqual(result, True)

  def test_OverLap_8(self):
    result = if_overlap((-1, 0), (-2, -3))
    self.assertEqual(result, False)


unittest.main()