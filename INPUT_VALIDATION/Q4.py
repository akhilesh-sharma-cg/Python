choice = int(input("1. View profile\n2. Edit profile\n3. Settings\n4. Exit\nEnter your choice: "))

while choice < 1 or choice > 4:
    print("Invalid choice! Please try again.")
    choice = int(input("1. View profile\n2. Edit profile\n3. Settings\n4. Exit\nEnter your choice: "))

if choice == 1:
    print("View profile")
elif choice == 2:
    print("Edit profile")
elif choice == 3:
    print("Settings")
else:
    print("Exit")

   
