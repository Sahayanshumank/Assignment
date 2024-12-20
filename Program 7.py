def fact(num):
    fact_str = ""
    fact = 1
    while num:
        if num > 1:
            fact_str += str(num) + " * "
        else:
            fact_str += str(num)
        fact *= num
        num -= 1
    return fact_str,fact

num = int(input("Enter the Number: "))
fact = fact(num)
print(str(num)+"!",fact[0],fact[1],sep=" = ")