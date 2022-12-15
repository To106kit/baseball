# %%
import numpy as np
import matplotlib.pyplot as plt
import os
from globaldef_pack import globalvalue_mod as g
import common_fnc_pack

def selectioneye_fnc(a_team, a_year_idx, a_np_array):
    # チーム
    t_team = a_team
    t_year_idx = a_year_idx
    t_del_idx_list = []
    t_result_base_path = g.g_selectioneye_result_base_path

    # 年度別の結果格納フォルダを作成
    t_result_path = os.path.join(t_result_base_path, str(t_year_idx))
    os.makedirs(t_result_path, exist_ok=True)

    # 解析対象外を除外する
    t_np_array = common_fnc_pack.exclude_data_mod.exclude_batter_data_fnc(a_np_array)

    # ボール球見極め率
    t_ballnoswingrate = common_fnc_pack.calc_ballnoswingrate_mod.ballnoswingrate_fnc(t_np_array)
    # ストライク見逃し率
    t_strikenoswingrate = common_fnc_pack.calc_strikenoswingrate_mod.strikenoswingrate_fnc(t_np_array)
    # 選手名
    t_player_name = common_fnc_pack.get_batter_data_mod.get_playername_fnc(t_np_array)

    # 散布図を描画
    plt.rcParams["font.size"] = 8

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(
        111, xlabel="ボール球見極め率", ylabel="ストライク見逃し率"
    )

    ax.set_xlim(0.4,0.9)
    ax.set_ylim(0.0,0.5)
    ax.scatter(t_ballnoswingrate, t_strikenoswingrate, s=40)

    for i, label in enumerate(t_player_name):
        plt.text(t_ballnoswingrate[i], t_strikenoswingrate[i], label)  # type: ignore

    plt.savefig(os.path.join(t_result_path, t_team + "_selectioneye.png"), format="png", dpi=300)
    plt.close()

if __name__ == "__main__":
    import sys
    import os
    selectioneye_fnc(sys.argv[1],sys.argv[2],sys.argv[3])

# %%
