# %%
import numpy as np
import matplotlib.pyplot as plt
import os
from globaldef_pack import globalvalue_mod as g

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

def selectioneye_fnc(a_team, a_year_idx, a_np_array):
    # チーム
    t_team = a_team
    t_year_idx = a_year_idx
    t_del_idx_list = []
    t_result_base_path = g.g_selectioneye_result_base_path

    # 年度別の結果格納フォルダを作成
    t_result_path = os.path.join(t_result_base_path, str(t_year_idx))
    os.makedirs(t_result_path, exist_ok=True)

    # mysqlからデータ取得
    t_np_array_del = a_np_array.copy()

    # t_atbat_define打席未満の選手は解析対象外とする。
    t_np_array = exclude_inappropriate_local_fnc(t_np_array_del)

    # ボール球見極め率
    t_ball_mikiwameritu = np.round(t_np_array[:,32].astype(int)/t_np_array[:,31].astype(int),2)
    # ストライク見逃し率
    t_strike_minogashiritu = np.round(t_np_array[:,34].astype(int)/t_np_array[:,33].astype(int),2)
    # 選手名
    t_player_name = t_np_array[:,3]

    # 散布図を描画
    plt.rcParams["font.size"] = 8

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(
        111, xlabel="ボール球見極め率", ylabel="ストライク見逃し率"
    )

    ax.set_xlim(0.4,0.9)
    ax.set_ylim(0.0,0.5)
    ax.scatter(t_ball_mikiwameritu, t_strike_minogashiritu, s=40)

    for i, label in enumerate(t_player_name):
        plt.text(t_ball_mikiwameritu[i], t_strike_minogashiritu[i], label)

    plt.savefig(os.path.join(t_result_path, t_team + "_selectioneye.png"), format="png", dpi=300)
    plt.close()

if __name__ == "__main__":
    import sys
    import os
    selectioneye_fnc(sys.argv[1],sys.argv[2],sys.argv[3])

# %%
