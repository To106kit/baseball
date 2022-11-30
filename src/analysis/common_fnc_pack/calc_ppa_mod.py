import numpy as np
import common_fnc_pack

# PPAを計算
def ppa_cals_fnc(a_np_array):
    # 被投球数
    t_pitch_sum = common_fnc_pack.get_data_mod.get_pitchedballsum_fnc(a_np_array) + common_fnc_pack.get_data_mod.get_pitchedstrikesum_fnc(a_np_array)
    # 打席数
    t_plateappearance = common_fnc_pack.get_data_mod.get_plateappearance_fnc(a_np_array)
    # PPAを計算
    t_ppa_result = np.round(t_pitch_sum/t_plateappearance , 3)   # 小数点4で四捨五入し小数点3へ表示

    return t_ppa_result