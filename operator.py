num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1+num2

diff = num1 - num2
multi = num1 * num2
if num2 != 0:
    div = num1 / num2
else:
    div = "undefined (cannot divide by zero)"
print(f"The addition of {num1} and {num2} is : {sum} ")
print(f"The subtraction of {num1} and {num2} is : {diff} ")
print(f"The multiplication of {num1} and {num2} is : {multi} ")
print(f"The division of {num1} and {num2} is : {div} ")