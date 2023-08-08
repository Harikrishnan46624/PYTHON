num1 = int(input("Enter your number :"))
num2 = int(input("Enter your number :"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.division")
check = int(input("Enter your Selection :"))
if(check==1):
    result = num1 + num2
    print("Result= ",result)
elif(check==2):
    result = num1 - num2
    print("Result= ",result)
elif(check==3):
    result = num1 * num2
    print("Result= ",result)
elif(check==4):
    result = num1 / num2
    print("Result = ",result)
else:
    print("You enterd wrong number")

