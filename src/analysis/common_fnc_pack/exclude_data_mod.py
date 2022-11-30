import numpy as np

# 解析対象外を除外する
def exclude_data_fnc(a_np_array):
    # 初期化
    t_del_idx_list = []

    # t_atbat_define打席未満の選手は解析対象外とする。
    t_atbat_define = 100 # この行を変更して解析対象を変更できる。
    for t_idx in range(a_np_array.shape[0]):
        if int(a_np_array[:,36][t_idx]) < t_atbat_define:
            t_del_idx_list = t_del_idx_list + [t_idx]
    # 削除
    t_np_array = np.delete(a_np_array, t_del_idx_list, 0)
    return t_np_array