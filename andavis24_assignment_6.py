# andavis24_assignment_6.py
# Student: Ajani Davis
# Assignment 6: Contact Information Formatter
# Demonstrates mastery of string methods for data cleaning and formatting

print("Enter contact information (format: name|phone|email|address):")
print()
print("=== CONTACT DIRECTORY ===")

contacts = []

while True:
    entry = input()
    if entry.strip().upper() == "DONE":
        break
    else:
        part = entry.split("|")
        contacts.append(part)      