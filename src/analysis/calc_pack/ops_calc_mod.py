import matplotlib.pyplot as plt
import numbers as np
import os

def ops_cals_func(a_obp, a_slg):
    # 初期化
    t_obp = float(a_obp)
    t_slg = float(a_slg)

    # ops計算実行
    t_ops = t_obp + t_slg
    print(round(t_ops, 3))

    return t_ops

if __name__ == "__main__":
    import os
    import sys
    # ops_cals_func(sys.argv[1], sys.argv[2])
    ops_cals_func('0.350', '0.350')

