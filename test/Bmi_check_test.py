import unittest

from src.Bmi import BMI


class MyTestCase(unittest.TestCase):
    def test_bmi_check(self):
        # stub
        bmi1 = 10
        bmi2 = 22
        bmi3 = 30

        # assume
        expected1 = "Under weight"
        expected2 = "Valid mass"
        expected3 = "Obese"

        # action
        result1 = BMI.bmi_check(bmi1)
        result2 = BMI.bmi_check(bmi2)
        result3 = BMI.bmi_check(bmi3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)

    def test_invalid_bmi(self):
        # stub
        bmi1 = 0
        bmi2 = -10
        bmi3 = -25.5

        # assume
        expected1 = "Invalid bmi"
        expected2 = "Invalid bmi"
        expected3 = "Invalid bmi"

        # action
        result1 = BMI.bmi_check(bmi1)
        result2 = BMI.bmi_check(bmi2)
        result3 = BMI.bmi_check(bmi3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)

    def test_invalid_type_bmi(self):
        # stub
        bmi1 = 'abc'
        bmi2 = '@'
        bmi3 = {1: 2, 3: 4}
        bmi4 = (1, 2)

        # assume
        expected1 = "Invalid Input"
        expected2 = "Invalid Input"
        expected3 = "Invalid Input"
        expected4 = "Invalid Input"

        # action
        result1 = BMI.bmi_check(bmi1)
        result2 = BMI.bmi_check(bmi2)
        result3 = BMI.bmi_check(bmi3)
        result4 = BMI.bmi_check(bmi4)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)


if __name__ == '__main__':
    unittest.main()
