import matplotlib.pyplot as plt
import numpy as np
import os

def calc_fnc(a_team, a_year_idx, a_np_array):
    # 初期化
    t_ppa_element = []
    t_del_idx_list = []
    t_ppa_list = np.empty((0,2), str)
    t_team = a_team
    t_year_idx = a_year_idx
    t_result_base_path = "D:\\11_github\\python\\baseball\\result\\ppa"

    # 年度別の結果格納フォルダを作成
    t_result_path = os.path.join(t_result_base_path, str(t_year_idx))
    os.makedirs(t_result_path, exist_ok=True)

    # mysqlからデータ取得
    t_np_array_del = a_np_array.copy()

    # t_atbat_define打席未満の選手は解析対象外とする。
    t_atbat_define = 100 # この行を変更して解析対象を変更できる。
    for t_idx in range(t_np_array_del.shape[0]):
        if int(t_np_array_del[:,36][t_idx]) < t_atbat_define:
            t_del_idx_list = t_del_idx_list + [t_idx]
    # 削除
    t_np_array = np.delete(t_np_array_del, t_del_idx_list, 0)


    # 計算
    for t_idx in range(t_np_array.shape[0]):
        # 打者名
        t_batter_name = t_np_array[t_idx][3]
        # 被投球数
        t_pitch_sum = int(t_np_array[t_idx][31]) + int(t_np_array[t_idx][33])
        # 打席数
        t_atbat_sum = int(t_np_array[t_idx][36])
        # p/pa(1打席あたりにピッチャーにどれだけ球数を投げさせたか)計算
        try:
            t_ppa_result = round(t_pitch_sum/t_atbat_sum , 2)   # 小数点4で四捨五入し小数点3へ表示
        except ZeroDivisionError:
            continue

        t_ppa_element = [str(t_batter_name), str(t_ppa_result)]
        # 縦結合
        t_ppa_list = np.row_stack((t_ppa_list, t_ppa_element))

    # プロット
    fig, ax = plt.subplots(figsize=(6, 2.5))
    ax.set_ylim(0.0,5.0)
    ax.bar(t_ppa_list[:,0], t_ppa_list[:,1].astype(np.float64))

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