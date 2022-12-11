import numpy as np
import common_fnc_pack

# 犠打成功率を計算
def calc_successbuntrate_fnc(a_np_array):
    t_trybunt = common_fnc_pack.get_data_mod.get_trybunt_fnc(a_np_array)
    t_successbunt = common_fnc_pack.get_data_mod.get_successbunt_fnc(a_np_array)
    
    # 犠打成功率計算
    t_successbuntrate = np.round(t_successbunt/t_trybunt, 3)

    return t_successbuntrate