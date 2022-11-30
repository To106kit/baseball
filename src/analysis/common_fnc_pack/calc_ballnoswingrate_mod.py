import numpy as np

# PPAを計算
def ballnoswingrate_fnc(a_np_array):
    t_ballnoswingrate = np.round(a_np_array[:,32].astype(int)/a_np_array[:,31].astype(int),2)

    return t_ballnoswingrate