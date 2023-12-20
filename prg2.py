#WAP to print factorial of any number.

number = int(input("Enter any number : "))
fact = 1 
for i in range(1, number+1):
  fact = fact * i

print("factorial = ",fact)
