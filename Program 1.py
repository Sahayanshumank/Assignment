#Storing Invalid Input String to a Variable
In_Input = "Please Enter Marks B/W 0 to 100.\n"

#To Get a Valid Input from User
temp = 0
while temp == 0:
    sub_1 = int(input("Enter Marks of 1st Subject:"))
    if 0 < sub_1 < 100:
        temp = 1
    else:
        print(In_Input)
        temp = 0
while temp == 1:
    sub_2 = int(input("Enter Marks of 2nd Subject:"))
    if 0 < sub_2 < 100:
        temp = 2
    else:
        print(In_Input)
        temp = 1
while temp == 2:
    sub_3 = int(input("Enter Marks of 3rd Subject:"))
    if 0 < sub_3 < 100:
        temp = 3
    else:
        print(In_Input)
        temp = 2

#Showing Subject Marks
print("\nSubject 1:",format(sub_1,"6"))
print("Subject 2:",format(sub_2,"6"))
print("Subject 3:",format(sub_3,"6"))

#Calculating Percentage
per = (sub_1+sub_2+sub_3)/3

#Showing Pecentage
print("Percentage:",format(per,"5.2f"))

#Assigning Grades
if per >= 80:
    print("Your Grade is A")
elif per >= 60:
    print("Your Grade is B")
elif per >= 40:
    print("Your Grade is C")
else:
    print("Your Grade is D")
