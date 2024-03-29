import matplotlib.pyplot as plt
import numpy as np
import os
from globaldef_pack import globalvalue_mod as g
import common_fnc_pack

def cor_lob_vs_k9_fnc(a_team, a_year_idx, a_np_array):
    # チーム
    t_team = a_team
    t_year_idx = a_year_idx
    t_result_base_path = g.g_lob_vs_k9_result_base_path

    # 年度別の結果格納フォルダを作成
    t_result_path = os.path.join(t_result_base_path, str(t_year_idx))
    os.makedirs(t_result_path, exist_ok=True)

    # 解析対象外を除外する
    t_np_array = common_fnc_pack.exclude_data_mod.exclude_pitcher_data_fnc(a_np_array)

    # 選手名
    t_player_name = common_fnc_pack.get_batter_data_mod.get_playername_fnc(t_np_array)

    # LOB%取得
    t_np_lob_list = common_fnc_pack.calc_lob_mod.calc_lob_fnc(t_np_array)

    # K/9取得
    t_np_k9_list = common_fnc_pack.calc_k9_mod.calc_k9_fnc(t_np_array)

    # 散布図を描画
    plt.rcParams["font.size"] = 8

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(
        111, xlabel="LOB%", ylabel="K9"
    )

    ax.set_xlim(30,100)
    ax.set_ylim(0.0,12)
    ax.scatter(t_np_lob_list, t_np_k9_list, s=40)

    #相関係数の算出
    correlation = np.corrcoef(t_np_lob_list,t_np_k9_list)
    print(correlation[0,1])

    for i, label in enumerate(t_player_name):
        plt.text(t_np_lob_list[i], t_np_k9_list[i], label)  # type: ignore

    plt.savefig(os.path.join(t_result_path, t_team + "_lob_vs_k9.png"), format="png", dpi=300)
    plt.close()

if __name__ == "__main__":
    import sys
    import os
    cor_lob_vs_k9_fnc(sys.argv[1],sys.argv[2],sys.argv[3])