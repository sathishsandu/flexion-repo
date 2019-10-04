
temperatures_uom_list = ["Kelvin", "Celsius", "Fahrenheit", "Rankine"]
volumes_uom_list = ["liters", "tablespoons", "cubic-inches", "cups", "cubic-feet", "gallons"]


def inputs(temperature_uom_type, volume_uom_type):
    print("The inputs are: {0}, {1}".format(temperature_uom_type, volume_uom_type))
    # print("temperature type is: {1}".format(volume_uom_type))
    if(temperature_uom_type) in temperatures_uom_list:
        print("Valid Temperature Type")
    else:
        print("Invalid Temperature Type")
    if(volume_uom_type) in volumes_uom_list:
        print("Valid Volume Type")
    else:
        print("Invalid Volume Type")
    

temperature_uom_type = input("Please enter temperature type: ")
volume_uom_type = input("Please enter volume type: ")
# greeting = input("Enter Greeting: ")
inputs(temperature_uom_type, volume_uom_type)

# greet("sathish", "good morning")
