import json
import logging.config
import pathlib

import pandas as pd

import config
from util.helpers import Helpers

tConfigFile = pathlib.Path.cwd() / "logging.conf"
logging.config.fileConfig(tConfigFile, disable_existing_loggers=False)

logger = logging.getLogger(__name__)


def bmi_category_and_health_risk(data: pd.DataFrame, obj: object) -> pd.DataFrame:
    """
    Append bmi, bmi category and health risk status to data
    """

    data.loc[:, "HeightM"] = data["HeightCm"] / 100
    data.loc[:, "BMI"] = data.apply(
        lambda x: x["WeightKg"] / x["HeightM"], axis=1
    ).round(1)
    data.loc[:, "BMI Category"] = data["BMI"].apply(obj.get_bmi_category)
    data.loc[:, "Health_risk"] = data["BMI"].apply(obj.get_health_risk)

    data.drop("HeightM", axis=1, inplace=True)
    return data


def count_patients_per_bmi_category(data: pd.DataFrame, category: str) -> dict:
    """
    Count patients per given bmi category
    """
    return {
        "count_patients_per_bmi_category": len(
            data.loc[data["BMI Category"] == category]
        ),
        "category": category,
    }


if __name__ == "__main__":
    logger.info("Execute program")
    helpers_obj = Helpers()

    input_data = pd.read_json(config.INPUT_DATA_FILEPATH)
    output_data = bmi_category_and_health_risk(input_data, helpers_obj)
    output_data.to_json(config.OUTPUT_BMI_CATEGORY_FILEPATH, orient="records")

    # delete data after use to free up memory
    del input_data

    with open(config.OUTPUT_COUNT_PATIENTS_FILEPATH, "w") as f:
        f.write(
            json.dumps(
                count_patients_per_bmi_category(output_data, config.BMI_CATEGORY)
            )
        )

    del output_data

    logger.info("End")
