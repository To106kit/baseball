import matplotlib.pyplot as plt
import numbers as np
import os

# 塁打とは、「単打＝1、二塁打＝2、三塁打＝3、本塁打＝4」として計算します。
def totalbases_cals_func(a_single, a_twobase, a_threebase, a_homerun):
    # 初期化
    t_single = int(a_single)            # 単打
    t_twobase = int(a_twobase)          # 二塁打
    t_threebase = int(a_threebase)      # 三塁打
    t_homerun = int(a_homerun)          # 本塁打

    # ops計算実行
    t_totalbases = t_single + t_twobase*2 + t_threebase*3 + t_homerun*4
    print(round(t_totalbases, 3))

    return t_totalbases

if __name__ == "__main__":
    import os
    import sys
    # ops_cals_func(sys.argv[1], sys.argv[2])
    totalbases_cals_func('1', '1', '1', '1')

