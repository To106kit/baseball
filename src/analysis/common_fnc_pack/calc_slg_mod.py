import numpy as np
import common_fnc_pack

def calc_slg_fnc(a_np_list):
    # 打数
    t_atbats = a_np_list[:,46].astype(int)

    # 塁打数計算
    t_totalbases = common_fnc_pack.calc_totalbases_mod.calc_totalbases_fnc(a_np_list)

    # ops計算実行
    t_slg = np.round(t_totalbases / t_atbats , decimals= 3)
    return t_slg