from prettytable import PrettyTable
from typing import Iterable, List, Tuple

def print_results_as_table(data: Iterable[Tuple], column_names: List[str]) -> None:
    """
    Displays the query results as a table with pagination.
    The user can choose to display the next batch of rows or exit.

    Args:
        data (Iterable[Tuple]): The data to display, where each element is a row (e.g., list of tuples).
                                 This can be any iterable containing rows of data.
        column_names (List[str]): A list of strings representing the names of the table columns.
                                   Each string corresponds to a column in the table.

    Returns:
        None: This function does not return a value. It prints the table to the console.
    """
    # Convert data to a list if it's not already, so we can count its length.
    data_list = list(data)
    total_rows = len(data_list)

    print(f"\nTotal rows found: {total_rows}\n")

    table = PrettyTable()
    table.field_names = ['№'] + column_names
    table.align = "l"

    row_count = 0
    for row in data_list:
        table.add_row([row_count + 1] + list(row))
        row_count += 1

        # Pause after every 10 rows
        if row_count % 10 == 0:
            print(table)
            table.clear_rows()  # Clear rows for the next batch

            choice = input(f"\nDisplayed {row_count} out of {total_rows} rows. Press 'y' to show the next 10 rows, or any other key to exit: ").lower()
            if choice != 'y':
                return

    # Print remaining rows, if any
    if table.rows:
        print(table)
        return

