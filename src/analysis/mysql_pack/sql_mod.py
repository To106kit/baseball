# MYSQLdbのインポート
import MySQLdb

def get_batter_course_fnc(a_team, a_year_idx):

    # DBへの接続とカーソルの生成
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='to106kita9ma',
        # db='python_db',
        db='python_test',
        # テーブル内部で日本語を扱うために追加
        charset='utf8'
    )

    cursor = connection.cursor()
    # SQL文
    t_sql_str = "SELECT * from batter_course_list where year = %s and team = %s"
    cursor.execute(t_sql_str, (a_year_idx, a_team,))
    # cursor.execute("SELECT * from batter_course_list where year = '2022' and team = 'ヤクルト'")

    # 全てのデータを取得
    r_rows = cursor.fetchall()
    return r_rows

def get_pitcher_course_fnc(a_team, a_year_idx):

    # DBへの接続とカーソルの生成
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='to106kita9ma',
        # db='python_db',
        db='python_test',
        # テーブル内部で日本語を扱うために追加
        charset='utf8'
    )

    cursor = connection.cursor()
    # SQL文
    t_sql_str = "SELECT * from pitcher_course_list where year = %s and team = %s"
    cursor.execute(t_sql_str, (a_year_idx, a_team,))
    # cursor.execute("SELECT * from batter_course_list where year = '2022' and team = 'ヤクルト'")

    # 全てのデータを取得
    r_rows = cursor.fetchall()
    return r_rows

def get_every_league_total(a_year_idx, a_league):

    # DBへの接続とカーソルの生成
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='to106kita9ma',
        # db='python_db',
        db='python_test',
        # テーブル内部で日本語を扱うために追加
        charset='utf8'
    )

    cursor = connection.cursor()
    # SQL文
    t_sql_str = "SELECT * from total_pitcher_list where year = %s and league = %s"
    cursor.execute(t_sql_str, (a_year_idx, a_league,))

    # 全てのデータを取得
    r_rows = cursor.fetchall()
    return r_rows

def get_both_league_total(a_year_idx):

    # DBへの接続とカーソルの生成
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='to106kita9ma',
        # db='python_db',
        db='python_test',
        # テーブル内部で日本語を扱うために追加
        charset='utf8'
    )

    cursor = connection.cursor()
    # SQL文
    t_sql_str = "SELECT * from total_pitcher_list where year = %s"
    cursor.execute(t_sql_str, (a_year_idx,))

    # 全てのデータを取得
    r_rows = cursor.fetchall()
    return r_rows