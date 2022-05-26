BMI_CATEGORY_AND_HEALTH_RISK = [
    {
        "BMI Category": "Underweight",
        "BMI Range (kg/m2)": [0, 18.4],
        "Health risk": "Malnutrition risk",
    },
    {
        "BMI Category": "Normal weight",
        "BMI Range (kg/m2)": [18.5, 24.9],
        "Health risk": "Low risk",
    },
    {
        "BMI Category": "Overweight",
        "BMI Range (kg/m2)": [25, 29.9],
        "Health risk": "Enhanced risk",
    },
    {
        "BMI Category": "Moderately obese",
        "BMI Range (kg/m2)": [30, 34.9],
        "Health risk": "Medium risk",
    },
    {
        "BMI Category": "Severely obese",
        "BMI Range (kg/m2)": [35, 39.9],
        "Health risk": "High risk",
    },
    {
        "BMI Category": "Very severely obese",
        "BMI Range (kg/m2)": [40, 100],
        "Health risk": "Very high risk",
    },
]
BMI_CATEGORY = "Overweight"
INPUT_DATA_FILEPATH = "data/input_data.json"
OUTPUT_BMI_CATEGORY_FILEPATH = "output/bmi_category_health_risk.json"
OUTPUT_COUNT_PATIENTS_FILEPATH = "output/count_patients.json"
TEST_DATA_FILEPATH = "tests/data/test_data.json"
TEST_OUTPUT_BMI_CATEGORY_FILEPATH = "tests/data/output_data_bmi_category.json"
TEST_OUTPUT_COUNT_PATIENTS_FILEPATH = "tests/data/output_data_count_patients.json"
