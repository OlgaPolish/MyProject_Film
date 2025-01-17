### Project Description: Console Application for Movie Search

The project represents a console application for searching movies, which uses the Sakila database as the data source. The main goal of the system is to provide users with a convenient interface for finding movies of interest and obtaining information about them.

---

### Database
The application uses **MySQL** to store information about movies, categories, ratings, and search history. Students need to install the Sakila test database on a local server. Information about movies and related data is stored in a structured way, which facilitates access and manipulation of this data.

---

### Project Files
- **db.py**: Contains functions for connecting to the database and handling connection errors.
- **main.py**: The main file that launches the application and processes user input.
- **my_exceptions.py**: Defines functions for handling user requests to continue or exit.
- **print_results.py**: Responsible for displaying the query results in a tabular format with pagination.
- **queries.py**: Contains functions for executing various SQL queries, such as searching for movies, retrieving categories, and ratings.
- **ui.py**: Handles the user interface, including displaying the menu and processing user selections.

---

### Key Search Functions
- **Keyword Search**: Allows users to search for movies by description.
- **Category and Year Search**: Users can filter movies by selected category and year of release.
- **Rating and Year Search**: Provides the ability to search for movies by rating and year of release.
- **View Popular Queries**: Displays the most frequently executed search queries, stored in a separate database table.
- **Query Logging**: All user queries are saved in the history for further analysis.

---

### User Interface
The application's interface is simple and intuitive:
- Users can select actions from the menu, enter search parameters, and receive results in a tabular format.
- The results are displayed with pagination, allowing users to view the data in parts.

---

### Conclusion
This console application for movie search provides a powerful tool that can be useful for both end-users and developers who want to expand the functionality. The logging capabilities and error handling make the system reliable and convenient to use.

---

### Описание проекта: Поиск фильмов

Проект представляет собой консольное приложение для поиска фильмов, которое позволяет пользователям осуществлять поиск по различным критериям, таким как ключевые слова, категория, год выпуска и рейтинг. Основная цель системы - предоставить пользователям удобный интерфейс для нахождения интересующих их фильмов и получения информации о них.

---

### База данных
Используется **MySQL** для хранения информации о фильмах, категориях, рейтингах и истории запросов. В проекте определены две конфигурации базы данных: для чтения и записи. Информация о фильмах и связанных с ними данных храниться в структурированном виде, что облегчает доступ и манипуляции с этими данными.

---

### Файлы проекта
- **db.py**: Содержит функции для подключения к базе данных и обработки ошибок подключения.
- **main.py**: Основной файл, запускающий приложение и обрабатывающий пользовательский ввод.
- **my_exceptions.py**: Определяет функции для обработки пользовательских запросов на продолжение или выход.
- **print_results.py**: Отвечает за вывод результатов запросов в виде таблицы с пагинацией.
- **queries.py**: Содержит функции для выполнения различных SQL-запросов, таких как поиск фильмов, получение категорий и рейтингов.
- **ui.py**: Обрабатывает пользовательский интерфейс, включая отображение меню и обработку выбора пользователя.

---

### Основные функции поиска
- **Поиск по ключевым словам**: Позволяет пользователям искать фильмы по описанию.
- **Поиск по категории и году**: Пользователи могут фильтровать фильмы по выбранной категории и году выпуска.
- **Поиск по рейтингу и году**: Предоставляет возможность искать фильмы по рейтингу и году выпуска.
- **Просмотр популярных запросов**: Отображает наиболее часто выполняемые запросы.
- **Логирование запросов**: Все запросы пользователей сохраняются в истории для дальнейшего анализа.

---

### Пользовательский интерфейс
Интерфейс приложения простой и интуитивно понятный:
- Пользователи могут выбирать действия из меню, вводить параметры поиска и получать результаты в виде таблиц.
- Результаты отображаются с возможностью пагинации, что позволяет пользователям просматривать данные по частям.

---

### Заключение
Этот проект предоставляет мощный инструмент для поиска фильмов, который может быть полезен как для конечных пользователей, так и для разработчиков, желающих расширить функционал приложения. Возможности логирования и обработки ошибок делают систему надежной и удобной в использовании.
