# file_handling_assignment.py

def main():
    try:
        # File Creation and Writing
        with open('my_file.txt', 'w') as file:
            file.write("Hello, this is the first line.\n")
            file.write("The number is: 42\n")
            file.write("Final line: Python is amazing!\n")
        print("File 'my_file.txt' created and written successfully.")

        # File Reading and Display
        with open('my_file.txt', 'r') as file:
            print("\nReading 'my_file.txt':")
            content = file.read()
            print(content)

        # File Appending
        with open('my_file.txt', 'a') as file:
            file.write("Appending more text here.\n")
            file.write("Second appended line: 100 days of Python.\n")
            file.write("Final appended line: Task completed!\n")
        print("Text appended successfully.")

        # Reading the updated content
        with open('my_file.txt', 'r') as file:
            print("\nReading 'my_file.txt' after appending:")
            updated_content = file.read()
            print(updated_content)

    except FileNotFoundError as e:
        print(f"Error: {e}. The file does not exist.")
    except PermissionError as e:
        print(f"Error: {e}. You do not have permission to access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File operation completed.")


if __name__ == "__main__":
    main()
