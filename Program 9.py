# a. Print length of the string
def str_len(str1):
    print("Length of the String is",len(str1))

# b. Find frequency of a character in the string
def freq(str1):
    cha = input("Enter the Character:")
    print(f"Frequency of Character {cha} is",str1.count(cha))

# c. Print the frequency of uppercase and lowercase characters
def chr_up_lo(str1):
    upper = 0
    lower = 0

    for i in str1:
        if 65 <= ord(i) <= 90:
            upper += 1
        elif 97 <= ord(i) <= 122:
            lower += 1

    print(f"Number of uppercase characters: {upper}")
    print(f"Number of lowercase characters: {lower}")

def display_menu():
    print("\n1. Print length of the string")
    print("2. Find frequency of a character in the string")
    print("3. Print whether characters are in uppercase or lowercase")
    print("4. Exit")

def main():
    str1 = input("Enter the String:")
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            str_len(str1)
        elif choice == 2:
            freq(str1)
        elif choice == 3:
            chr_up_lo(str1)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        
main()
    


        



