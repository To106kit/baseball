import numpy as np
import common_fnc_pack
import mysql_pack
from fractions import Fraction

# リーグ平均防御率を計算
def calc_league_total_homerunallowed_fnc(a_year_idx, a_team):
    # 初期化
    t_era = ""
    t_league = ""
    t_innings_sum = Fraction(0)

    # チーム
    t_central_team_list = [
        'ヤクルト',
        '巨人',
        'DeNA',
        '中日',
        '阪神',
        '広島',
    ]

    t_pacific_team_list = [
        '西武',
        '日本ハム',
        'ロッテ',
        'オリックス',
        'ソフトバンク',
        '楽天',
    ]

    # チーム名からリーグを判定
    if a_team in t_central_team_list:
        t_league = "セ"
    elif a_team in t_pacific_team_list:
        t_league = "パ"

    # 投手mysqlからデータ取得
    # リーグ別
    t_pitcher_data = mysql_pack.sql_mod.get_every_league_total(a_year_idx, t_league)
    # セパ統一
    # t_pitcher_data = mysql_pack.sql_mod.get_both_league_total(a_year_idx)
    t_np_pitcher_array = np.array(t_pitcher_data)

    # 計算(後にローカル関数化予定)
    # 奪三振取得
    t_np_homerunallowed = t_np_pitcher_array[:,17]
    t_homerunallowed_list = t_np_homerunallowed.tolist()
    t_homerunallowed_str = ' '.join(t_homerunallowed_list)
    t_homerunallowed_str = t_homerunallowed_str.replace(',','')
    t_homerunallowed_list = t_homerunallowed_str.split()
    t_np_homerunallowed_list = np.array(t_homerunallowed_list)
    t_np_homerunallowed_list = t_np_homerunallowed_list.astype(int)

    t_sum_homerunallowed = np.sum(t_np_homerunallowed_list)

    return t_sum_homerunallowed

# if __name__ == "__main__":
#     import sys
#     import os
#     calc_league_total_era_fnc(2022, 'DeNA')