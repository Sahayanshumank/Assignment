def choice():
    flag = True
    print("1. Area of Rectangle",
          "2. Area of Square",
          "3. Area of Circle",
          "4. Area of Triangle",
          sep= "\n")
    while flag:
        num = int(input("Enter Your Choice (1-4): "))
        if num in (1, 2, 3, 4):
            flag = False
            print()
        else:
            print("Invalid choice. Please choose a valid option.")
    return num

def rectangle():
    len = float(input("Enter Length: "))
    wid = float(input("Enter Width: "))
    ar = len*wid
    return ar

def square():
    sid = float(input("Enter Side: "))
    ar = sid*sid
    return ar

def circle():
    rad = float(input("Enter Radius: "))
    ar = 3.14*(rad**2)
    return ar

def trianle():
    base = float(input("Enter Base: "))
    height = float(input("Enter Height: "))
    ar = 0.5*base*height
    return ar
    
ch = choice()
if ch == 1:
    print("Area of Rectangle is",rectangle())
elif ch == 2:
    print("Area of Square is",square())
elif ch == 3:
    print("Area of Circle is",circle())
elif ch == 4:
    print("Area of Triangle is",trianle())

