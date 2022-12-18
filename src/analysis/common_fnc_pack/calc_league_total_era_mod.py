import numpy as np
import common_fnc_pack
import mysql_pack
from fractions import Fraction

# リーグ平均防御率を計算
def calc_league_total_era_fnc(a_year_idx, a_team):
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
    t_batter_data = mysql_pack.sql_mod.get_every_league_total(a_year_idx, t_league)
    t_np_batter_array = np.array(t_batter_data)

    # 計算(後にローカル関数化予定)
    # 自責点
    t_np_jisekiten = t_np_batter_array[:,22].astype(int)
    t_sum_jisekiten = np.sum(t_np_jisekiten)

    # 投球回合計
    t_np_innings = t_np_batter_array[:,12]
    t_innings_list = t_np_innings.tolist()
    t_innings_str = ' '.join(t_innings_list)
    t_innings_list = t_innings_str.split()
    for s in t_innings_list:
        t_fraction_innings = Fraction(s)
        t_innings_sum = t_innings_sum + t_fraction_innings

    # 防御率(era)を計算 : 防御率 ＝ 自責点×9÷投球回数
    t_era = t_sum_jisekiten * 9 / t_innings_sum

    return float(t_era)

# if __name__ == "__main__":
#     import sys
#     import os
#     calc_league_total_era_fnc(2022, 'DeNA') 