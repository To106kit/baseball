import numpy as np
import common_fnc_pack

def calc_isop_fnc(a_np_array):
    # 長打率を取得
    t_slg = common_fnc_pack.calc_slg_mod.calc_slg_fnc(a_np_array)
    # 打率を取得
    t_average = common_fnc_pack.calc_average_mod.calc_average_fnc(a_np_array)
    # IsoPを計算
    t_isop = np.round((t_slg - t_average), 3)

    return t_isop