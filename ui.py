from queries import *
from my_exceptions import continue_or_exit
def show_menu():
    """
    Отображение меню пользователя.
    """
    print("\nВы можете искать фильмы по следующим параметрам:")
    print("1. Ключевое слово в описании.")
    print("2. Категория и год.")
    print("3. Рейтинг и год.")
    print("4. Просмотр популярных запросов.")
    print("5. Выход.")
    return input("\nВыберите действие (1-5): ").strip()

def choice_1(connection_query, connection_write):
    while True:
        keyword = input("Введите ключевое слово: ").strip()
        if keyword:
            try:
                search_by_keyword(connection_query, connection_write, keyword)
            except (Exception, ValueError, RuntimeError) as e:
                if not continue_or_exit(f"{str(e)}. Try again?"):
                    break

                continue
            break
        if not continue_or_exit("Ключевое слово не может быть пустым."):
            break

def choice_2(connection_query, connection_write):
    while True:

        try:

            categories = get_categories(connection_query)

        except Exception as e:

            raise RuntimeError(f"Error fetching categories: {e}")

        if categories:

            print("\nДоступные категории:")

            for category in categories:
                print(f"{category[0]}: {category[1]}")

            category_id = input("\nВведите номер категории: ").strip()

            if category_id.isdigit():

                category_id = int(category_id)

                if any(cat[0] == category_id for cat in categories):

                    while True:

                        year = input("Введите год:").strip()

                        if year.isdigit():

                            year = int(year)

                            try:
                                print(f"\033[91mФильмы категории {categories[category_id - 1][1]}, год: {year}\033[0m")
                                if get_movies_by_category(connection_query, connection_write, category_id, year):
                                    break

                                continue

                            except (ValueError, RuntimeError) as e:

                                if not continue_or_exit(f"{str(e)}. Try again?"):
                                    break

                                continue

                        if not continue_or_exit("Пожалуйста, введите корректный ГОД"):
                            break

                    break

                else:

                    print("Неверный идентификатор категории.")

            else:

                if not continue_or_exit("Неверный идентификатор категории"):
                    break

        else:

            print("Нет доступных категорий.")

            break


def choice_3(connection_query, connection_write):
    """
    Поиск фильмов по рейтингу и году.
    """
    while True:
        try:
            categories = get_ratings(connection_write)
        except Exception as e:
            raise RuntimeError(f"Error fetching categories: {e}")

        if categories:
            print("\nСписок возможных рейтингов:")
            for category in categories:
                print(f"{category[0]}: {category[1]}-{category[2]}")

            choice_num = input("\nВведите номер рейтинга: ").strip()
            if choice_num.isdigit():
                choice_num = int(choice_num)
                if 1 <= choice_num <= len(categories):
                    category_id = categories[choice_num - 1][1]
                    while True:
                        year = input("Введите год:").strip()
                        if year.isdigit():
                            year = int(year)
                            try:
                                print(f"\033[94mФильмы рейтинга {category_id}, год: {year}\033[0m")
                                if search_by_rating_and_year(connection_query, connection_write,
                                                             category_id, year):
                                    break
                                continue
                            except (ValueError, RuntimeError) as e:
                                if not continue_or_exit(f"{str(e)}. Try again?"):
                                    break
                                continue
                        if not continue_or_exit("Пожалуйста, введите корректный ГОД"):
                            break
                    break
                else:
                    print("Неверный идентификатор категории.")
            else:
                if not continue_or_exit("Неверный идентификатор категории"):
                    break
        else:
            print("Нет доступных категорий.")
            break


