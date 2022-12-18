from getdata_pack import get_totaldata_mod
from lib_pack import makedict_mod
from mysql_pack import total_sql_mod
import sendgmail_pack
import time_pack
import numpy as np
import re
import os
import urllib
import time
from globaldef_pack import globalvalue_mod as g

############################## クラス定義 ##################################
############################## クラス定義 ##################################

# 時間計測開始
t_time_sta = time.time()

# 初期化
t_np_batter_total_list_for_sql= np.empty((0,39), str)
t_np_pitcher_total_list_for_sql= np.empty((0,35), str)
t_unit_flag = "sec"
t_totaldata_url = ""

# データ取得対象球団のベースとなるページurlリスト
## TODO: 全体url global変数に登録するべき
t_url_totaldata_list = [
        ["https://baseballdata.jp/c/", "セ"],
        ["https://baseballdata.jp/p/", "パ"],
    ]
## TODO: 全体url global変数に登録するべき

# セ・パループ
for t_league_idx in t_url_totaldata_list:
    # 年度別url作成
    for t_year_idx in range(2012, 2023, 1):
        # 前年度までのシーズンのデータを取得
        print(str(t_year_idx)+"年")
        if t_year_idx != 2022:
            # ベースデータ取得用url(年度別)を作成
            t_totaldata_split = t_league_idx[0].split('/')
            t_totaldata_replace = t_totaldata_split.copy()
            t_totaldata_replace.insert(3, str(t_year_idx))
            t_totaldata_url = '/'.join(t_totaldata_replace)
        # 今シーズンのデータを取得
        elif t_year_idx == 2022:
            t_totaldata_url = t_league_idx[0]

        # トータルデータからmysql用データを取得
        t_np_total_batter_list, t_np_total_pitcher_list = get_totaldata_mod.get_total_data(t_totaldata_url)

        m, n = t_np_total_batter_list.shape
        # リーグを挿入(野手)
        t_np_total_batter_list = np.c_[np.full(m, t_league_idx[1]), t_np_total_batter_list]
        # 年度を挿入(野手)
        t_np_total_batter_list = np.c_[np.full(m, t_year_idx), t_np_total_batter_list]
        t_np_batter_total_list_for_sql  = np.vstack([t_np_batter_total_list_for_sql, t_np_total_batter_list])

        m, n = t_np_total_pitcher_list.shape
        # リーグを挿入(投手)
        t_np_total_pitcher_list = np.c_[np.full(m, t_league_idx[1]), t_np_total_pitcher_list]
        # 年度を挿入(投手)
        t_np_total_pitcher_list = np.c_[np.full(m, t_year_idx), t_np_total_pitcher_list]
        t_np_pitcher_total_list_for_sql  = np.vstack([t_np_pitcher_total_list_for_sql, t_np_total_pitcher_list])

print("unko")

# mysqlへ登録
## 野手データをmysqlに登録
try:
    total_sql_mod.set_sql_batter_total(t_np_batter_total_list_for_sql)
except Exception as e:
    print("例外args:", e.args)

## 投手データをmysqlに登録
try:
    total_sql_mod.set_sql_pitcher_total(t_np_pitcher_total_list_for_sql)
except Exception as e:
    print("例外args:", e.args)

# 時間計測終了
t_time_end = time.time()
# 経過時間（min）
t_time, t_unit_flag = time_pack.calc_exec_time_mod.calc_exec_time_fnc(t_time_sta, t_time_end)

# gmailへ実行完了メールを送信
sendgmail_pack.sendgmail_mod.sendgmail(t_time, t_unit_flag)

print("########## all end ################")


