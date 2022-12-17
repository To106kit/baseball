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
    t_np_total_batter_list = np.empty((0,37), str)
    t_np_total_pitcher_list = np.empty((0,33), str)
    try:
        # 初期化
        t_def_table_row_length = 6
        t_col_def_start_batter_table = 0
        t_col_def_start_pitcher_table = 0
        t_col_def_for_batter_table = 37
        t_col_def_for_pitcher_table = 33

        # Beautifulsoupでデータを取得
        # requests1回につき1s待つ
        time.sleep(1)
        r = requests.get(a_totaldata_url)
        soup = BeautifulSoup(r.content, 'html.parser')

        # 通算成績行を取得(文字列)
        t_batter_total_str = soup.select('body > div > div.main > div:nth-child(7) > table > tbody')[0].text
        t_pitcher_total_str = soup.select('body > div > div.main > div:nth-child(9) > table > tbody')[0].text

        # 改行文字列系を削除し、空白行でリスト分割
        t_batter_total_list = t_batter_total_str.replace("\n","").replace("\r","").split() # 引数なしのsplitは空白文字列による分割
        # t_pitcher_total_list = t_pitcher_total_str.replace("\n","").replace("\r","").split() # 引数なしのsplitは空白文字列による分割
        t_pitcher_total_list = t_pitcher_total_str.replace("\r","")
        t_pitcher_total_list = t_pitcher_total_str.split('\n')
        t_pitcher_total_list = list(filter(None, t_pitcher_total_list))
        t_pitcher_total_list = list(filter(lambda x: x != '     ', t_pitcher_total_list))
        t_pitcher_total_list = [s.replace("     ", "") for s in t_pitcher_total_list]
        t_pitcher_total_list = list(filter(lambda x: x != '\r', t_pitcher_total_list))
        t_pitcher_total_list = [s.replace("\r", "") for s in t_pitcher_total_list]
        # テーブル風に整形(野手データ)
        for t_idx_batter in range(t_def_table_row_length):
            t_row_batter = t_batter_total_list[t_col_def_start_batter_table:t_col_def_start_batter_table+t_col_def_for_batter_table:1]

            t_np_total_batter_list = np.vstack([t_np_total_batter_list, t_row_batter])
            t_col_def_start_batter_table += t_col_def_for_batter_table

        # テーブル風に整形(投手データ)
        for t_idx_pitcher in range(t_def_table_row_length):
            t_row_pitcher = t_pitcher_total_list[t_col_def_start_pitcher_table:t_col_def_start_pitcher_table+t_col_def_for_pitcher_table:1]

            t_np_total_pitcher_list = np.vstack([t_np_total_pitcher_list, t_row_pitcher])
            t_col_def_start_pitcher_table += t_col_def_for_pitcher_table

        print("test")

    except Exception as e:
        # 基本設計書の例外定義を参照すること。
        # 例外処理として、すべてノーデータとして埋め、SQLへ登録する。
        print("例外args:", e.args)


    return t_np_total_batter_list, t_np_total_pitcher_list

if __name__ == "__main__":
    import sys
