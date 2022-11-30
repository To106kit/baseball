import numpy as np
import common_fnc_pack

def calc_ops_fnc(a_np_array):
    # 出塁率を取得(obp)
    t_obp = common_fnc_pack.calc_obp_mod.calc_obp_fnc(a_np_array)
    # 長打率を取得(slg)
    t_slg = common_fnc_pack.calc_slg_mod.calc_slg_fnc(a_np_array)

    # ops計算実行
    t_ops = t_obp + t_slg

    return t_ops