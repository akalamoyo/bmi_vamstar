import config


class Helpers:
    def __init__(self):
        self.bmi_category_and_range = config.BMI_CATEGORY_AND_HEALTH_RISK
        pass

    def bmi_formular(self, mass: int, height: int) -> float:
        """
        Calculate bmi
        """
        return mass / height

    def get_bmi_category(self, bmi: float) -> str:
        """
        Get bmi category given a bmi
        """
        return [
            ls.get("BMI Category", "")
            for ls in self.bmi_category_and_range
            if ls["BMI Range (kg/m2)"][0] <= bmi <= ls["BMI Range (kg/m2)"][1]
        ][0]

    def get_health_risk(self, bmi: float) -> str:
        """
        Get health risk status given a bmi
        """
        return [
            ls.get("Health risk", "")
            for ls in self.bmi_category_and_range
            if ls["BMI Range (kg/m2)"][0] <= bmi <= ls["BMI Range (kg/m2)"][1]
        ][0]
