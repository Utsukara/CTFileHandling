import os

# Objective:
# The goal of this assignment is to deepen your understanding of the OS module in Python. 
# You will engage in tasks that involve file and directory operations, path manipulations, 
# and practical applications of these operations in real-world scenarios.

# Task 1: Directory Inspector:

# Problem Statement:
# Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.

# Code Example:

def list_directory_contents(path):
    # List and print all files and subdirectories in the given path
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print("File: ", entry.name)
                elif entry.is_dir():
                    print("Directory: ", entry.name)
    except FileNotFoundError:
        print("The specified directory does not exist.")
    except PermissionError:
        print("You do not have permission to access this directory.")
    except NotADirectoryError:
        print("The specified path is not a directory.")
    except Exception as e:
        print("An error occurred:", e)


directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)

# Expected Outcome:
# The script should correctly list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories.