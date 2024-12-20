heading = "| Height(in Feet) | Height(in inches) |"

length = len(heading)

print("-"*length)
print(heading)
print("-"*length)

for i in range(50, 61):
    value = i/10.0 

    feet = round(value,1)
    inch = round(value*12,1)

    print("|     ",feet,"ft","    |   ",inch,"inches","   |")
    
    print("-"*length)

