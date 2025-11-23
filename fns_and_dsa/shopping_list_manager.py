def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            Add_item = input("Enter the item to add: ")
            shopping_list.append(Add_item)
            print(f"'{Add_item}' has been added to shopping list.\n")
    
        elif choice == '2':
            remove_item = input("Enter the item to remove: ")
            if remove_item  in shopping_list:
                shopping_list.remove(remove_item)
                print(f"'{remove_item}' has been removed from the list.\n")
            else:
               print(f"{remove_item} not in the list.\n")  

        elif choice == '3':
            print(f"Your shopping_list: \n")
            if len(shopping_list) == 0:
                print("The list is empty. \n")
            else:
                for item in shopping_list:
                    print(f" -  {item}")
                print()

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

