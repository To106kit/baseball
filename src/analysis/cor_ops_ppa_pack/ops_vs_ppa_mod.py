# %%
import numpy as np
import matplotlib.pyplot as plt
import os
from globaldef_pack import globalvalue_mod as g
import calc_pack


# 出塁率計算
def calc_obp_local_fnc(a_np_array):
    # 初期化
    t_np_array = a_np_array

    ## 打数
    t_atbats = t_np_array[:,46].astype(int)
    ## 安打数
    t_hit = t_np_array[:,37].astype(int)
    ## 死球数
    t_hitbypitch = t_np_array[:,43].astype(int)
    ## 四球数
    t_walk = t_np_array[:,42].astype(int)
    ## 犠飛
    t_sacrificeflight = t_np_array[:,47].astype(int)
    # 計算（出塁率 ＝ （安打数＋死球+四球）÷（打数＋死球＋四球＋犠飛））
    t_obp = np.round((t_hit + t_hitbypitch + t_walk) / (t_atbats + t_hitbypitch + t_walk + t_sacrificeflight) , 3)

    return t_obp, t_atbats

# 解析対象外を除外する
def exclude_inappropriate_local_fnc(a_np_array_del):
    # 初期化
    t_np_array_del = a_np_array_del
    t_del_idx_list = []

    # t_atbat_define打席未満の選手は解析対象外とする。
    t_atbat_define = 100 # この行を変更して解析対象を変更できる。
    for t_idx in range(t_np_array_del.shape[0]):
        if int(t_np_array_del[:,36][t_idx]) < t_atbat_define:
            t_del_idx_list = t_del_idx_list + [t_idx]
    # 削除
    t_np_array = np.delete(t_np_array_del, t_del_idx_list, 0)
    return t_np_array

# 塁打数を計算
def totalbases_cals_func(a_np_array):
    # 初期化
    t_np_array = a_np_array
    t_single = t_np_array[:,38].astype(int)     # 単打(38)
    t_twobase = t_np_array[:,39].astype(int)    # 二塁打(39)
    t_threebase = t_np_array[:,40].astype(int)  # 三塁打(40)
    t_homerun = t_np_array[:,41].astype(int)    # 本塁打(41)

    t_totalbases = t_single + t_twobase*2 + t_threebase*3 + t_homerun*4

    return t_totalbases

# 長打率を計算
def slg_cals_func(a_totalbases, a_atbats):
    # 初期化
    t_totalbases = a_totalbases    # 塁打数
    t_atbats = a_atbats    # 打数

    # ops計算実行
    t_slg = np.round(t_totalbases / t_atbats , decimals= 3)
    return t_slg

# PPAを計算
def ppa_cals_local_func(a_np_array):
    # 初期化
    t_np_array = a_np_array

    # 打者名
    t_batter_name = t_np_array[:,3]

    # 被投球数
    t_pitch_sum = t_np_array[:,31].astype(int) + t_np_array[:,33].astype(int)
    # 打席数
    t_atbat_sum = t_np_array[:,36].astype(int)

    t_ppa_result = np.round(t_pitch_sum/t_atbat_sum , 3)   # 小数点4で四捨五入し小数点3へ表示

    return t_ppa_result

def ops_vs_ppa_fnc(a_team, a_year_idx, a_np_array):
    # チーム
    t_team = a_team
    t_year_idx = a_year_idx
    t_result_base_path = g.g_ops_vs_ppa_result_base_path

    # 年度別の結果格納フォルダを作成
    t_result_path = os.path.join(t_result_base_path, str(t_year_idx))
    os.makedirs(t_result_path, exist_ok=True)

    # mysqlからデータ取得
    t_np_array_del = a_np_array.copy()

    # t_atbat_define打席未満の選手は解析対象外とする。
    t_np_array = exclude_inappropriate_local_fnc(t_np_array_del)

    # 選手名
    t_player_name = t_np_array[:,3]

    # 出塁率計算
    t_obp, t_atbats = calc_obp_local_fnc(t_np_array)

    # 塁打数計算
    t_totalbases = totalbases_cals_func(t_np_array)

    # 長打率計算
    t_slg = slg_cals_func(t_totalbases, t_atbats)

    # OPS計算
    t_ops = t_obp + t_slg

    # PPA計算
    t_ppa = ppa_cals_local_func(t_np_array)

    ##############TODO################
    # PPAの計算を関数化リファクタリングすること#
    ##############TODO################

    # 散布図を描画
    plt.rcParams["font.size"] = 8

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(
        111, xlabel="OPS", ylabel="PPA"
    )

    ax.set_xlim(0.3,1.0)
    ax.set_ylim(3,5)
    ax.scatter(t_ops, t_ppa, s=40)

    for i, label in enumerate(t_player_name):
        plt.text(t_ops[i], t_ppa[i], label)  # type: ignore

    plt.savefig(os.path.join(t_result_path, t_team + "_ops_vs_ppa.png"), format="png", dpi=300)
    plt.close()

if __name__ == "__main__":
    import sys
    import os
    ops_vs_ppa_fnc(sys.argv[1],sys.argv[2],sys.argv[3])

# %%
