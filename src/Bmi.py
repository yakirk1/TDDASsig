class BMI:

    @staticmethod
    #assuming mass is in kg's and height in cms
    def bmi_calc(height, mass):
        if not isinstance(height, (int, float)) or not isinstance(mass, (int, float)):
            return "Invalid characters,please type only numerical characters"
        if height <= 0:
            return "Invalid height"
        if mass <= 0:
            return "Invalid mass"

            # convert cms to ms
        height = height / 100

        return mass / (height * height)

    def bmi_check(bmi):
        pass