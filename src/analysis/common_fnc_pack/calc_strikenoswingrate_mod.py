import numpy as np

# PPAを計算
def strikenoswingrate_fnc(a_np_array):
    t_strikenoswingrate = np.round(a_np_array[:,34].astype(int)/a_np_array[:,33].astype(int),2)

    return t_strikenoswingrate