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


def main():
    initialize_database()

    # 以下から書き始めること！


if __name__ == '__main__':
    main()
