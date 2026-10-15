import unittest
from grading import calculate_grade
class TestGrading(unittest.TestCase):
  def test_cases(self):
    cases =[(39,"F"),(40,"C"),(59,"C"),(60,"B"),(79,"B"),(80,"A"),(99,"A")]
    for marks,expected in cases:
      with self.subTest(marks=marks):
        self.assertEqual(calculate_grade(marks),expected)

  def test_invalid_marks(self):
    for marks in [-1,101,"abc",True]:
      with self.subTest(marks=marks):
        with self.assertRaises(ValueError):
          calculate_grade(marks)
if __name__ == "__main__":
   unittest.main()
