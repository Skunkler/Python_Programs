

import math

#This function address task1 it takes an input from a user in degree minutes seconds format and converts it to decimal degrees
def DMS_to_DD(Input):
    try:

        #we take the DMS input from the user and split it up by the comma into three different elements
        first = Input.split(',')[0]
        second = Input.split(',')[1]
        third = Input.split(',')[2]
        #This condition statement checks to see it the user added a negative value
        #and if so the calculation is done to preserve the negative value in its ouput Decimal degree format
        if first[0] == '-':
            answer = float(first) - float(second)/60 - float(third)/3600

            #This returns the answer to the user in a str format with the final decimal degree value rounded to the 4 decimal place
            return "The value was in DMS form and its DD form is " + str(round(answer,4))
        else:
            #if the input from the user isn't a negative value then the calculation is done as if it were a positive value
            answer = float(first) + float(second)/60 + float(third)/3600

            #This returns the answer to the user in a str format which rounds the decimal degree to the 4th place
            return "The value was in DMS form and its DD form is " + str(round(answer,4))
    except:
        #This is if the intended DMS form is not valid, this message is sent to the user
        return "This input is not a valid DMS form, Please try again."

#This function was design for task2
def DD_to_DMS(Input):
    try:
        #variable input_value_split splits the input into a whole part of the number which is the value to the left of the decimal
        #and a the fractional value which is everything to the right of the decimal
        input_value_split = Input.split('.')

        #variable degree represents the whole value or everything to the left of the decimal point
        degree = input_value_split[0]

        
        #decimal1 is the fractional part, or everything to the right of the decimal point with the decimal point added back in to the value
        decimal = '.' + input_value_split[1]

        #This variable converts the value of decimal into a float data type and multiplies it by 60 to get the value for minutes
        decimal_floatConvert = 60 * float(decimal)

        #This variable converts the previous variable from a float data type to a string data type
        str_decimalfloatConvert = str(decimal_floatConvert)

        #We convert the float back into the string data type so that we can split the value based off of the decimal again
        #and assign to minutes variable to the whole part of the number
        minutes = str_decimalfloatConvert.split('.')[0]

        #variable second_str is the fractional part of decimal_floatConvert
        second_str = '.' + str_decimalfloatConvert.split('.')[1]

        #we assign the variable seconds to the whole part of the result of the equation to get the values for seconds
        seconds = float(second_str) * 60
        #return the value to the user with the seconds variable properly formated to get the final result in DMS format
        return "The input value was in DD form and its DMS form is " + degree + " " +  minutes + " " +  str(int(seconds))
    #This print message is executed if there was a '.' in the user input but the user input cannot be converted into a degree minutes seconds format
    except:
        print "THis input is not a valid form of DD, Please try again."


#This function was designed to address task3
def main_call():

    #this prompts the user for an input and stores it in variable User_input
    User_input = raw_input("Please enter a DMS or DD format to convert: ")

    #This first condition checks to see if there is a comma in User_input and if so call DMS_to_DD function with User_input and print the results
    if ',' in User_input:
        print DMS_to_DD(User_input)

    #This elif statement checks to see if there is a decimal in the User_input and if so call the DD_to_DMS function using the value stored in User_value
    #Then print the results to the screen
    elif '.' in User_input:
        print DD_to_DMS(User_input)

    #this message is printed to the screen if the user does not enter a valid input that can be used by either of the two functions
    else:
        print "Please enter a valid form of a DMS or DD to convert."



#This calls the main_call() function which prompts the user for input when one launches this python script
main_call()
