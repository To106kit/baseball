# %%
import numpy as np
import matplotlib.pyplot as plt
import os
from globaldef_pack import globalvalue_mod as g
import common_fnc_pack

def cor_ppa_vs_slg_fnc(a_team, a_year_idx, a_np_array):
    # チーム
    t_team = a_team
    t_year_idx = a_year_idx
    t_result_base_path = g.g_ppa_vs_slg_result_base_path

    # 年度別の結果格納フォルダを作成
    t_result_path = os.path.join(t_result_base_path, str(t_year_idx))
    os.makedirs(t_result_path, exist_ok=True)

    # 解析対象外を除外する
    t_np_array = common_fnc_pack.exclude_data_mod.exclude_data_fnc(a_np_array)

    # 選手名
    t_player_name = common_fnc_pack.get_data_mod.get_playername_fnc(t_np_array)

    # PPA計算
    t_ppa = common_fnc_pack.calc_ppa_mod.ppa_cals_fnc(t_np_array)

    #SLG計算
    t_slg = common_fnc_pack.calc_slg_mod.calc_slg_fnc(t_np_array)

    # 散布図を描画
    plt.rcParams["font.size"] = 8

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(
        111, xlabel="PPA", ylabel="SLG"
    )

    ax.set_xlim(3,5)
    ax.set_ylim(0.0,0.8)
    ax.scatter(t_ppa, t_slg, s=40)

    for i, label in enumerate(t_player_name):
        plt.text(t_ppa[i], t_slg[i], label)  # type: ignore

    plt.savefig(os.path.join(t_result_path, t_team + "_ppa_vs_slg.png"), format="png", dpi=300)
    plt.close()

# %%