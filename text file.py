# file_handling_assignment.py

# File Creation and Writing
try:
    # Create a new file and write initial content
    with open("my_file.txt", 'w') as file:
        file.write("First line: Hello, World!\n")
        file.write("Second line: The number is 42.\n")
        file.write("Third line: Python is awesome!\n")
    print("File created and initial content written successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error while writing to file: {e}")

# File Reading and Displaying Content
try:
    # Read the content from the file
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nReading file content:")
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error while reading the file: {e}")

# File Appending
try:
    # Open file in append mode and add new lines
    with open("my_file.txt", 'a') as file:
        file.write("Fourth line: Appending more text.\n")
        file.write("Fifth line: 2024 is the year of AI!\n")
        file.write("Sixth line: Adding one more line.\n")
    print("\nNew content appended successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error while appending to file: {e}")

# Reading the updated content
try:
    # Read the updated content to confirm appending
    with open("my_file.txt", 'r') as file:
        updated_content = file.read()
        print("\nUpdated file content:")
        print(updated_content)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error while reading the updated file: {e}")

finally:
    print("\nFile operations completed.")
