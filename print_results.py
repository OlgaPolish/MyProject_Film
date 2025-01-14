from prettytable import PrettyTable

def print_results_as_table(data, column_names):
    """
    Displays the query results as a table with pagination.
    The user can choose to display the next batch of rows or exit.

    Args:
        data (iterable): The data to display, where each element is a row (e.g., list of tuples).
        column_names (list): The names of the table columns.

    Returns:
        None
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
                print("\nExiting...")
                return

    # Print remaining rows, if any
    if table.rows:
        print(table)

