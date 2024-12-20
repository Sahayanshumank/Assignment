num = int(input("Enter a Number: "))

# Initialize variables for sum and the string representation of the series
sum_str=""
sum=0

for i in range(1,num+1):
    sum_str += str(i)   # Append the current number to the series string
    sum += i    # Add the current number to the sum

    # Add a plus sign after each number except the last one
    if i < num:
        sum_str += " + "  
    else:
        sum_str += " = "

print(sum_str,sum)