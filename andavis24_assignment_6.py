# andavis24_assignment_6.py
# Student: Ajani Davis
# Assignment 6: Contact Information Formatter
# Demonstrates mastery of string methods for data cleaning and formatting

# --- Program introduction ---
print("Enter contact information (format: name|phone|email|address):\n")

# Create an empty list to hold all contacts before cleaning
contacts = []

# === INPUT PHASE ===
# This loop keeps asking for input until the user types DONE
while True:
    entry = input()
    # Stop if the user types DONE (any capitalization works)
    if entry.strip().upper() == "DONE":
        break
    else:
        # Split the entry into 4 parts (name, phone, email, address)
        parts = entry.split("|")
        contacts.append(parts)

# === CLEANING PHASE ===
# Create a new list to store cleaned and formatted contact info
cleaned_contacts = []

# Loop through each contact entered by the user
for i in contacts:
    # --- Name cleaning ---
    # Remove extra spaces, split into words, rejoin with one space, and title case
    name = " ".join(i[0].strip().split()).title()

    # --- Phone cleaning ---
    phone = i[1]
    digits_only = ""
    for char in phone:
        if char.isdigit():
            digits_only += char
    if len(digits_only) == 10:
        phone = f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    else:
        phone = phone.strip()

    # --- Email cleaning ---
    # Strip spaces and make all characters lowercase
    email = i[2].strip().lower()

    # --- Address cleaning ---
    # Split address into words and check for state abbreviations
    address_parts = i[3].strip().split()
    formatted_address_parts = []
    for part in address_parts:
        # If part is 2 letters and all letters (state), make uppercase
        if len(part) == 2 and part.isalpha():
            formatted_address_parts.append(part.upper())
        else:
            # Otherwise, title-case it
            formatted_address_parts.append(part.title())
    address = " ".join(formatted_address_parts)

    # Add cleaned info as a simple list
    cleaned_contacts.append([name, phone, email, address])

# === OUTPUT PHASE ===
# Print all sections of the formatted directory

# --- Contact Directory Section ---
print("\n=== CONTACT DIRECTORY ===\n")

count = 1  # Start the counter at 1
for contact in cleaned_contacts:
    print(f"CONTACT {count}:")
    print(f"Name:     {contact[0]}")
    print(f"Phone:    {contact[1]}")
    print(f"Email:    {contact[2]}")
    print(f"Address:  {contact[3]}\n")
    count += 1  # Increase the counter by 1 for the next contact

# --- Directory Summary Section ---
print("=== DIRECTORY SUMMARY ===")
print(f"Total contacts processed: {len(cleaned_contacts)}\n")

# --- Formatted for Printing Section ---
print("=== FORMATTED FOR PRINTING ===")
for contact in cleaned_contacts:
    # Split full name into parts to get last name and first names
    name_parts = contact[0].split()
    last_name = name_parts[-1]
    first_names = " ".join(name_parts[:-1])
    # Align columns using f-string width specifiers
    print(f"{last_name}, {first_names:<25}{contact[1]:<20}{contact[2]}")
