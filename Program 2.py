def print_factors(number):
    print(f"Factors of {number} are: ",end="")
    for i in range(1, number + 1):
        if number % i == 0:
            if i != number:
                print(i,end=",")
            else:
                print(i,end=".")

# Input from the user
num = int(input("Enter a number: "))

if num > 0:
    print_factors(num)
else:
    print("Please enter a positive number.")
