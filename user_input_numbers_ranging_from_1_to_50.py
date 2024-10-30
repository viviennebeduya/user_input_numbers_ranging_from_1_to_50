#initialize array for the ranges
number_per_range = [0,0,0,0,0]
#ask user to input a number ranging from 1 to 50
# ask again to input number
    #if valid, continue asking
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
        #1-10 = ?
        #11-20 = ?
        #21-30 = ?
        #31-40 = ?
        #41-50 = ?
