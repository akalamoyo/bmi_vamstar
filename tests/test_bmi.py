import pandas as pd
import pytest

import config
from main import bmi_category_and_health_risk, count_patients_per_bmi_category
from util.helpers import Helpers

helpers_obj = Helpers()


def test_bmi():
    """
    Test bmi calculation, bmi_category and health risk retrieval
    Test count of patients with given bmi category

    """

    data = pd.read_json(config.TEST_DATA_FILEPATH)
    category = "Very severely obese"
    expected_outpput_bmi_category = pd.read_json(
        config.TEST_OUTPUT_BMI_CATEGORY_FILEPATH
    )
    expected_output_count_patients = pd.read_json(
        config.TEST_OUTPUT_COUNT_PATIENTS_FILEPATH
    )
    output_bmi_category = bmi_category_and_health_risk(data, helpers_obj)
    output_count_patients = pd.DataFrame.from_dict(
        [count_patients_per_bmi_category(output_bmi_category, category)]
    )

    assert expected_outpput_bmi_category.equals(output_bmi_category)
    assert expected_output_count_patients.equals(output_count_patients)