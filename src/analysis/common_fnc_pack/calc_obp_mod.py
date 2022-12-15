import numpy as np
import common_fnc_pack

# PPAを計算
def calc_obp_fnc(a_np_array):
    ## 打数
    t_atbats = common_fnc_pack.get_batter_data_mod.get_atbat_fnc(a_np_array)
    ## 安打数
    t_allhit = common_fnc_pack.get_batter_data_mod.get_allhit_fnc(a_np_array)
    ## 死球数
    t_hitbypitch = common_fnc_pack.get_batter_data_mod.get_hitbypitch_fnc(a_np_array)
    ## 四球数
    t_walk = common_fnc_pack.get_batter_data_mod.get_walk_fnc(a_np_array)
    ## 犠飛
    t_sacrificeflight = common_fnc_pack.get_batter_data_mod.get_sacrificeflight_fnc(a_np_array)

    # 計算（出塁率 ＝ （安打数＋死球+四球）÷（打数＋死球＋四球＋犠飛））
    t_obp = np.round((t_allhit + t_hitbypitch + t_walk) / (t_atbats + t_hitbypitch + t_walk + t_sacrificeflight) , 3)

    return t_obp