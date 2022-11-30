# %%
import numpy as np
import matplotlib.pyplot as plt
import os
from globaldef_pack import globalvalue_mod as g
import calc_pack

# 解析対象外を除外する
def exclude_inappropriate_local_fnc(a_np_array_del):
    # 初期化
    t_np_array_del = a_np_array_del
    t_del_idx_list = []

    # t_atbat_define打席未満の選手は解析対象外とする。
    t_atbat_define = 100 # この行を変更して解析対象を変更できる。
    for t_idx in range(t_np_array_del.shape[0]):
        if int(t_np_array_del[:,36][t_idx]) < t_atbat_define:
            t_del_idx_list = t_del_idx_list + [t_idx]
    # 削除
    t_np_array = np.delete(t_np_array_del, t_del_idx_list, 0)
    return t_np_array

# PPAを計算
def ppa_cals_local_func(a_np_array):
    # 初期化
    t_np_array = a_np_array

    # 打者名
    t_batter_name = t_np_array[:,3]

    # 被投球数
    t_pitch_sum = t_np_array[:,31].astype(int) + t_np_array[:,33].astype(int)
    # 打席数
    t_atbat_sum = t_np_array[:,36].astype(int)

    t_ppa_result = np.round(t_pitch_sum/t_atbat_sum , 3)   # 小数点4で四捨五入し小数点3へ表示

    return t_ppa_result

def ppa_vs_strikeoutrate_fnc(a_team, a_year_idx, a_np_array):
    # チーム
    t_team = a_team
    t_year_idx = a_year_idx
    t_result_base_path = g.g_ppa_vs_strikeoutrate_result_base_path

    # 年度別の結果格納フォルダを作成
    t_result_path = os.path.join(t_result_base_path, str(t_year_idx))
    os.makedirs(t_result_path, exist_ok=True)

    # mysqlからデータ取得
    t_np_array_del = a_np_array.copy()

    # t_atbat_define打席未満の選手は解析対象外とする。
    t_np_array = exclude_inappropriate_local_fnc(t_np_array_del)

    # 選手名
    t_player_name = t_np_array[:,3]

    # PPA計算
    t_ppa = ppa_cals_local_func(t_np_array)

    # 三振率計算
    t_strikeoutrate = np.round(t_np_array[:,44].astype(int)/t_np_array[:,36].astype(int),3)
    # t_np_array[:,36]    # 打席数
    # t_np_array[:,44]    # 三振数

    # 散布図を描画
    plt.rcParams["font.size"] = 8

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(
        111, xlabel="PPA", ylabel="StrikeOutRate"
    )

    ax.set_xlim(3,5)
    ax.set_ylim(0.0,0.5)
    ax.scatter(t_ppa, t_strikeoutrate, s=40)

    for i, label in enumerate(t_player_name):
        plt.text(t_ppa[i], t_strikeoutrate[i], label)  # type: ignore

    plt.savefig(os.path.join(t_result_path, t_team + "_ppa_vs_strikeoutrate.png"), format="png", dpi=300)
    plt.close()

if __name__ == "__main__":
    import sys
    import os
    ppa_vs_strikeoutrate_fnc(sys.argv[1],sys.argv[2],sys.argv[3])

# %%
