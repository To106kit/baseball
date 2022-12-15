import matplotlib.pyplot as plt
import numpy as np
import os
from globaldef_pack import globalvalue_mod as g
import common_fnc_pack

# 解析対象外を除外する
def exclude_validity_local_fnc(a_np_array):
    # 初期化
    t_del_idx_list = []

    # t_atbat_define打席未満の選手は解析対象外とする。
    t_invalid_str = "---" # ---(ND)の場合はその行を解析対象外とする
    for t_idx in range(a_np_array.shape[0]):
        if np.any(a_np_array[:,6:15][t_idx] == "---"):
            t_del_idx_list = t_del_idx_list + [t_idx]
    # 削除
    t_plot_list = np.delete(a_np_array, t_del_idx_list, 0)
    return t_plot_list


def plot_average_fnc(a_team, a_year_idx, a_np_array):
    # 初期化
    t_team = a_team
    t_year_idx = a_year_idx
    t_del_idx_list = []
    t_result_base_path = g.g_course_result_base_path

    # 年度別の結果格納フォルダを作成
    t_result_path = os.path.join(t_result_base_path, str(t_year_idx))
    os.makedirs(t_result_path, exist_ok=True)

    # 解析対象外を除外する
    t_np_array = common_fnc_pack.exclude_data_mod.exclude_batter_data_fnc(a_np_array)

    # プロット対象を取得
    t_plot_list = exclude_validity_local_fnc(t_np_array)

    fig = plt.figure(figsize=(10, 10))
    plt.rcParams["font.size"] = 5
    # # プロット
    for t_idx in range(g.g_strike_size):
        t_strike_int = t_idx + 1  # pythonは0始まりなので、+1している。
        t_title = "strike" + str(t_strike_int)

        ax = fig.add_subplot(3,3,t_strike_int, title=t_title)

        ax.bar(t_plot_list[:,3], t_plot_list[:,t_idx + 6].astype(np.float32)) # id,playerid,role,name,team,year(6要素分を足したあとの要素からスタートするため6を足している。)
        ax.tick_params(axis="x", rotation=30)
        ax.tick_params(labelsize=5)
    plt.savefig(os.path.join(t_result_path, t_team + "_strike_course.png"), format="png", dpi=300)
    plt.close()

if __name__ == "__main__":
    import sys
    import os
    # plot_average_fnc(sys.argv[1])
    print('getcwd:      ', os.getcwd())
    print('__file__:    ', __file__)
    print('basename:    ', os.path.basename(__file__))
    print('dirname:     ', os.path.dirname(__file__))

