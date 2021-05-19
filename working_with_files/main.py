# read only mode
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# rewrite the file
# with open("my_file.txt", mode="w") as file:
#     file.write("Nothing really matters")

# appending info
# with open("my_file.txt", mode="a") as file:
#     file.write("anyone can see")

# will create new file and write inside
with open("new_file.txt", mode="w") as file:
    file.write("Nothing really matters")
