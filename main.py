from db import create_connection_mysql_db_query, create_connection_mysql_db_write
from ui import *
from queries import *

def main():
    try:
        connection_query = create_connection_mysql_db_query()
        connection_write = create_connection_mysql_db_write()
        print("\nДобро пожаловать в систему поиска фильмов!")

        while True:
            choice = show_menu()

            if choice == "1":
                choice_1(connection_query, connection_write)

            elif choice == "2":
                choice_2(connection_query, connection_write)

            elif choice == "3":
                choice_3(connection_query, connection_write)
            elif choice == "4":
                try:
                    show_popular_queries(connection_write)
                except (ValueError, RuntimeError) as e:
                    if not continue_or_exit(f"{str(e)}. Try again?"):
                        break
                    continue
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Некорректный выбор, попробуйте снова")

    finally:
        if 'connection_query' in locals():
            connection_query.close()
        if 'connection_write' in locals():
            connection_write.close()


if __name__ == "__main__":
    main()
