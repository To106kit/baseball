import numpy as np
import common_fnc_pack

# ボール球見逃し率を計算
def ballnoswingrate_fnc(a_np_array):
    # ボール球被投球数
    t_pitchedballsum = common_fnc_pack.get_data_mod.get_pitchedballsum_fnc(a_np_array)
    # ボール球見逃し数
    t_ballnoswing = common_fnc_pack.get_data_mod.get_ballnoswing_fnc(a_np_array)

    # ボール球見逃し率
    t_ballnoswingrate = np.round(t_ballnoswing/t_pitchedballsum,2)
    return t_ballnoswingrate