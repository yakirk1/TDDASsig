import unittest

from src.Bmi import BMI


class Bmi_test(unittest.TestCase):
    def test_invalid_type(self):
        # stub
        height1 = 'a'
        mass1 = 50

        height2 = 180
        mass2 = 'abc'

        height3 = "95"
        mass3 = True

        height4 = 100
        mass4 = 50

        # assume
        expected1 = "Invalid characters,please type only numerical characters"
        expected2 = "Invalid characters,please type only numerical characters"
        expected3 = "Invalid characters,please type only numerical characters"
        expected4 = 50

        # action
        result1 = BMI.bmi_calc(height1, mass1)
        result2 = BMI.bmi_calc(height2, mass2)
        result3 = BMI.bmi_calc(height3, mass3)
        result4 = BMI.bmi_calc(height4, mass4)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)

    def test_divided_by_zero(self):
        # stub
        height1 = 0
        mass1 = 75

        height2 = 0
        mass2 = 0

        # assume
        expected1 = "Invalid height"
        expected2 = "Invalid height"

        # action
        result1 = BMI.bmi_calc(height1, mass1)
        result2 = BMI.bmi_calc(height2, mass2)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)

    def test_invalid_values(self):
        # stub
        height1 = -10
        mass1 = 67

        height2 = 180
        mass2 = 0

        height3 = 59
        mass3 = -34

        height4 = -158
        mass4 = -5

        # assume
        expected1 = "Invalid height"
        expected2 = "Invalid mass"
        expected3 = "Invalid mass"
        expected4 = "Invalid height"

        # action
        result1 = BMI.bmi_calc(height1, mass1)
        result2 = BMI.bmi_calc(height2, mass2)
        result3 = BMI.bmi_calc(height3, mass3)
        result4 = BMI.bmi_calc(height4, mass4)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)

if __name__ == '__main__':
    unittest.main()
