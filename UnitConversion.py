import sys

temperatures_uom_list = ["Kelvin", "Celsius", "Fahrenheit", "Rankine"]
volumes_uom_list = ["liters", "tablespoons", "cubic-inches", "cups", "cubic-feet", "gallons"]

# First validate input_uom value - is it in the specified list of temperature types or volume types?
def validate_input_uom(input_uom):
    isValid = False

    if(input_uom) in temperatures_uom_list:
        isValid = True
    elif(input_uom) in volumes_uom_list:
        isValid = True

    return isValid 

# validate if the target_uom is valid for the specified input_uom
def validate_target_uom(input_uom, target_uom):
    isValid = False

    if(input_uom) in temperatures_uom_list:
        if(target_uom) in temperatures_uom_list:
            isValid = True
    elif(input_uom) in volumes_uom_list:
        if(target_uom) in volumes_uom_list:
            isValid = True

    return isValid 

# conversion function to convert input_numerical_value from input_uom to target_uom
def convertInputUOM_to_TargetUOM(input_numerical_value, input_uom, target_uom):
    convertedOutput = 0.0

    if(input_uom) in temperatures_uom_list:
        convertedOutput = convertTemperature(input_numerical_value, input_uom, target_uom)
    if(input_uom) in volumes_uom_list:
        convertedOutput = convertVolume(input_numerical_value, input_uom, target_uom)
        
    return convertedOutput

def convertTemperature(input_numerical_value, input_uom, target_uom):
    outputTemp = 0.0
    # convert input_uom to 'Kelvin' temperature UOM.
    k = toK[input_uom](float(input_numerical_value))

    # now calculate all the temperature values in temperatures_uom_list.
    celsiusValue = k - 273.15
    fahrenheitValue = k * 1.8 - 459.67
    rankineValue =  k * 1.8
    kelvinValue = k 

    if target_uom == "Kelvin":
        outputTemp = kelvinValue
    elif target_uom == "Celsius":
        outputTemp = celsiusValue
    elif target_uom == "Fahrenheit":
        outputTemp = fahrenheitValue
    elif target_uom == "Rankine":
        outputTemp = rankineValue

    # round outputTemp to the tenths decimal place
    outputTemp = round(outputTemp, 1)
    return outputTemp

def convertVolume(input_numerical_value, input_uom, target_uom):
    outputVolume = 0.0
    # convert input_uom to 'tablespoons' volume UOM.
    t = toT[input_uom](float(input_numerical_value))

    # now calculate all the volume values in volumes_uom_list.
    litersValue = t * 0.0147868
    gallonsValue = t * 0.00390625
    cupsValue =  t * 0.0625
    cubicInchesValue = t * 0.902344
    cubicFeetValue = t * 0.00052219
    tablespoonsValue = t

    if target_uom == "liters":
        outputVolume = litersValue
    elif target_uom == "tablespoons":
        outputVolume = tablespoonsValue
    elif target_uom == "cubic-inches":
        outputVolume = cubicInchesValue
    elif target_uom == "cups":
        outputVolume = cupsValue
    elif target_uom == "cubic-feet":
        outputVolume = cubicFeetValue
    elif target_uom == "gallons":
        outputVolume = gallonsValue

    # round outputVolume to the tenths decimal place
    outputVolume = round(outputVolume, 1)
    return outputVolume

# convert given temperature to Kelvin UOM
toK = { 'Celsius': (lambda c: c + 273.15),
        'Fahrenheit': (lambda f: (f + 459.67) / 1.8),
        'Rankine': (lambda r: r / 1.8),
        'Kelvin': (lambda k: k) 
      }

# convert given volume to tablespoons UOM
toT = { 'liters': (lambda l: l * 67.628),
        'gallons': (lambda g: g * 256),
        'cups': (lambda c: c * 16),
        'cubicInches': (lambda ci: ci * 1.10823),
        'cubicFeet': (lambda cf: cf * 1915.01),
        'tablespoons': (lambda t: t) }

# This is the main function that takes the input values,  and invokes functions to validate input_uom/target_uom and to convert input_numerical_value to the corresponding value in target_uom
def processInputs(input_numerical_value, input_uom, target_uom, student_numeric_response):
    programConversionOutput = 0
    # round student_numeric_response to the tenth decimal place
    student_numeric_response = round(float(student_numeric_response), 1)

    # validate input_uom
    isInput_UOM_Valid = validate_input_uom(input_uom)

    # validate target_uom only if input_uom is valid
    if(isInput_UOM_Valid):
        isTarget_UOM_Valid = validate_target_uom(input_uom, target_uom)
        # invoke convert function only if input_uom and target_uom are valid
        if(isTarget_UOM_Valid):
            programConversionOutput = convertInputUOM_to_TargetUOM(input_numerical_value, input_uom, target_uom)
            
            if programConversionOutput == student_numeric_response:
                print("correct")
            elif programConversionOutput != student_numeric_response:
                print("incorrect")
        else:
            print("invalid")
    else:
        print("invalid")

# Validate the input data values for input_numerical_value and student_numerica_response: The input values entered must be numbers.
def validateDataTypes(input_numerical_value, student_numeric_response):
    try:
        input_numerical_value = float(input_numerical_value)
    except ValueError:
        print("input_numerical_value provided is not a number. It's a string")
        sys.exit('incorrect')
    
    try:
        student_numeric_response = float(student_numeric_response)
    except ValueError:
        print("student_numeric_response provided is not a number. It's a string")
        sys.exit('incorrect')



input_numerical_value = input("Please enter input_numerical_value: ")
input_uom = input("Please enter input_uom: ")
target_uom = input("Please enter target_uom: ")
student_numeric_response = input("Please enter student_numeric_response: ")


validateDataTypes(input_numerical_value, student_numeric_response)
processInputs(input_numerical_value, input_uom, target_uom, student_numeric_response)

