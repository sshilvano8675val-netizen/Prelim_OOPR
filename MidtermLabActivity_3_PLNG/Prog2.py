name = input("Enter your name: ")
last_name = input("Enter your last name: ")

full_name = name + " " + last_name

print("Full Name: ", full_name)

print("First character:", name[0])
print("Last Character: ", last_name[0])

try:
    name[0] = "D"
except TypeError as e:
    print("Error:", e)
    print("Strings are immutable and cannot be changed directly.")

new_name = "D" + name[1]
print("New Name:", new_name)
print("Original First Name:", name)

print("Characters in Full Name:")
for characters in full_name:
    print(characters)

space = full_name.find(" ")
print("Sliced First Name:", full_name[:space])
print("Sliced Last Name:", full_name[space + 1:])

character = input("Enter one character to search: ").lower()

found = False

for i in range(len(full_name)):
    if full_name[i].lower() == character:
        print("Character found at index", i)
        found = True

if not found:
    print("Character not found.")