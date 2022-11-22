# %%
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import mysql_pack
import course_pack
import ppa_pack
import cor_selectioneye_pack
import cor_obp_selectball_pack
import time

# 時間計測開始
t_time_start = time.time()

# チーム
t_team_list = [
    'ヤクルト',
    '巨人',
    'DeNA',
    '中日',
    '阪神',
    '広島',
    '西武',
    '日本ハム',
    'ロッテ',
    'オリックス',
    'ソフトバンク',
    '楽天',
]

# 各チームごとのループ処理
for t_team in t_team_list:
    # 各年度ごとのループ処理
    for t_year_idx in range(2012, 2023, 1):
    # mysqlからデータ取得
        t_rows = mysql_pack.sql_mod.get_batter_course_fnc(t_team, t_year_idx)
        t_np_array = np.array(t_rows)

        # 解析(プロット用データ整理)
        # ## コース別打率
        course_pack.average_mod.plot_average_fnc(t_team, t_year_idx, t_np_array)

        # # ## ppa計算
        ppa_pack.ppa_calc_mod.calc_fnc(t_team, t_year_idx, t_np_array)

        # # ## 選球眼解析(selectioneye)
        cor_selectioneye_pack.selectioneye_mod.selectioneye_fnc(t_team, t_year_idx, t_np_array)

        # ## 出塁率xボール球見極め率相関
        cor_obp_selectball_pack.obp_selectball_mod.obp_selectball_fnc(t_team, t_year_idx, t_np_array)

# 時間計測終了
t_time_end = time.time()

# 経過時間計算 (秒)
t_elapsed_time = t_time_end - t_time_start
print(t_elapsed_time)