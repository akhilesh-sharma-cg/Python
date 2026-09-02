# Input from user
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
course = input("Enter course: ").strip()
age = int(input("Enter age: "))

# Full name
full_name = first_name + " " + last_name

# Outputs
print("Full Name:", full_name)
print("Title Case:", full_name.title())
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Length of Full Name:", len(full_name))
print("First Character:", full_name[0])
print("Last Character:", full_name[-1])

print("City:", city)
print("Course:", course)

print(f"Age: {age}")

print("Contains 'Python':", "Python" in course)

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
print("Updated Course:", course.replace(old_word, new_word))

print("Number of Words in Course:", len(course.split()))