import numpy as np
import common_fnc_pack

# ストライク見逃し率を計算
def strikeswingrate_fnc(a_np_array):
    # ストライク被投球数
    t_pitchedstrikesum = common_fnc_pack.get_data_mod.get_pitchedstrikesum_fnc(a_np_array)
    # ストライク空振り数
    t_strikeeirswing = common_fnc_pack.get_data_mod.get_strikeeirswing_fnc(a_np_array)
    # ストライク見逃し数
    t_strikenoswing = common_fnc_pack.get_data_mod.get_strikenoswing_fnc(a_np_array)
    # ストライクスイング数
    t_strikeswing = t_pitchedstrikesum - (t_strikeeirswing + t_strikenoswing)

    # ストライクスイング率
    t_strikeswingrate = np.round(t_strikeswing/t_pitchedstrikesum,2)

    return t_strikeswingrate