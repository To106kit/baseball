from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd

# TODO: feat: mysqlデータベース再構築(打者シート/投手シートリーグ別平均) #33
def get_total_data(a_totaldata_url):
    # ゼロの縦ベクトルを作成
    t_total_batter_list = np.empty((0,37), str)
    print(t_total_batter_list)
    try:
        # 初期化
        t_def_table_row_length = 6
        t_col_def_start_table = 0
        t_col_def_for_batting_table = 37
        t_row = []

        # Beautifulsoupでデータを取得
        # requests1回につき1s待つ
        time.sleep(1)
        r = requests.get(a_totaldata_url)
        soup = BeautifulSoup(r.content, 'html.parser')

        # 通算成績行を取得(文字列)
        # t_total_str = soup.select('body > div > div.main > div:nth-child(7) > table')[0].text
        t_total_str = soup.select('body > div > div.main > div:nth-child(7) > table > tbody')[0].text
        # 改行文字列系を削除し、空白行でリスト分割
        t_total_list = t_total_str.replace("\n","").replace("\r","").split() # 引数なしのsplitは空白文字列による分割

        # リスト風に整形
        for t_idx in range(t_def_table_row_length):
            print(t_total_list[t_col_def_start_table:t_col_def_start_table+t_col_def_for_batting_table:1])
            t_row = t_total_list[t_col_def_start_table:t_col_def_start_table+t_col_def_for_batting_table:1]

            t_total_batter_list = np.vstack([t_total_batter_list, t_row])
            t_col_def_start_table += t_col_def_for_batting_table

        print("test")

    except Exception as e:
        # 基本設計書の例外定義を参照すること。
        # 例外処理として、すべてノーデータとして埋め、SQLへ登録する。
        # t_basedata_list = ["---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---"]
        # t_exception_flag = True
        print("例外args:", e.args)


    return t_total_batter_list

if __name__ == "__main__":
    import sys
