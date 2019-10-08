
Github Repo for the CICD POC

UnitConversion.py is the main python script.

Installation & Execution Instructions:
Software Pre-requisites:
Python3 (I am using Python 3.6.3rc1)

1. Clone this repo to your local environment using this command:
git clone https://github.com/sathishsandu/sathishsandu-cicd-repo.git

2. On command line (unix or windows), execute the following command
python UnitConversion.py

Then provide values for the following input parameters from command line:
input_numerical_value 
input_uom 
target_uom
student_numeric_response

Output of the Program will be one of these values:
correct -   When the Student_numeric_response value matches the authoritative answer after both the student’s response and authoritative answer are rounded to the tenths place. 
incorrect - When the Student_numeric_response value does not match the authoritative answer after both the student’s response and authoritative answer are rounded to the tenths place. 
invalid - The output will be 'Invalid' if one of the scenarios is true:
    * If the input_uom value and/or target_uom provided is not in one of the following valid values lists:
    temperatures_uom_list = ["Kelvin", "Celsius", "Fahrenheit", "Rankine"]
    volumes_uom_list = ["liters", "tablespoons", "cubic-inches", "cups", "cubic-feet", "gallons"]
    * If type of input_uom and target_uom must match. That means, if the input_uom is a temperature uom then target_uom must also be temperature uom. 
      If the input_uom is a volume uom then target_uom must also be a volume uom. 