# BMI App #

## Description: ##
This repository contains information on:
- Calculating bmi 

## 1: How to run program ##
The `main.py` file located in the root folder is the single entry point of the program 
```sh
run main.py
```
The program uses a set of defined configuration available in config.py 

## 2: Unit testing ##
Pytest to unit test functions used in the program. Tests are defined in the `tests` folder located in the root folder of the project.
Each functional unit test comprises of:
- a data folder with input and output data
- a python file with prefix: `test_{name_of_test}.py`

## 3: Proof of execution
![image](https://user-images.githubusercontent.com/26175849/170578073-73566f4c-6fc7-4768-8955-b58066d4d549.png)

![image](https://user-images.githubusercontent.com/26175849/170577865-a466a0c2-6676-414a-a6ac-7f8a8dee6a00.png)

## 4: Additional info and futher improvements
- Table 1 is added as a list of dicts to the config file as this is static reference table. It can also be retireved from a database.
- Counting the number of patients per bmi category is scalable by adding the category as a parameter and to the config
- Program can be scaled with big data by creating udfs and moving operations to pyspark rather than pandas.
- Unit test can be further granulated to singular functions and additional scenarios can be tested

