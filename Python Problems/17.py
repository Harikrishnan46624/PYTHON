class Calculator:
   def addition(self, num1, num2):
      return num1 + num2
   def subtraction(self, num1, num2):
      return num1 - num2
   def multplication(self, num1, num2):
      return num1 * num2
   def divsion(self, num1, num2):
      return num1 / num2

calculator = Calculator()
print("Select an operator")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

choice = int(input("Enter the choce: "))

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == 1:
   result = calculator.addition(num1, num2)
   print("Result = ",result)
elif choice == 2:
   result = calculator.subtraction(num1, num2)
   print("Result = ",result)
elif choice == 3:
   result = calculator.multplication(num1, num2)
   print("Result = ",result)
elif choice == 4:
   result = calculator.divsion(num1, num2)
   print("Result = ",result)
