#task 1
try:
    file = open("sample.txt", "r")

    print("File contents:")
    for line in file:
        print(line, end="")

    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

#TASK 2
# Write user input to file
# Write user input to file
with open("output.txt", "w") as file:
    text = input("Enter text to write to the file: ")
    file.write(text + "\n")

# Append additional data to the file
with open("output.txt", "a") as file:
    more_text = input("Enter text to append to the file: ")
    file.write(more_text + "\n")

# Read and display final content of the file
with open("output.txt", "r") as file:
    print("\nFinal content of the file:")
    print(file.read())
