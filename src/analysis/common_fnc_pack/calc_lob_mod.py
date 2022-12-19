import numpy as np
import common_fnc_pack

def calc_lob_fnc(a_np_array):
    # 安打数を取得
    t_hitallowed = common_fnc_pack.get_pitcher_data_mod.get_hitsallowed_fnc(a_np_array)
    # 与死球を取得
    t_hitbypitch = common_fnc_pack.get_pitcher_data_mod.get_hitbypitch_fnc(a_np_array)

    # 与四球を取得
    t_basesonballs = common_fnc_pack.get_pitcher_data_mod.get_basesonballs_fnc(a_np_array)

    # 失点を取得
    t_runsallowed = common_fnc_pack.get_pitcher_data_mod.get_runsallowed_fnc(a_np_array)

    # 本塁打を取得
    t_homerunallowed = common_fnc_pack.get_pitcher_data_mod.get_homerunallowed_fnc(a_np_array)

    # LOB%を計算
    ## LOB[%] ＝ (安打 + 与四死球 － 失点) ÷ {安打 + 与四死球 － (本塁打 × 1.4)} * 100
    t_np_lob_list = np.round((t_hitallowed + t_hitbypitch + t_basesonballs - t_runsallowed)\
                    / (t_hitallowed + t_hitbypitch + t_basesonballs - (t_homerunallowed * 1.4)) * 100, 1)

    return t_np_lob_list
