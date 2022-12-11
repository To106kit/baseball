import numpy as np
import common_fnc_pack

# PPAを計算
def calc_isod_fnc(a_np_array):
    # 出塁率取得
    t_obp = common_fnc_pack.calc_obp_mod.calc_obp_fnc(a_np_array)

    # 打率取得
    t_ave = common_fnc_pack.calc_average_mod.calc_average_fnc(a_np_array)

    # isod計算[出塁率-打率]
    t_isod = np.round((t_obp-t_ave),4)
    return t_isod