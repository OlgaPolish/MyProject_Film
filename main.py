import ui
import db
def main():
    """
    Main function to run the movie search system.

    Establishes database connections and displays the main menu.
    Handles user choices for searching movies, viewing popular queries, and exiting the application.

    """
    try:
        connection_query = db.create_connection_mysql_db_query()
        connection_write = db.create_connection_mysql_db_write()
        print("\033[93m \nWelcome to the Movie Search System!\033[0m")
        while True:
            choice = ui.show_menu()

            if choice == "1":
                ui.choice_1(connection_query, connection_write)

            elif choice == "2":
                ui.choice_2(connection_query, connection_write)

            elif choice == "3":
                ui.choice_3(connection_query, connection_write)

            elif choice == "4":
                ui.choice_4(connection_write)
                input("\033[94mPress any key to continue...\033[0m")

            elif choice == "5":
                print("\033[93mGoodbye!\033[0m")
                break

            else:
                print("\033[96mInvalid choice, please try again\033[0m")

    finally:
        connection_query.close()
        connection_write.close()

if __name__ == "__main__":
    main()