
def calc_exec_time_fnc(a_time_sta, a_time_end):
    # 初期化
    t_time_sta = a_time_sta
    t_time_end = a_time_end

    # 実行時間計算[sec]
    t_time = t_time_end - t_time_sta

    # 出力形式仕様
    # ・t_time が 60[sec]未満ならsec
    # ・t_time が 60[sec]以上3600[sec]以下ならmin
    # ・t_time が 3600[sec]以上ならhour
    if t_time < 60:
        t_time_for_mail = round(t_time, 2)
        t_unit_flag = "sec"

    elif t_time <= 3600:
        t_time_for_mail = round(t_time/60, 2)
        t_unit_flag = "min"

    else:
        t_time_for_mail = round(t_time/3600, 2)
        t_unit_flag = "hour"

    return t_time_for_mail, t_unit_flag

if __name__ == "__main__":
    import sys
    calc_exec_time_fnc(sys.argv[1], sys.argv[2])