import common_fnc_pack
import numpy as np

def calc_average_fnc(a_np_array):
    # 打数を取得
    t_atbats = common_fnc_pack.get_batter_data_mod.get_atbat_fnc(a_np_array)
    # 安打数を取得
    t_allhits = common_fnc_pack.get_batter_data_mod.get_allhit_fnc(a_np_array)
    # 打率を計算
    t_average = np.round((t_allhits/t_atbats), 3)

    return t_average