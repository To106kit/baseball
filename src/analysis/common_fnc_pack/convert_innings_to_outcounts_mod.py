import numpy as np

# 解析対象外を除外する
def convert_innings_to_outcounts_fnc(a_innings):
    # 初期化
    t_totaloutcounts_list = []
    t_innings = a_innings.copy()

    t_invalid_str = "/" # イニングが端数の場合はその行を計算する。
    for t_idx in range(a_innings.shape[0]):
        if np.any(t_invalid_str in a_innings[t_idx]):
            # イニングの端数を分数に表現
            t_split_list = t_innings[t_idx].split('+')
            # 端数
            t_fraction_list = t_split_list[1].split('/')

            # イニング→アウトカウントに変換(*3)
            t_main = int(t_split_list[0]) * 3
            t_fraction = int(t_fraction_list[0]) / int(t_fraction_list[1]) * 3
            t_allout_ele = t_main + t_fraction

            # Fractionモジュール使用して端数分数化
            t_totaloutcounts_list = t_totaloutcounts_list + [int(t_allout_ele)]
        else:
            t_totaloutcounts_list = t_totaloutcounts_list + [a_innings[t_idx].astype(int).tolist() * 3]

    t_np_totaloutcounts_list = np.array(t_totaloutcounts_list)


    return t_np_totaloutcounts_list