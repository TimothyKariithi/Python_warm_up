def multisum(num1, num2): #function
    if num1 * num2 <= 1000: # boolean data type; if number 1 multiplied by number 2 = less than 100 then print the product
        return num1 * num2 # loop
    
    else:  # if the num1 and num2 multiplied are greater than 1000 then do not return and add them together.
        return num1 + num2 
    
bob = multisum(37, 51) # variable
print(bob)# string literal