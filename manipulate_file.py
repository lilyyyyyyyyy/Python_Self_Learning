### Writing a File ###

# Method 1:
new_file = open("new_file.txt", "w") #"w" means "open the file for writing"
new_file.write("Hellfdsfso World")
new_file.write("\n")  #indent
new_file.write("...")
new_file.write("\n")
new_file.write("Goofdsfdbye")

# Method 2:
file_name = "my_message.txt"
with open(file_name, "w") as file: # NOTE: "w" means "open the file for writing"
    file.write("Hello World")
    file.write("\n")
    file.write("\n")
    file.write("...")
    file.write("\n")
    file.write("\n")
    file.write("Goodbye")

# Reading Files

file_name = "my_message.txt" # refers to a file path relative to the path from which you invoke your your script.

with open(file_name, "r") as file: # NOTE: "r" means "open the file for reading"
    contents = file.read()
    print(contents)
