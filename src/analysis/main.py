# %%
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import mysql_pack
import course_pack
import ppa_pack
import correlation_pack
import time
import common_fnc_pack

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
    # for t_year_idx in range(2022, 2023, 1):
    # 野手mysqlからデータ取得
        t_batter_data = mysql_pack.sql_mod.get_batter_course_fnc(t_team, t_year_idx)
        t_np_batter_array = np.array(t_batter_data)
    # 投手mysqlからデータ取得
        t_pitcher_data = mysql_pack.sql_mod.get_pitcher_course_fnc(t_team, t_year_idx)
        t_np_pitcher_array = np.array(t_pitcher_data)

        # # 解析(プロット用データ整理)
        # ## コース別打率
        # course_pack.average_mod.plot_average_fnc(t_team, t_year_idx, t_np_batter_array)

        # # ## ppa計算
        # ppa_pack.ppa_calc_mod.calc_fnc(t_team, t_year_idx, t_np_batter_array)

        # # ## 選球眼解析(selectioneye)
        # correlation_pack.correlation_selectioneye_mod.selectioneye_fnc(t_team, t_year_idx, t_np_batter_array)

        # # # ## 出塁率xボール球見極め率相関
        # correlation_pack.correlation_obp_selectball_mod.obp_selectball_fnc(t_team, t_year_idx, t_np_batter_array)

        # # # ## 相関解析(OPS vs PPA)
        # correlation_pack.correlation_ops_vs_ppa_mod.ops_vs_ppa_fnc(t_team, t_year_idx, t_np_batter_array)

        # # ## 相関解析(PPA vs 三振率)
        # correlation_pack.correlation_ppa_strikeoutrate_mod.ppa_vs_strikeoutrate_fnc(t_team, t_year_idx, t_np_batter_array)

        # # ## 相関解析(PPA vs SLG)
        # correlation_pack.correlation_ppa_vs_slg_mod.cor_ppa_vs_slg_fnc(t_team, t_year_idx, t_np_batter_array)

        # ## 相関解析(SLG vs OBP)
        # correlation_pack.correlation_slg_vs_obp_mod.slg_vs_obp_fnc(t_team, t_year_idx, t_np_batter_array)

        # ## 相関解析(PPA vs IsoP)
        # correlation_pack.correlation_ppa_vs_isop_mod.ppa_vs_isop_fnc(t_team, t_year_idx, t_np_batter_array)

        ## 相関解析(ボール球見逃し率 vs ストライクスイング率)
        # correlation_pack.correlation_ballnoswing_vs_strikeswing_mod.cor_ballnoswing_vs_strikeswing_fnc(t_team, t_year_idx, t_np_batter_array)

        ## 相関解析(バント成功率 vs battingeye(ボール球見極め率 + ストライクスイング率))
        # correlation_pack.correlation_buntsuccessrate_vs_battingeye_mod.buntsuccessrate_vs_battingeye_fnc(t_team, t_year_idx, t_np_batter_array)

        # # ## 相関解析(NOI vs PPA)
        # correlation_pack.correlation_noi_vs_ppa_mod.noi_vs_ppa_fnc(t_team, t_year_idx, t_np_batter_array)

        # 相関解析(IsoD vs PPA)
        # correlation_pack.correlation_isod_vs_ppa_mod.isod_vs_ppa_fnc(t_team, t_year_idx, t_np_batter_array)

        # try_fnc
        # correlation_pack.try_correlation_mod.try_fnc(t_team, t_year_idx, t_np_pitcher_array)
        # common_fnc_pack.calc_league_total_homerunallowed_mod.calc_league_total_homerunallowed_fnc(t_year_idx, t_team)
        correlation_pack.correlation_lob_vs_k9_mod.cor_lob_vs_k9_fnc(t_team, t_year_idx, t_np_pitcher_array)
# 時間計測終了
t_time_end = time.time()

# 経過時間計算 (秒)
t_elapsed_time = t_time_end - t_time_start
print(t_elapsed_time)