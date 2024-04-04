
# Objective:
# The purpose of this assignment is to harness the power of regular expressions (regex) in 
# Python for advanced text data processing. You will apply regex to extract, manipulate, 
# and analyze data from text files, combining it with efficient file handling techniques.

# Task 1: Email Extractor:

# Problem Statement:
# Write a Python script to extract all email addresses from a given text file (contacts.txt). 
# The file contains a mix of text and email addresses.

# File Example:
# Contact List:

# John Doe - john.doe@example.com
# Jane Smith - jane.smith@gmail.com

# For inquiries, please contact info@example.com
# Code Example:

import re

def extract_emails(filename):
    # Read the file and use regex to find and return all email addresses
    try:
        with open(filename, 'r') as file:
            data = file.read()
            emails = re.findall(r'[\w\.-]+@[\w\.-]+', data)
            unique_emails = list(set(emails))
            for email in unique_emails:
                print(email)
    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print("An error occurred:", e)

filename = "contact_list.txt"
extract_emails(filename)

# Expected Outcome:
# The script should output a list of all unique email addresses found in the file. 
# Utilize regex to accurately identify email addresses amidst other text.