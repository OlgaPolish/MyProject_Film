def continue_or_exit(message):
    """
    Prompts the user to continue or exit based on their input.

    Args:
        message (str): The message to display to the user prompting them for input.

    Returns:
        bool: Returns True if the user chooses to continue ('y'),
              and False if the user chooses to exit (any other key).
    """
    while True:
        choice = input(f"{message} Please enter 'y' to continue or any other key to exit: ").strip().lower()
        if choice == "y":
            return True
        else:
            return False
