def create_lists(n):
    even_list = []
    odd_list = []
  
    for i in range(1, 2*n+1):
        if i % 2 == 0:
          even_list.append(i)
        else:
          odd_list.append(i)
  
    return even_list, odd_list

def display_menu():
    print("\nList Operations Menu:")
    print("1. Display Even List")
    print("2. Display Odd List")
    print("3. Append an element to Even List")
    print("4. Append an element to Odd List")
    print("5. Insert an element at a specific position in Even List")
    print("6. Insert an element at a specific position in Odd List")
    print("7. Remove an element from Even List")
    print("8. Remove an element from Odd List")
    print("9. Sort Even List")
    print("10. Sort Odd List")
    print("11. Reverse Even List")
    print("12. Reverse Odd List")
    print("13. Concatenate Even and Odd Lists")
    print("14. Find the length of Even List")
    print("15. Find the length of Odd List")
    print("16. Check if an element exists in Even List")
    print("17. Check if an element exists in Odd List")
    print("18. Clear Even List")
    print("19. Clear Odd List")
    print("20. Exit")

def main():
    even_list, odd_list = create_lists(10)
    display_menu()
  
    while True:
        choice = int(input("Enter your choice: "))
    
        if choice == 1:
            print("Even List:", even_list)
        elif choice == 2:
            print("Odd List:", odd_list)
        elif choice == 3:
            element = int(input("Enter element to append to Even List: "))
            even_list.append(element)
        elif choice == 4:
            element = int(input("Enter element to append to Odd List: "))
            odd_list.append(element)
        elif choice == 5:
            pos = int(input("Enter position to insert in Even List: "))
            element = int(input("Enter element to insert: "))
            even_list.insert(pos, element)
        elif choice == 6:
            pos = int(input("Enter position to insert in Odd List: "))
            element = int(input("Enter element to insert: "))
            odd_list.insert(pos, element)
        elif choice == 7:
            element = int(input("Enter element to remove from Even List: "))
            even_list.remove(element)
        elif choice == 8:
            element = int(input("Enter element to remove from Odd List: "))
            odd_list.remove(element)
        elif choice == 9:
            even_list.sort()
        elif choice == 10:
            odd_list.sort()
        elif choice == 11:
            even_list.reverse()
        elif choice == 12:
            odd_list.reverse()
        elif choice == 13:
            concatenated_list = even_list + odd_list
            print("Concatenated List:", concatenated_list)
        elif choice == 14:
            print("Length of Even List:", len(even_list))
        elif choice == 15:
            print("Length of Odd List:", len(odd_list))
        elif choice == 16:
            element = int(input("Enter element to check in Even List: "))
            if element in even_list:
                print(f"{element} exists in Even List.")
            else:
                print(f"{element} does not exist in Even List.")
        elif choice == 17:
            element = int(input("Enter element to check in Odd List: "))
            if element in odd_list:
                print(f"{element} exists in Odd List.")
            else:
                print(f"{element} does not exist in Odd List.")
        elif choice == 18:
            even_list.clear()
        elif choice == 19:
            odd_list.clear()
        elif choice == 20:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        print()
    
main()
