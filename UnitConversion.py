
temperatures_uom_list = ["Kelvin", "Celsius", "Fahrenheit", "Rankine"]
volumes_uom_list = ["liters", "tablespoons", "cubic-inches", "cups", "cubic-feet", "gallons"]

def validate_uom(input_uom):
    isValid = False
    print("input_uom value is: ", format(input_uom))
    # check if input_uom is in temperatures_uom_list
    if(input_uom) in temperatures_uom_list:
        isValid = True
    elif(input_uom) in volumes_uom_list:
        isValid = True
    else:
        print("input_uom value entered is invalid")
    return isValid 

def inputs(input_numerical_value, input_uom, target_uom, student_numeric_response):
    print("The inputs are: {0}, {1}, {2}, {3}".format(input_numerical_value, input_uom, target_uom, student_numeric_response))
    isInput_UOM_Valid = validate_uom(input_uom)
    print(isInput_UOM_Valid)


input_numerical_value = input("Please enter input_numerical_value: ")
input_uom = input("Please enter input_uom: ")
target_uom = input("Please enter target_uom: ")
student_numeric_response = input("Please enter student_numeric_response: ")

inputs(input_numerical_value, input_uom, target_uom, student_numeric_response)



#1.	The teacher must be able to provide an input numerical value, an input unit of measure, a target unit of measure, and a student’s numeric response.
#2.	The system indicates that the response is correct, incorrect, or invalid. To be considered correct, the student’s response must match an authoritative answer after both the student’s response and authoritative answer are rounded to the tenths place. 
