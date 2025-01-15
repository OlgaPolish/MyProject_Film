from queries import *
from my_exceptions import continue_or_exit
from typing import List, Tuple

def show_menu() -> str:
    """
    Displays the main user menu with available search options.

    Returns:
        str: Menu item selected by user (1-5)
    """
    print("\033[94m \nYou can search movies by the following parameters: \033[0m")
    print("1. Keyword in description.")
    print("2. Category and year.")
    print("3. Rating and year.")
    print("4. View popular queries.")
    print("5. Exit.")
    return input("\033[94m\nSelect action \033[0m (1-5): ").strip()

def choice_1(connection_query, connection_write) -> None:
    """
    Handles movie search by keyword.

    Args:
        connection_query: Database connection object for queries
        connection_write: Database connection object for writing

    Returns:
        None
    """
    while True:
        keyword = input("Enter keyword: ").strip()
        if not keyword:
            if not continue_or_exit("Keyword cannot be empty."):
                break
            continue

        try:
            print(f"\033[35mMovies with keyword {keyword} \033[0m")
            search_by_keyword(connection_query, connection_write, keyword)
            break
        except (Exception, ValueError, RuntimeError) as e:
            if not continue_or_exit(f"{str(e)}. Try again?"):
                break

def choice_2(connection_query, connection_write) -> None:
    """
    Handles movie search by category and year.

    Args:
        connection_query: Database connection object for queries
        connection_write: Database connection object for writing

    Raises:
        RuntimeError: If error occurs while fetching categories

    Returns:
        None
    """
    try:
        categories: List[Tuple[int, str]] = get_categories(connection_query)
        if not categories:
            print("No categories available.")
            return

        print("\nAvailable categories:")
        for cat_id, cat_name in categories:
            print(f"{cat_id}: {cat_name}")

        while True:
            category_id = input("\nEnter category number: ").strip()
            if not category_id.isdigit():
                if not continue_or_exit("Invalid category ID"):
                    return
                continue

            category_id = int(category_id)
            if not any(cat[0] == category_id for cat in categories):
                print("Invalid category ID.")
                continue

            while True:
                year = input("Enter year: ").strip()
                if not year.isdigit():
                    if not continue_or_exit("Please enter a valid YEAR"):
                        return
                    continue

                try:
                    year = int(year)
                    print(f"\033[92mMovies in category {categories[category_id - 1][1]}, year: {year}\033[0m")
                    if get_movies_by_category(connection_query, connection_write, category_id, year):
                        return
                except (ValueError, RuntimeError) as e:
                    if not continue_or_exit(f"{str(e)}. Try again?"):
                        return

    except Exception as e:
        raise RuntimeError(f"Error fetching categories: {e}")

def choice_3(connection_query, connection_write) -> None:
    """
    Handles movie search by rating and year.

    Args:
        connection_query: Database connection object for queries
        connection_write: Database connection object for writing

    Raises:
        RuntimeError: If error occurs while fetching ratings

    Returns:
        None
    """
    try:
        ratings: List[Tuple[int, str, str]] = get_ratings(connection_write)
        if not ratings:
            print("No rating categories available.")
            return

        print("\nList of available ratings:")
        for idx, min_rate, max_rate in ratings:
            print(f"{idx}: {min_rate}-{max_rate}")

        while True:
            choice_num = input("\nEnter rating number: ").strip()
            if not choice_num.isdigit():
                if not continue_or_exit("Invalid rating ID"):
                    return
                continue

            choice_num = int(choice_num)
            if not 1 <= choice_num <= len(ratings):
                print("Invalid rating ID.")
                continue

            rating_id = ratings[choice_num - 1][1]
            while True:
                year = input("Enter year: ").strip()
                if not year.isdigit():
                    if not continue_or_exit("Please enter a valid YEAR"):
                        return
                    continue

                try:
                    year = int(year)
                    print(f"\033[94mMovies with rating {rating_id}, year: {year}\033[0m")
                    if search_by_rating_and_year(connection_query, connection_write, rating_id, year):
                        return
                except (ValueError, RuntimeError) as e:
                    if not continue_or_exit(f"{str(e)}. Try again?"):
                        return

    except Exception as e:
        raise RuntimeError(f"Error fetching ratings: {e}")

def choice_4(connection_write) -> None:
    """
    Handles displaying popular queries.

    Args:
        connection_write: Database connection object for writing

    Returns:
        None
    """
    try:
        show_popular_queries(connection_write)
    except Exception as e:
        raise RuntimeError(f"Error fetching popular queries: {e}")
