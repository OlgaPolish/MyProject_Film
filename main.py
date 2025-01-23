import ui
import db
from settings import COLORS,MENU_ITEMS
import my_exceptions

def main():
    """
    Main function to run the movie search system.
    Establishes database connections and displays the main menu.
    Handles user choices for searching movies, viewing popular queries, and exiting the application.
    """
    connection_query = None
    connection_write = None
    try:
        connection_query = db.create_connection_mysql_db_query()
        connection_write = db.create_connection_mysql_db_write()
        print(f"{COLORS['yellow']} \nWelcome to the Movie Search System!{COLORS['reset']}")
        while True:
            ui.show_menu(MENU_ITEMS)
            choice = input(f"{COLORS['blue']}Select action {COLORS['reset']} (1-5): ").strip()

            if choice == "1":
                ui.choice_1(connection_query, connection_write)

            elif choice == "2":
                ui.choice_2(connection_query, connection_write)


            elif choice == "3":
                ui.choice_3(connection_query, connection_write)

            elif choice == "4":
                ui.choice_4(connection_write)
#                input(f"{COLORS['blue']} \nPress any key to continue...{COLORS['reset']}")

            elif choice == "5":
                print(f"{COLORS['yellow']}Goodbye!{COLORS['reset']}")
                break
            else:
                print(f"{COLORS['red']}Invalid choice, please try again{COLORS['reset']}")

    # except my_exceptions.DBConnectionError as e:
    #     print(f"{COLORS['red']}Error: {e}{COLORS['reset']}")
    except Exception as e:
        print(f"{COLORS['green']}An unexpected error occurred: {e}{COLORS['reset']}")
    finally:
        if connection_query:
            connection_query.close()
        if connection_write:
            connection_write.close()


if __name__ == "__main__":
    main()
