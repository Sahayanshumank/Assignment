t1 = (1, 2, 5, 7, 2, 4)

# a. Print tuple in two lines
mid = len(t1) // 2
print(t1[:mid]) 
print(t1[mid:])

# b. Concatenate with tuple t2
t2 = (10, 11)
t3 = t1 + t2 

print("Concatenated tuple:", t3)