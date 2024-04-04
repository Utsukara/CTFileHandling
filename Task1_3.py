import os

# Task 3: File Extension Counter:

# Problem Statement:
# Develop a Python script that counts the number of files of each extension type in a directory. For instance, in a directory with five '.txt' files and three '.py' files, the script should report "TXT: 5" and "PY: 3".

# Code Example:
def count_file_extensions(directory):
    # Count and print the number of files of each extension type in the directory
    try:
        file_extensions = {}
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    file_name = entry.name
                    file_extension = file_name.split(".")[-1].upper()
                    if file_extension in file_extensions:
                        file_extensions[file_extension] += 1
                    else:
                        file_extensions[file_extension] = 1
        for extension, count in file_extensions.items():
            print(f"{extension}: {count}")
    except FileNotFoundError:
        print("The specified directory does not exist.")
    except PermissionError:
        print("You do not have permission to access this directory.")
    except NotADirectoryError:
        print("The specified path is not a directory.")
    except Exception as e:
        print("An error occurred:", e)


directory_path = input("Enter the directory path: ")
count_file_extensions(directory_path)

# Expected Outcome:
# The script should accurately count and display the number of files for each extension type 
# in the specified directory. Handle different cases of file extensions 
# (e.g., '.TXT' and '.txt' should be considered the same).