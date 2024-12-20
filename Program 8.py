def factorial(num):
	fact = 1
	while num:
		fact *= num
		num -= 1
	return fact
		
		
def fact_series(num):
    sum_str = ""
    sum = 0
    for i in range(1,num+1):
        sum += round(1/factorial(i),2)
        if i < num:
            sum_str += "1/"+str(factorial(i)) + " + "
        else:
            sum_str += "1/"+str(factorial(i)) + " = "
    return sum_str,sum
    
 		
num = int(input("Enter the Number: "))
fact = fact_series(num)
print(fact[0],fact[1],sep="")