import numpy as np

# 塁打数を計算
def calc_totalbases_fnc(a_np_array):
    t_single = a_np_array[:,38].astype(int)     # 単打(38)
    t_twobase = a_np_array[:,39].astype(int)    # 二塁打(39)
    t_threebase = a_np_array[:,40].astype(int)  # 三塁打(40)
    t_homerun = a_np_array[:,41].astype(int)    # 本塁打(41)

    t_totalbases = t_single + t_twobase*2 + t_threebase*3 + t_homerun*4

    return t_totalbases