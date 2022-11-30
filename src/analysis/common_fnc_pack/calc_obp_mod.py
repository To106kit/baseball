import numpy as np

# PPAを計算
def calc_obp_fnc(a_np_array):
    ## 打数
    t_atbats = a_np_array[:,46].astype(int)
    ## 安打数
    t_hit = a_np_array[:,37].astype(int)
    ## 死球数
    t_hitbypitch = a_np_array[:,43].astype(int)
    ## 四球数
    t_walk = a_np_array[:,42].astype(int)
    ## 犠飛
    t_sacrificeflight = a_np_array[:,47].astype(int)
    # 計算（出塁率 ＝ （安打数＋死球+四球）÷（打数＋死球＋四球＋犠飛））
    t_obp = np.round((t_hit + t_hitbypitch + t_walk) / (t_atbats + t_hitbypitch + t_walk + t_sacrificeflight) , 3)

    return t_obp