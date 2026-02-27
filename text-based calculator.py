def get_input():
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    operation = input("Pick an operation +, -, *, / : ")
    return num1,num2,operation

def get_output(num1,num2,operation):
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif operation=="/":
        return num1/num2
    
num1,num2,operation=get_input()
result = get_output(num1,num2,operation)
print(num1,operation,num2,"= ",result)

user_response=input(f"Enter 'y' to continue calculation with {result}, 'n' to start a new calculation : ").lower()
if user_response=="y":
    num3=int(input("What's the new number : "))
    res_ult=get_output(num3,result,operation)
    print(num3,operation,result,"= ",res_ult)

else:
    new_num1,new_num2,new_operation=get_input()
    new_result=get_output(new_num1,new_num2,new_operation)
    print(new_num1,new_operation,new_num2,"= ",new_result)
    


