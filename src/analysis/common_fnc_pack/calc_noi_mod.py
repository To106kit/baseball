import numpy as np
import common_fnc_pack

# PPAを計算
def calc_noi_fnc(a_np_array):
    # 出塁率取得
    t_obp = common_fnc_pack.calc_obp_mod.calc_obp_fnc(a_np_array)
    
    # 長打率取得
    t_slg = common_fnc_pack.calc_slg_mod.calc_slg_fnc(a_np_array)

    # noi計算[(出塁率 + 長打率/3)*1000]
    t_noi = np.round((t_obp + t_slg/3) *1000)
    return t_noi