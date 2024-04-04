import os

# Task 2: File Size Reporter:

# Problem Statement:
# Write a Python program that reports the sizes of all files in a specific directory. 
# The program should ask the user for a directory path and then print each file's name and size 
# within that directory.

# Code Example:

def report_file_sizes(directory):
    # Iterate through files in the directory and print their names and sizes
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    print("File:", entry.name, "Size:", entry.stat().st_size, "bytes")
    except FileNotFoundError:
        print("The specified directory does not exist.")
    except PermissionError:
        print("You do not have permission to access this directory.")
    except NotADirectoryError:
        print("The specified path is not a directory.")
    except Exception as e:
        print("An error occurred:", e)

directory_path = input("Enter the directory path: ")
report_file_sizes(directory_path)

# Expected Outcome:
# Your program should display the name and size (in bytes) of each file in the given directory. 
# Ensure that the program only reports on files, not directories, and handles any errors gracefully.