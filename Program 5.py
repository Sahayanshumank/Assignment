num = int(input("Enter a Number:"))

# Method - 1
print("By Method - 1")
for i in range(num):
    for j in range(i+1):
        print("*",end="")
    print()

# Method - 2
print("\nBy Method - 2")
num = int(input("Enter a Number:"))
for i in range(1,num+1):
    print("*"*i)
