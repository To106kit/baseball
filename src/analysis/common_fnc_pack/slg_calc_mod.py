import matplotlib.pyplot as plt
import numbers as np
import os

def slg_cals_func(a_totalbases, a_atbats):
    # 初期化
    t_totalbases = int(a_totalbases)    # 塁打数
    t_atbats = int(a_atbats)    # 打数

    # ops計算実行
    t_slg = t_totalbases / t_atbats
    print(round(t_slg, 3))

    return t_slg

if __name__ == "__main__":
    import os
    import sys
    # ops_cals_func(sys.argv[1], sys.argv[2])
    slg_cals_func('100', '220')

