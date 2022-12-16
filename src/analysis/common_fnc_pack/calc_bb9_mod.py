import numpy as np
import common_fnc_pack

# 解析対象外を除外する
def convert_innings_local_fnc(a_innings):
    # 初期化
    t_totalInnings = []
    t_innings = a_innings.copy()

    t_invalid_str = "/" # イニングが端数の場合はその行を計算する。
    for t_idx in range(a_innings.shape[0]):
        if np.any(t_invalid_str in a_innings[t_idx]):
            # イニングの端数を分数に表現
            t_split_list = t_innings[t_idx].split('+')
            # 端数
            t_fraction_list = t_split_list[1].split('/')

            # イニング→打者数に変換(*3)
            t_main = int(t_split_list[0]) * 3
            t_fraction = int(t_fraction_list[0]) / int(t_fraction_list[1]) * 3
            t_allout = t_main + t_fraction

            # Fractionモジュール使用して端数分数化
            t_totalInnings = t_totalInnings + [int(t_allout)]
        else:
            t_totalInnings = t_totalInnings + [a_innings[t_idx].astype(int).tolist() * 3]

    return t_totalInnings

# PPAを計算
def calc_bb9_fnc(a_np_array):
    # 与四球取得
    t_np_basesonballs = common_fnc_pack.get_pitcher_data_mod.get_basesonballs_fnc(a_np_array)

    # 投球回取得
    t_innings = common_fnc_pack.get_pitcher_data_mod.get_innings_fnc(a_np_array)

    # イニングの端数を計算する
    t_totalOut = convert_innings_local_fnc(t_innings)
    t_np_totalOut = np.array(t_totalOut)

    # 【計算方法】 BB/9=（与四球 / 投球回数）× 9 → BB/9=（与四球 / 総アウト数 * 3）× 9
    # ※投球回=総アウト数/3と計算する
    t_bb9 = np.round((t_np_basesonballs / t_np_totalOut * 3) * 9, 3)
    return t_bb9