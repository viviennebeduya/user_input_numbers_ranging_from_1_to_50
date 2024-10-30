# initialize array for the ranges
number_per_range = [0,0,0,0,0]
# ask user to input a number ranging from 1 to 50
# if valid, continue asking for input.
while True:
    try:
        user_input = int(input("Please input a number (from 1 to 50):"))

        if user_input >=1 and user_input <=50:
            if user_input >=1 and user_input<=10:
                number_per_range[0] +=1
            if user_input >=11 and user_input<=20:
                number_per_range[1] +=1
            if user_input >=21 and user_input<=30:
                number_per_range[2] +=1
            if user_input >=31 and user_input<=40:
                number_per_range[3] +=1
            if user_input >=41 and user_input<=50:
                number_per_range[4] +=1
        else:
            print ("Number is already out of range. Input must only range from number 1 to 50.")
            break
    except: 
        print ("Make sure to input numbers only.")
        
#if invalid, display how many inputted numbers are in the following range:

print ("Here's all your input based on various range:")
print (f"1-10: {number_per_range[0]}")
print (f"11-20: {number_per_range[1]}")
print (f"21-30: {number_per_range[2]}")
print (f"31-40: {number_per_range[3]}")
print (f"41-50: {number_per_range[4]}")
