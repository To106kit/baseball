# %%
import numpy as np
import matplotlib.pyplot as plt
import os
from globaldef_pack import globalvalue_mod as g
import common_fnc_pack

def buntsuccessrate_vs_battingeye_fnc(a_team, a_year_idx, a_np_array):
    # チーム
    t_team = a_team
    t_year_idx = a_year_idx
    t_result_base_path = g.g_successbuntrate_vs_battingeye_result_base_path

    # 年度別の結果格納フォルダを作成
    t_result_path = os.path.join(t_result_base_path, str(t_year_idx))
    os.makedirs(t_result_path, exist_ok=True)

    # 解析対象外を除外する
    t_np_array = common_fnc_pack.exclude_data_mod.exclude_data_fnc(a_np_array)

    # 選手名
    t_player_name = common_fnc_pack.get_data_mod.get_playername_fnc(t_np_array)

    # ボール球見極め率
    t_ballnoswingrate = common_fnc_pack.calc_ballnoswingrate_mod.ballnoswingrate_fnc(t_np_array)

    # ストライクスイング率
    t_strikeswingrate = common_fnc_pack.calc_strikeswingrate_mod.strikeswingrate_fnc(t_np_array)

    # 選球眼(batting eye):ボール球見極め率 + ストライクスイング率
    t_battingeye = t_ballnoswingrate + t_strikeswingrate

    # バント成功率
    t_successbuntrate = common_fnc_pack.calc_successbuntrate_mod.calc_successbuntrate_fnc(t_np_array)

    # 散布図を描画
    plt.rcParams["font.size"] = 8

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(
        111, xlabel="バント成功率", ylabel="battingeye(ボール球見極め率 + ストライクスイング率)"
    )

    ax.set_xlim(0.0,1.0)
    ax.set_ylim(1.0,1.5)
    ax.scatter(t_successbuntrate, t_battingeye, s=40)

    for i, label in enumerate(t_player_name):
        # バント成功率nanの場合は飛ばす。
        if np.isnan(t_successbuntrate[i]):
            continue
        plt.text(t_successbuntrate[i], t_battingeye[i], label)  # type: ignore

    plt.savefig(os.path.join(t_result_path, t_team + "_successbuntrate_battingeye.png"), format="png", dpi=300)
    plt.close()

if __name__ == "__main__":
    import sys
    import os
    buntsuccessrate_vs_battingeye_fnc(sys.argv[1],sys.argv[2],sys.argv[3])

# %%
