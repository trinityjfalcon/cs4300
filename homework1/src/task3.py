#Create a new file named task3.py. Create an if statement to check if a given number is positive,
#negative, or zero. Implement a for loop to print the first 10 prime numbers (you may need to
#research how to calculate prime numbers). Create a while loop to find the sum of all numbers from
#1 to 100. Write pytest test cases to verify the correctness of your code for each control structure.

number = float(input("Enter a number:"))

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
elif number == 0:
    print(f"The number is zero")

counter = 0
num = 1
while counter < 10:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        counter += 1
    num += 1