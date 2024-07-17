num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while num2 != 0:
    
   temp=num2
   num2=num1 % num2
   num1=temp

print("The GCD of two num is {}".format(num1))