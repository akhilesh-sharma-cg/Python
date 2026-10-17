def format_name(first, last, uppercase=False):
    full_name = first + " " + last

    if uppercase == True:
        return full_name.upper()
    else:
        return full_name

print(format_name("Akhilesh", "Sharma"))
print(format_name("Akhilesh", "Sharma", True))