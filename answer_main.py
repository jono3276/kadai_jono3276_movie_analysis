import sqlite3
from pathlib import Path
from typing import List, Dict

"""
回答例
"""


def initialize_database() -> None:
    # このコードは改変しないこと
    root_path = Path(__file__).parent

    db_path = root_path / 'my_movies.db'
    conn = sqlite3.connect(db_path)

    init_sql_path = root_path / 'init.sql'
    conn.executescript(init_sql_path.read_text())

    conn.close()


def fetch_amount_income_each_genre(conn: sqlite3.Connection) -> List[Dict]:
    sql = """
        SELECT genre, sum(income) FROM my_movies 
        GROUP BY genre
        ORDER BY sum(income) DESC;
    """

    rows = conn.execute(sql).fetchall()

    # 自分が使いたいデータ型(List[Dict])に変換している
    results = []

    for genre, amount_income in rows:
        result = dict(genre=genre, amount_income=amount_income)

        results.append(result)

    return results


def to_csv(results: List[Dict], save_file_path: str) -> None:
    with open(save_file_path, mode='w') as f:
        for result in results:
            genre = result['genre']
            amount_income = result['amount_income']

            # print(msg, file=f)
            f.write(f'{genre},{amount_income}\n')


def main():
    initialize_database()

    # 以下から書き始めること！
    conn = sqlite3.connect('my_movies.db')
    results = fetch_amount_income_each_genre(conn)

    save_file_path = 'output.csv'

    to_csv(results, save_file_path)


if __name__ == '__main__':
    main()
