import numpy as np

def calc_strikeout_fnc(a_np_array):

    t_strikeoutrate = np.round(a_np_array[:,44].astype(int)/a_np_array[:,36].astype(int),3)
    return t_strikeoutrate

if __name__ == "__main__":
    import sys
    calc_strikeout_fnc(sys.argv[1])