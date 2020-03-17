MINIMUM_LENGTH = 4

def main():
    """Get and print password using functions."""
    password = get_password(MINIMUM_LENGTH)
    guess_password(password)


def guess_password(password):
    print_asterisks(password)