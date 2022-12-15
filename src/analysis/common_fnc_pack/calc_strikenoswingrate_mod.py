import numpy as np
import common_fnc_pack

# ストライク見逃し率を計算
def strikenoswingrate_fnc(a_np_array):
    # ストライク被投球数
    t_pitchedstrikesum = common_fnc_pack.get_batter_data_mod.get_pitchedstrikesum_fnc(a_np_array)
    # ストライク見逃し数
    t_strikenoswing = common_fnc_pack.get_batter_data_mod.get_strikenoswing_fnc(a_np_array)
    # ストライク見逃し率
    t_strikenoswingrate = np.round(t_strikenoswing/t_pitchedstrikesum,2)

    return t_strikenoswingrate