# Function for doing arithmetic calculations

def calc(operator):
    
    if (operator=='+'):
        return (num1 + num2)
    
    elif (operator=='-'):
       return (num1 - num2)
   
    elif (operator=='*'):
        return (num1 * num2)
    
    elif (operator=='/'):
        return (num1 / num2)
    
    elif (operator=='//'):
        return (num1 // num2)
    
    elif (operator=='%'):
        return (num1 % num2)
        
    else:
        print("Sorry! This operator is not available")
    
    
# Driver code    
if __name__=="__main__":
    print("Arithmetic Calculator ")
    num1= float(input("\n Enter first number: "))
    num2= float(input(" Enter second number: "))
    operator= input(" Select operator from +, -, *, /, //, % : ")
    print (f' {num1} {operator} {num2} is {calc(operator)}')
