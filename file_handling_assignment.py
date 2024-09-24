def create_and_write_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, world!\n")
            file.write("This is a file handling assignment.\n")
            file.write("I am a PLP student.\n")
        print("File 'my_file.txt' has been created and written to successfully.")
    except PermissionError:
        print("Error: Permission denied when trying to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while writing: {e}")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Contents of 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied when trying to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred while reading: {e}")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Hello, world!\n")
            file.write("This is a file handling assignment.\n")
            file.write("I am a PLP student.\n")
        print("Data has been appended to 'my_file.txt' successfully.")
    except PermissionError:
        print("Error: Permission denied when trying to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while appending: {e}")

def main():
    create_and_write_file()
    read_file()
    append_to_file()
    read_file()

if __name__ == "__main__":
    main()
