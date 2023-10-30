def calculator():
    print("_______________  Welcome to the Calulator ______________")
    print()

    print('''Type "exit" for exiting the calculator ''')
    print()

    result = None

    while True:
        if result is not None:
            use_result = input(f"Use the previous result ({result}) for further calculation? (y/n) or type 'exit' for exit.: ").lower()
            if use_result =='y':
                num1 = result
            elif use_result == 'exit':
                print("Exiting the Calculator.")
                break
            else:
                num1 = input("Enter Number(value 1) : ")
        else:
            num1 = (input("Enter Number(value 1) : "))

        if num1 =='exit':
            print("Exiting the Calculator.")
            break
        
        try:
            num1 = float(num1)
        except ValueError:
            print("Invalid input . Please enter a valid number.")
            continue
        print()
        operation = input('''-------------  Select Operator------------ 
                  
            1. For Addition -->  +  
            2. For Subtraction --> - 
            3. For Multiplication --> *
            4. For Divition --> / 
            5. For Power of -->  ^ 
            6. For Division Remainder -->  %
                      
                      (or 'exit' to quit)   :  ''')
        print()

        if operation == 'exit':
            print("Exiting the Calculator.")
            break
        
        num2 = input("Enter Number(value 2) (or 'exit' to quit): ")
        if num2 == 'exit':
            print("Exiting the calculator.")
            break
        try:
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        valid_operators= ["+","-","/","*","%","^"]

        if operation not in valid_operators:
            print("Enter correct operator from the list!!")
            continue
    
        else:
            if operation == "+":
                result = num1+num2
            
            elif operation == "-":
                result = num1-num2
            
            elif operation == "/":
                if num2 ==0:
                    print("Division by zero is not allowed.")
                    continue
                result = num1/num2
            
            elif operation == "*":
                result = num1*num2
            
            elif operation == "%":
                if num2 == 0:
                    print("Modulo by zero is not allowed.")
                    continue
                result = num1%num2
            
            elif operation == "^":
                result = num1**num2
            print("Result is : ",result)
        
    

calculator()

