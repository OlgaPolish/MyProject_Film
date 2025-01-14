from print_results import print_results_as_table

def get_categories(connection_query):
    """
    Retrieve a list of categories from the database.

    Args:
        connection_query (object): Database connection object for querying data.

    Returns:
        list: A list of tuples containing category_id and name.

    Raises:
        RuntimeError: If no categories are found in the database.
    """
    query = "SELECT category_id, name FROM category;"
    results = execute_query(connection_query, query)
    if results:
        return results
    else:
        raise RuntimeError("No categories found.")

def search_by_keyword(connection_query, connection_write, keyword):
    """
    Search for films by a keyword in their description.

    Args:
        connection_query (object): Database connection object for querying data.
        connection_write (object): Database connection object for logging queries.
        keyword (str): The keyword to search for in film descriptions.

    Raises:
        RuntimeError: If no films are found for the given keyword.
    """
    query = "SELECT title, description, release_year FROM film WHERE description LIKE %s;"
    results = execute_query(connection_query, query, (f"%{keyword}%",))
    if results:
        print_results_as_table(results, ["Title", "Description", "Year"])
        log_query(connection_write, query, "keyword", keyword)
    else:
        raise RuntimeError("No results found for the given keyword.")

def get_ratings(connection_write):
    """
    Retrieve a list of available ratings from the database.

    Args:
        connection_write (object): Database connection object for querying data.

    Returns:
        list: A list of tuples containing rating_id, rating_code, and description.

    Raises:
        RuntimeError: If no ratings are found in the database.
    """
    query = "SELECT rating_id, rating_code, description FROM movie_ratings;"
    results = execute_query(connection_write, query)
    if results:
        return results
    else:
        raise RuntimeError("No ratings found.")

def get_movies_by_category(connection_query, connection_write, category_id, year):
    """
    Retrieve a list of movies for a specific category and release year.

    Args:
        connection_query (object): Database connection object for querying data.
        connection_write (object): Database connection object for logging queries.
        category_id (int): The ID of the category to filter by.
        year (int): The release year to filter by.

    Returns:
        bool: Returns True if the operation is successful.

    Raises:
        RuntimeError: If no movies are found for the specified category and year.
        ValueError: If there is an issue with the input values.
        RuntimeError: For any unexpected errors during execution.
    """
    try:
        query = """
        SELECT film.title, film.release_year, film.description
        FROM film
        INNER JOIN film_category ON film.film_id = film_category.film_id
        WHERE film_category.category_id = %s AND film.release_year = %s;
        """
        results = execute_query(connection_query, query, (category_id, year))
        if results:
            log_query(connection_write, query, "category_and_year", f"Category ID: {category_id}, Year: {year}")
            print_results_as_table(results, ["Title", "Year", "Description"])
        else:
            raise RuntimeError(f"No movies found for category {category_id} for the year {year}.")
    except ValueError as e:
        raise ValueError(f"Input Error: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
    return True

def search_by_rating_and_year(connection_query, connection_write, rating, year):
    """
    Search for films by rating and release year.

    Args:
        connection_query (object): Database connection object for querying data.
        connection_write (object): Database connection object for logging queries.
        rating (str): The rating to filter by (e.g., 'PG', 'R').
        year (int): The release year to filter by.

    Returns:
        bool: Returns True if the operation is successful.

    Raises:
        RuntimeError: If no movies are found for the specified rating and year.
        ValueError: If there is an issue with the input values.
        RuntimeError: For any unexpected errors during execution.
    """
    try:
        query = """
        SELECT f.title, f.release_year, f.description
        FROM sakila.film f
        JOIN Project_OlgaP.movie_ratings mr ON f.rating = mr.rating_code
        WHERE f.rating = %s AND f.release_year = %s;
        """
        results = execute_query(connection_query, query, (rating, year))
        if results:
            log_query(connection_write, query, "rating_and_year", f"Rating: {rating}, Year: {year}")
            print_results_as_table(results, ["Title", "Year", "Rating"])
        else:
            raise RuntimeError(f"No movies found for rating {rating} for the year {year}.")
    except ValueError as e:
        raise ValueError(f"Input Error: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
    return True

def show_popular_queries(connection_write):
    """
    Display the most popular queries based on their frequency.

    Args:
        connection_write (object): Database connection object for querying data.

    Raises:
        RuntimeError: If no popular queries are found in the database.
    """
    query = """
    SELECT Query_type, COUNT(*) AS Query_Count
    FROM History
    GROUP BY Query_type
    ORDER BY Query_Count DESC;
    """
    results = execute_query(connection_write, query)
    if results:
        print_results_as_table(results, ["Query Type", "Count"])
    else:
        raise RuntimeError("No popular queries found.")

def log_query(connection_write, query_text, query_type, keyword):
    """
    Log a query into the query history table.

    Args:
        connection_write (object): Database connection object for writing data.
        query_text (str): The SQL query text to log.
        query_type (str): The type of query being logged (e.g., 'keyword', 'rating_and_year').
        keyword (str): Additional information or the keyword used in the query.
    """
    insert_query = """
    INSERT INTO History (Text_query, Query_type, Keyword)
    VALUES (%s, %s, %s);
    """
    execute_query(connection_write, insert_query, (query_text, query_type, keyword))

def execute_query(connection, query, parameters=None):
    """
    Executes a SQL query on the provided database connection.

    Args:
        connection (object): A database connection object, typically created using a library like MySQLdb or pymysql.
        query (str): The SQL query to execute.
        parameters (tuple, optional): Parameters to safely insert into the query. Defaults to None.

    Returns:
        list: If the query is a SELECT statement, returns a list of tuples containing the fetched rows.
        None: If the query is not a SELECT statement, commits the changes and returns nothing.

    Raises:
        RuntimeError: If there is an error during query execution, it raises a RuntimeError with the error message.

    Notes:
        - For SELECT queries, the function fetches and returns all rows.
        - For non-SELECT queries (e.g., INSERT, UPDATE, DELETE), the function commits the transaction.
        - In case of an error, the transaction is rolled back to maintain database integrity.
    """
    cursor = connection.cursor()
    try:
        # Execute the query with provided parameters or an empty tuple if no parameters are given
        cursor.execute(query, parameters if parameters is not None else ())

        # If the query is a SELECT statement, fetch and return the results
        if query.strip().lower().startswith("select"):
            return cursor.fetchall()
        else:
            # Commit the transaction for non-SELECT queries
            connection.commit()
    except MySQLError as e:
        # Rollback the transaction in case of an error
        connection.rollback()
        raise RuntimeError(f"An error occurred during query execution: {e}")
    finally:
        # Ensure the cursor is closed to release resources
        cursor.close()