import sqlite3
from pathlib import Path


def initialize_database() -> None:
    # このコードは改変しないこと
    root_path = Path(__file__).parent

    db_path = root_path / 'my_movies.db'
    conn = sqlite3.connect(db_path)

    init_sql_path = root_path / 'init.sql'
    conn.executescript(init_sql_path.read_text())

    conn.close()

def fetch_income_genre() -> list:
    conn = sqlite3.connect('my_movies.db')
    sql = 'SELECT sum(income) AS sum_income, genre FROM my_movies GROUP BY genre ORDER BY sum_income DESC ;'

    return conn.execute(sql).fetchall()


def sort_genre_to_income(results_income_genre) -> list:
    genre_income_list = []
    for result in results_income_genre:
        sum_income, genre = map(str, result)
        genre_income_list.append(f'{genre},{sum_income}')
    return genre_income_list


def make_csv_file(genre_income_list):
    with open('output.csv', mode='w', encoding='utf-8') as f:
        output = '\n'.join(genre_income_list)
        f.write(output)



def main():
    initialize_database()

    # 以下から書き始めること！
    income_genre_list = fetch_income_genre()

    genre_income_list = sort_genre_to_income(income_genre_list)

    make_csv_file(genre_income_list)


if __name__ == '__main__':
    main()
