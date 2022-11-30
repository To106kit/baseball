import matplotlib.pyplot as plt
import numpy as np
import os
from globaldef_pack import globalvalue_mod as g
import common_fnc_pack

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
    t_np_array = common_fnc_pack.exclude_data_mod.exclude_data_fnc(a_np_array)
#TODO feat : average_mod.pyのリファクタリング #11
    t_np_strike_array = t_np_array[:,0:15]
    t_validity_list = t_np_strike_array[np.all(t_np_strike_array != "---", axis=1)]
    t_course_list = t_validity_list[:,6:15].astype(np.float32)
    t_course_average_for_plt_nplist = np.column_stack([t_validity_list[:,3:5],t_course_list])
    t_plot_list = t_course_average_for_plt_nplist.copy()
#TODO feat : average_mod.pyのリファクタリング #11

    fig = plt.figure(figsize=(10, 10))
    plt.rcParams["font.size"] = 5
    # # プロット
    for t_idx in range(t_plot_list.shape[1] - 2): # チーム名、選手名の2列分の要素数を引く
        t_strike_int = t_idx + 1  # pythonは0始まりなので、+1している。
        t_title = "strike" + str(t_strike_int)

        ax = fig.add_subplot(3,3,t_strike_int, title=t_title)

        ax.bar(t_plot_list[:,0], t_plot_list[:,t_idx + 2].astype(np.float32)) # チーム名、選手名の2列分の要素数をタス
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

