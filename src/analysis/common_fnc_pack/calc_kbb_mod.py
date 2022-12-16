import numpy as np
import common_fnc_pack

# PPAを計算
def calc_kbb_fnc(a_np_array):
    # 与四球取得
    t_np_basesonballs = common_fnc_pack.get_pitcher_data_mod.get_basesonballs_fnc(a_np_array)

    # 奪三振数取得
    t_np_strikeout = common_fnc_pack.get_pitcher_data_mod.get_strikeout_fnc(a_np_array)

    # 【計算方法】 奪三振数÷与四球数
    t_kbb = np.round(t_np_strikeout / t_np_basesonballs, 3)
    return t_kbb