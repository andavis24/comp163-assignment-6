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

formatted_contacts = []

for i in contacts:
    name = " ".join(c[0].strip().split()).title()

    address = " ".join(c[3].strip().split()).title()

    formatted_contacts_contacts.append({"name": name,"address": address})

    phone = c[1]
    digits_only = ""

    for char in phone:
    if char.isdigit():
        digits_only += char

    if len(digits_only) == 10:
        phone = f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    else:
        phone = phone.strip()

    email = c[2].strip().lower()

    # Smart address detection
    address_parts = c[3].strip().split()
    cleaned_address_parts = []
    for part in address_parts:
        if len(part) == 2 and part.isalpha():
            cleaned_address_parts.append(part.upper())
        else:
            cleaned_address_parts.append(part.title())
    address = " ".join(cleaned_address_parts)

    formatted_contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
