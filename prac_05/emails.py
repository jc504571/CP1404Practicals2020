
def main():
    """Creating dictionary of emails-to-names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)