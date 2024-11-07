"""
CP1404 prac 5
emails
"""

# lindsay.ward@gmail.com
email_to_name = {}
email = input("Email: ")
while email != "":
    parts = email.split('@')[0]
    more_parts = parts.split('.')
    possible_name = " ".join(more_parts).title()
    possible_name_confirmation = input(f"Is your name {possible_name}? (Y/N) ").upper()
    if possible_name_confirmation != "" and possible_name_confirmation != "Y":
        name = input("Name: ")
    else:
        name = possible_name
    email_to_name[email] = name
    email = input("Email: ")
for email, name in email_to_name.items():
    print(f"{name} ({email})")
