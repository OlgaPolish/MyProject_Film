import queries
import my_exceptions
from settings import COLORS
from typing import List, Tuple

def show_menu() -> str:
    """
    Displays the main user menu with available search options.

    Returns:
        str: Menu item selected by user (1-5)
    """
    print(f"{COLORS['blue']}\nYou can search movies by the following parameters: {COLORS['reset']}")
    print("1. Keyword in description.")
    print("2. Category and year.")
    print("3. Rating and year.")
    print("4. View popular queries.")
    print("5. Exit.")
    return input(f"{COLORS['blue']}\nSelect action {COLORS['reset']} (1-5): ").strip()

def choice_1(connection_query, connection_write) -> None:
    while True:
        keyword = input("Enter keyword: ").strip()
        if not keyword:
            if not my_exceptions.continue_or_exit("Keyword cannot be empty."):
                break
            continue

        print(f"{COLORS['blue']}Movies with keyword {keyword}{COLORS['reset']}")
        try:
            queries.search_by_keyword(connection_query, connection_write, keyword)
            break
        except RuntimeError as e:
            if not my_exceptions.continue_or_exit(f"{str(e)}. Try again?"):
                break

def choice_2(connection_query, connection_write) -> None:
    try:
        categories: List[Tuple[int, str]] = queries.get_categories(connection_query)
        if not categories:
            print("No categories available.")
            return

        print(f"{COLORS['blue']}\nAvailable categories:{COLORS['reset']}")
        for cat_id, cat_name in categories:
            print(f"{cat_id}: {cat_name}")

        while True:
            category_id = input("\nEnter category number: ").strip()
            try:
                category_id = my_exceptions.rating_validate(category_id, len(categories))
            except ValueError as e:
                if not my_exceptions.continue_or_exit(str(e)):
                    return
                continue

            while True:
                year: str = input("Enter year: ").strip()
                try:
                    year = my_exceptions.year_validate(year)
                    print(f"{COLORS['blue']}Movies in category {categories[category_id - 1][1]}, year: {year}{COLORS['reset']}")
                    if queries.get_movies_by_category(connection_query, connection_write, category_id, year):
                        return
                except ValueError as e:
                    if not my_exceptions.continue_or_exit(f"{COLORS['red']}{str(e)}.{COLORS['reset']}"):
                        return

    except RuntimeError as e:
        print(f"Error fetching categories: {e}")


def choice_3(connection_query, connection_write) -> None:
    try:
        ratings: List[Tuple[int, str, str]] = queries.get_ratings(connection_write)
        if not ratings:
            print("No rating categories available.")
            return

        print("\nList of available ratings:")
        for idx, min_rate, max_rate in ratings:
            print(f"{idx}: {min_rate}-{max_rate}")

        while True:
            choice_num = input("\nEnter rating number: ").strip()
            try:
                choice_num = my_exceptions.rating_validate(choice_num, len(ratings))
            except ValueError as e:
                if not my_exceptions.continue_or_exit(str(e)):
                    return
                continue

            rating_id = ratings[choice_num - 1][1]
            while True:
                year = input("Enter year: ").strip()
                try:
                    year = my_exceptions.year_validate(year)
                    print(f"{COLORS['blue']}Movies with rating {rating_id}, year: {year}{COLORS['reset']}")
                    if queries.search_by_rating_and_year(connection_query, connection_write, rating_id, year):
                        return
                except ValueError as e:
                    if not my_exceptions.continue_or_exit(f"{str(e)}. Try again?"):
                        return

    except RuntimeError as e:
        print(f"Error fetching ratings: {e}")


def choice_4(connection_write) -> None:
    """
    Handles displaying popular queries.

    Args:
        connection_write: Database connection object for writing

    Returns:
        None
    """
    try:
        queries.show_popular_queries(connection_write)
    except Exception as e:
        raise RuntimeError(f"Error fetching popular queries: {e}")
