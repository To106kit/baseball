import numpy as np

# PPAを計算
def ppa_cals_fnc(a_np_array):
    # 被投球数
    t_pitch_sum = a_np_array[:,31].astype(int) + a_np_array[:,33].astype(int)
    # 打席数
    t_atbat_sum = a_np_array[:,36].astype(int)
    # PPAを計算
    t_ppa_result = np.round(t_pitch_sum/t_atbat_sum , 3)   # 小数点4で四捨五入し小数点3へ表示

    return t_ppa_result