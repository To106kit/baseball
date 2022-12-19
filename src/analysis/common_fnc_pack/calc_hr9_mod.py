import numpy as np
import common_fnc_pack

def calc_hr9_fnc(a_np_array):
    # 被本塁打を取得
    t_np_homerunallowed_list = common_fnc_pack.get_pitcher_data_mod.get_homerunallowed_fnc(a_np_array)
    # 投球回を取得
    t_np_innings_list = common_fnc_pack.get_pitcher_data_mod.get_innings_fnc(a_np_array)

    # 投球回をアウト数に変換
    t_np_totaloutcounts_list = common_fnc_pack.convert_innings_to_outcounts_mod.convert_innings_to_outcounts_fnc(t_np_innings_list)

    # hr/9を計算
    ## 計算式：HR/9 ＝ (被本塁打 ÷ 投球回) × 9 =  被本塁打 / 全アウト数 * 3 * 9
    t_np_hr9 = np.round((t_np_homerunallowed_list / t_np_totaloutcounts_list * 3 * 9), 3)   # 小数点第4位を四捨五入

    return t_np_hr9
