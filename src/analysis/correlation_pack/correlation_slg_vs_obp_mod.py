# %%
import numpy as np
import matplotlib.pyplot as plt
import os
from globaldef_pack import globalvalue_mod as g
import common_fnc_pack

def slg_vs_obp_fnc(a_team, a_year_idx, a_np_array):
    # チーム
    t_team = a_team
    t_year_idx = a_year_idx
    t_result_base_path = g.g_obp_vs_slg_result_base_path

    # 年度別の結果格納フォルダを作成
    t_result_path = os.path.join(t_result_base_path, str(t_year_idx))
    os.makedirs(t_result_path, exist_ok=True)

    # 解析対象外を除外する
    t_np_array = common_fnc_pack.exclude_data_mod.exclude_data_fnc(a_np_array)

    # 選手名
    t_player_name = common_fnc_pack.get_data_mod.get_playername_fnc(t_np_array)

    # 出塁率計算
    t_obp = common_fnc_pack.calc_obp_mod.calc_obp_fnc(t_np_array)

    # SLG計算
    t_slg = common_fnc_pack.calc_slg_mod.calc_slg_fnc(t_np_array)

    # 散布図を描画
    plt.rcParams["font.size"] = 8

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(
        111, xlabel="SLG", ylabel="OBP"
    )

    ax.set_xlim(0.0,0.8)
    ax.set_ylim(0.1,0.5)
    ax.scatter(t_slg, t_obp, s=40)

    for i, label in enumerate(t_player_name):
        plt.text(t_slg[i], t_obp[i], label)  # type: ignore

    plt.savefig(os.path.join(t_result_path, t_team + "_slg_vs_obp.png"), format="png", dpi=300)
    plt.close()

if __name__ == "__main__":
    import sys
    import os
    slg_vs_obp_fnc(sys.argv[1],sys.argv[2],sys.argv[3])