#Task 1: Create a program to take a string input from the user and print its length.
name = input("Enter a username:")
print(f"The length of given string is: {len(name)}")



#Task 2: Write a program to convert a list of strings into a list of integers.
str_list = ["1", "2", "763", "1122", "2059"]
int_list = [int (x) for x in str_list]
print(f"Converted integer are: {int_list}")



#Task 3: Write a program to check if a given number is even or odd.
num = int(input("Enter any integer:"))
if num % 2 == 0:
    print(f"The {num} is even number.")
else:
    print(f"The {num} is odd number.")



#Task 4:Write a program to find the largest of three numbers entered by the user.
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the greatest number.")
elif num2 > num3 and num2 > num1:
    print(f"{num2} is the greatest number.")
elif num3 > num1 and num3 >num2:
    print(f"{num3} is the greatest number.")
else:
    print("Please enter valid input.")



#Task 5: Write a program to print the multiplication table of a given number.
num = int(input("Enter a number:"))
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")



#Task 6: Write a program to print all numbers from 1 to 50 that are divisible by 5.
for i in range(1,51):
    if i % 5 == 0:
        print(i)



#Task 7: Write a program to count how many vowels are present in a given string.
user_input = input("Enter a string:")
vowels = "aeiouAEIOU"
count = 0
for char in user_input:
    if char in vowels:
        count += 1
print(f"Number of vowels in '{user_input}': {count}")



#Task 8. Write a program to print the factorial of a number using a while loop.
num=int(input("Enter any number: "))
factorial=1
i=1
while i<=num:
    factorial*=i
    i+=1
print(f"The factorial of {num} is {factorial}")



#Task 9: Write a function to check whether a given number is prime or not.
def is_prime(num):
    if num <= 1:
        return False  
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")



#Task 10: Write a function to reverse a string without using built-in functions like [::-1] or reversed().
def reverse_string(s):
    reversed_str = ""          
    for i in s:             
        reversed_str = i + reversed_str  
    return reversed_str
text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))



# Task 11: Use list coprehension to find even numbers from 1 to 100 (100 is inclusive)
even_numbers = [num for num in range(1, 101) if num % 2 == 0]
print(f"Even number from 1 to 100 is: {even_numbers}")