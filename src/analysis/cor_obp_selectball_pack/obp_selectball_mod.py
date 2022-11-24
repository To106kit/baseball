# %%
import numpy as np
import matplotlib.pyplot as plt
import os
from globaldef_pack import globalvalue_mod as g

def obp_selectball_fnc(a_team, a_year_idx, a_np_array):
    # チーム
    t_team = a_team
    t_year_idx = a_year_idx
    t_del_idx_list = []
    t_result_base_path = g.g_obp_selectball_result_base_path

    # 年度別の結果格納フォルダを作成
    t_result_path = os.path.join(t_result_base_path, str(t_year_idx))
    os.makedirs(t_result_path, exist_ok=True)

    # mysqlからデータ取得
    t_np_array_del = a_np_array.copy()

    # t_atbat_define打席未満の選手は解析対象外とする。
    t_atbat_define = 100 # この行を変更して解析対象を変更できる。
    for t_idx in range(t_np_array_del.shape[0]):
        if int(t_np_array_del[:,36][t_idx]) < t_atbat_define:
            t_del_idx_list = t_del_idx_list + [t_idx]
    # 削除
    t_np_array = np.delete(t_np_array_del, t_del_idx_list, 0)


    # ボール球見極め率
    t_ball_mikiwameritu = np.round(t_np_array[:,32].astype(int)/t_np_array[:,31].astype(int),2)
    # ストライク見逃し率
    t_strike_minogashiritu = np.round(t_np_array[:,34].astype(int)/t_np_array[:,33].astype(int),2)
    # 選手名
    t_player_name = t_np_array[:,3]

    # 出塁率計算
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


    # 散布図を描画
    plt.rcParams["font.size"] = 8

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(
        111, xlabel="ボール球見極め率", ylabel="出塁率"
    )

    ax.set_xlim(0.4,0.9)
    ax.set_ylim(0.0,0.5)
    ax.scatter(t_ball_mikiwameritu, t_obp, s=40)

    for i, label in enumerate(t_player_name):
        plt.text(t_ball_mikiwameritu[i], t_obp[i], label)

    plt.savefig(os.path.join(t_result_path, t_team + "_obp_selectball.png"), format="png", dpi=300)
    plt.close()

if __name__ == "__main__":
    import sys
    import os
    obp_selectball_fnc(sys.argv[1],sys.argv[2],sys.argv[3])

# %%
