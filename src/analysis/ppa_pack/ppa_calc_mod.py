import matplotlib.pyplot as plt
import numpy as np
import os
from globaldef_pack import globalvalue_mod as g
import common_fnc_pack

def calc_fnc(a_team, a_year_idx, a_np_array):
    # 初期化
    t_ppa_list = np.empty((0,2), str)
    t_team = a_team
    t_year_idx = a_year_idx
    t_result_base_path = g.g_ppa_result_base_path

    # 年度別の結果格納フォルダを作成
    t_result_path = os.path.join(t_result_base_path, str(t_year_idx))
    os.makedirs(t_result_path, exist_ok=True)

    # 解析対象外を除外する
    t_np_array = common_fnc_pack.exclude_data_mod.exclude_batter_data_fnc(a_np_array)

    # 選手名
    t_player_name = common_fnc_pack.get_batter_data_mod.get_playername_fnc(t_np_array)

    # PPA計算
    t_ppa = common_fnc_pack.calc_ppa_mod.ppa_cals_fnc(t_np_array)

    # プロット
    fig, ax = plt.subplots(figsize=(6, 2.5))
    ax.set_ylim(0.0,5.0)
    ax.bar(t_player_name, t_ppa)

    fig.autofmt_xdate(rotation=30, ha="center")
    plt.tick_params(labelsize=5)

    plt.savefig(os.path.join(t_result_path, t_team + "ppa.png"), format="png", dpi=300)
    plt.close()

if __name__ == "__main__":
    import sys
    import os
    print('getcwd:      ', os.getcwd())
    print('__file__:    ', __file__)
    print('basename:    ', os.path.basename(__file__))
    print('dirname:     ', os.path.dirname(__file__))