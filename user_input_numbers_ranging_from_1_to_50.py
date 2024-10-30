#ask user to input a number ranging from 1 to 50
try:
    user_input = int(input("Please input a number (from 1 to 50):"))
except: 
    print ("Make sure to input numbers only.")
# ask again to input number
    #if valid, continue asking
    #if invalid, display how many inputted numbers are in the following range:
        #1-10 = ?
        #11-20 = ?
        #21-30 = ?
        #31-40 = ?
        #41-50 = ?