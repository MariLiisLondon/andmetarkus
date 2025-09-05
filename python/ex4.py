# Check if a person is an adult (18 years or older)
##def is_adult(age: int) -> bool:
    if not isinstance(age, int) or age < 0:
        return "Invalid age"
    elif age>= 18:
        return True
    else:
        return False

##print(is_adult(20))  # True
##print(is_adult(15))  # False
##print(is_adult("ri"))   
##print(is_adult(1.2))    
##print(is_adult(-5))   
##print(is_adult("0"))

#age = int(input("Enter your age: "))
#if is_adult(age):       
    print("You are an adult.")
#else:
    #print("You are not an adult.")
    