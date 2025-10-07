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
        # Add this raw contact data to the contacts list
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

    # Extract only digits from the phone number
    for char in phone:
        if char.isdigit():
            digits_only += char

    # If there are exactly 10 digits, format into (XXX) XXX-XXXX
    if len(digits_only) == 10:
        phone = f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    else:
        # If phone format is incorrect, just strip spaces
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

    # Rejoin all address parts into one clean string
    address = " ".join(formatted_address_parts)

    # Add cleaned data as a dictionary into the main list
    cleaned_contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

# === OUTPUT PHASE ===
# Print all sections of the formatted directory

# --- Contact Directory Section ---
print("\n=== CONTACT DIRECTORY ===\n")

# Loop through each cleaned contact and display their info
for i, c in enumerate(cleaned_contacts, start=1):
    print(f"CONTACT {i}:")
    print(f"Name:     {c['name']}")
    print(f"Phone:    {c['phone']}")
    print(f"Email:    {c['email']}")
    print(f"Address:  {c['address']}\n")

# --- Directory Summary Section ---
print("=== DIRECTORY SUMMARY ===")
print(f"Total contacts processed: {len(cleaned_contacts)}\n")

# --- Formatted for Printing Section ---
# Print each contact in “Last, First” format for professional printing
print("=== FORMATTED FOR PRINTING ===")
for c in cleaned_contacts:
    # Split full name to separate last and first names
    name_parts = c['name'].split()
    last_name = name_parts[-1]  # Last element is the last name
    first_names = " ".join(name_parts[:-1])  # Everything before last name

    # Align columns using f-string width specifiers
    print(f"{last_name}, {first_names:<25}{c['phone']:<20}{c['email']}")
