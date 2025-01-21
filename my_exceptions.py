class DBConnectionError(Exception):
    """Raised when there is an error connecting to the database."""
    pass

class InvalidInputError(Exception):
    """Raised when the user input is invalid."""
    pass

class NoResultsError(Exception):
    """Raised when no results are found for a query."""
    pass

class QueryExecutionError(Exception):
    """Raised when there is an error executing a SQL query."""
    pass

def continue_or_exit(message: str) -> bool:
    """
    Prompts the user to continue or exit based on their input.

    Args:
        message (str): The message to display to the user prompting them for input.

    Returns:
        bool: Returns True if the user chooses to continue ('y'),
              and False if the user chooses to exit (any other key).
    """

    choice = input(f"{message} Please enter 'y' to continue or any other key to exit: ").strip().lower()
    if choice == "y":
        return True
    else:
        return False

def year_validate(year: str) -> int:
    """
    Validates the input year.

    Args:
        year (str): The year input as a string.

    Returns:
        int: Returns the validated year as an integer.

    Raises:
        ValueError: If the input year is invalid.
    """
    try:
        year_int = int(year)
        if year_int < 1888:  # For example, the first film was made in 1888
            raise ValueError("Year must be greater than or equal to 1888.")
        return year_int
    except ValueError:
        raise ValueError("Please enter a valid year.")


def rating_validate(choice_num: str, max_rating: int) -> int:
    """
    Validates the rating number input by the user.

    Args:
        choice_num (str): The input from the user.
        max_rating (int): The maximum valid rating number.

    Returns:
        int: The validated rating number.

    Raises:
        ValueError: If the input is invalid.
    """
    if not choice_num.isdigit():
        raise ValueError("Invalid rating ID")

    choice_num = int(choice_num)
    if not 1 <= choice_num <= max_rating:
        raise ValueError("Rating ID out of range")

    return choice_num

