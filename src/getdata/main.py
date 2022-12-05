# import getdata.getdata as getdata
from getdata_pack import getdata_mod
from lib_pack import makedict_mod
from mysql_pack import sql_mod
import sendgmail_pack
import time_pack
import numpy as np
import re
import os
import urllib
import time
from globaldef_pack import globalvalue_mod as g


############################## 関数定義 ####################################
def get_course_data(t_course_url, t_ele, t_year_idx):
    t_getdatalist = []
    t_player_id = t_ele[0]
    t_player_name = t_ele[1]
    t_player_role = t_ele[2]

    # コース別打率を取得
    t_getdatalist, t_teamName, t_invalid_flag  = getdata_mod.getaverage(t_course_url, t_year_idx)
    t_getdatalist = np.append(t_getdatalist, t_player_name)
    t_getdatalist = np.append(t_getdatalist, t_year_idx)
    t_getdatalist = np.append(t_getdatalist, t_teamName)
    t_getdatalist = np.append(t_getdatalist, t_player_id)
    # URLがバッターデータの場合
    if g.t_batter_key_str in t_course_url:
        t_getdatalist = np.append(t_getdatalist, g.t_batter_key_str)
    # URLがピッチャーデータの場合
    elif g.t_picher_key_str in t_course_url:
        t_getdatalist = np.append(t_getdatalist, g.t_picher_key_str)
    return t_getdatalist, t_invalid_flag
############################## 関数定義 ####################################

############################## クラス定義 ##################################
############################## クラス定義 ##################################



# 時間計測開始
t_time_sta = time.time()

# 初期化
t_getdatalist = []
t_batterDataList = np.empty((0,51), str)
t_picherDataList = np.empty((0,30), str)
t_playerName = ""
t_teamName = ""
t_course_split = []
t_course_url = ""
t_selectionEye_url = ""
t_selectionEye_split = []
t_base_url = ""
t_base_split = []
t_basedata_list = []
t_exception_flag = False
t_invalid_flag = False
t_unit_flag = "sec"

# データ取得対象球団のベースとなるページurlリスト
## 打者url
t_url_batter_list = [
        "https://baseballdata.jp/1/ctop.html",
        # "https://baseballdata.jp/2/ctop.html",
        # "https://baseballdata.jp/3/ctop.html",
        # "https://baseballdata.jp/4/ctop.html",
        # "https://baseballdata.jp/5/ctop.html",
        # "https://baseballdata.jp/6/ctop.html",
        # "https://baseballdata.jp/7/ctop.html",
        # "https://baseballdata.jp/8/ctop.html",
        # "https://baseballdata.jp/9/ctop.html",
        # "https://baseballdata.jp/11/ctop.html",
        # "https://baseballdata.jp/12/ctop.html",
        # "https://baseballdata.jp/376/ctop.html",
    ]

## 投手url
t_url_pitcher_list = [
        "https://baseballdata.jp/1/cptop.html",
        "https://baseballdata.jp/2/cptop.html",
        "https://baseballdata.jp/3/cptop.html",
        "https://baseballdata.jp/4/cptop.html",
        "https://baseballdata.jp/5/cptop.html",
        "https://baseballdata.jp/6/cptop.html",
        "https://baseballdata.jp/7/cptop.html",
        "https://baseballdata.jp/8/cptop.html",
        "https://baseballdata.jp/9/cptop.html",
        "https://baseballdata.jp/11/cptop.html",
        "https://baseballdata.jp/12/cptop.html",
        "https://baseballdata.jp/376/cptop.html",
    ]

# 辞書を取得
t_np_batter_list = makedict_mod.makedict(t_url_batter_list)
t_np_pitcher_list = makedict_mod.makedict(t_url_pitcher_list)

t_np_list = np.concatenate([t_np_batter_list, t_np_pitcher_list])

for t_ele in t_np_list:
    t_player_id = t_ele[0]
    t_player_name = t_ele[1]
    t_player_role = t_ele[2]
    print(t_player_id, t_player_name, t_player_role)

    # player roleがバッターの場合
    if t_player_role == g.t_batter_key_str:
        # ベースurl(現状は打席数のみ取得するために使用している。)
        t_base_url =  [g.t_prefix_url + g.t_batter_key_str + '/'+ t_player_id + g.t_sufix_base]
        t_base_split = t_base_url[0].split('/')

        # コース別打率url
        t_course_url = [g.t_prefix_url + g.t_batter_key_str + '/'+ t_player_id + g.t_sufix_course]
        t_course_split = t_course_url[0].split('/')

        # 選球眼url
        t_selectionEye_url = [g.t_prefix_url + g.t_batter_key_str + '/'+ t_player_id + g.t_sufix_selectionEye]
        t_selectionEye_split = t_selectionEye_url[0].split('/')

    # player roleがピッチャーの場合
    elif t_player_role == g.t_picher_key_str:
        # コース別打率url
        t_course_url = [g.t_prefix_url + g.t_picher_key_str + '/'+ t_player_id + g.t_sufix_course]
        t_course_split = t_course_url[0].split('/')

    # 年度別url作成
    for t_year_idx in range(2012, 2023, 1):
        # 前年度までのシーズンのデータを取得
        if t_year_idx != 2022:
            # 打席数打取得用url(年度別)を作成
            t_base_replace = t_base_split.copy()
            t_base_replace.insert(3, str(t_year_idx))
            t_base_archive_url = '/'.join(t_base_replace)

            # コース別打率取得用url(年度別)を作成
            t_course_replace = t_course_split.copy()
            t_course_replace.insert(3, str(t_year_idx))
            t_course_archive_url = '/'.join(t_course_replace)

            # 選球眼データ取得用url(年度別)を作成
            t_selectionEye_replace = t_selectionEye_split.copy()
            t_selectionEye_replace.insert(3, str(t_year_idx))
            t_selectionEye_archive_url = '/'.join(t_selectionEye_replace)

            # コース別打率を取得
            try:
                t_getdatalist, t_invalid_flag = get_course_data(t_course_archive_url, t_ele, t_year_idx)
                # 引退した選手のデータが残っている場合の処理(mysqlへ追加しない様にするために、次のインデックスへ移る。)
                if t_invalid_flag == True:
                    #次のurlへ移る
                    continue
                elif t_invalid_flag == False:
                    #何もしない
                    pass
            except (urllib.request.HTTPError, ValueError, IndexError):  # type: ignore
                print('Not found:', t_course_archive_url)
                continue

            # player roleがバッターの場合のデータ取得
            if t_player_role == g.t_batter_key_str:
                # 選球眼データ取得
                try:
                    t_selectionEye_list  = getdata_mod.getpitchedpiches(t_selectionEye_archive_url)
                    t_getdatalist  = np.append(t_getdatalist, t_selectionEye_list)
                except (urllib.request.HTTPError, ValueError, IndexError):  # type: ignore
                    print('Not found:', t_selectionEye_archive_url)
                    continue

                # 打席数・安打数・単打数・二塁打数・三塁打数・本塁打数・四球数・死球数・三振数・併殺数(計10要素)を取得
                try:
                    # t_basedata_list, t_exception_flag = getdata_mod.getbasebatterdata(t_base_archive_url)
                    t_basedata_result_list = getdata_mod.getbasebatterdata(t_base_archive_url)
                    t_basedata_list = t_basedata_result_list[0]
                    t_exception_flag = t_basedata_result_list[1]
                    t_getdatalist  = np.append(t_getdatalist, t_basedata_list)
                except Exception as e:
                    print("例外args:", e.args)


        # 今シーズンのデータを取得
        elif t_year_idx == 2022:
            # コース別打率を取得
            try:
                t_getdatalist, t_invalid_flag = get_course_data(t_course_url[0], t_ele, t_year_idx)
                # 引退した選手のデータが残っている場合の処理(mysqlへ追加しない様にするために、次のインデックスへ移る。)
                if t_invalid_flag == True:
                    #次のurlへ移る
                    continue
                elif t_invalid_flag == False:
                    #何もしない
                    pass
            except (urllib.request.HTTPError, ValueError, IndexError):  # type: ignore
                print('Not found:', t_course_url[0])
                continue

            # player roleがバッターの場合
            # 選球眼データ取得
            if t_player_role == g.t_batter_key_str:
                try:
                    # 選球眼データ取得
                    t_selectionEye_list  = getdata_mod.getpitchedpiches(t_selectionEye_url[0])
                    t_getdatalist  = np.append(t_getdatalist, t_selectionEye_list)
                except (urllib.request.HTTPError, ValueError, IndexError):  # type: ignore
                    print('Not found:', t_selectionEye_url[0])
                    continue

                # 打席数・安打数・単打数・二塁打数・三塁打数・本塁打数・四球数・死球数・三振数・併殺数(計10要素)を取得
                try:
                    t_basedata_result_list = getdata_mod.getbasebatterdata(t_base_url[0])
                    t_basedata_list = t_basedata_result_list[0]
                    t_exception_flag = t_basedata_result_list[1]
                    t_getdatalist  = np.append(t_getdatalist, t_basedata_list)

                except Exception as e:
                    print("例外args:", e.args)
                    t_getdatalist  = np.append(t_getdatalist, t_basedata_list)

        if t_exception_flag == False:
            # 縦結合(年度毎の打率※投手の場合は被打率)
            # player roleがバッターの場合
            if t_player_role == g.t_batter_key_str:
                try:
                    t_batterDataList = np.row_stack((t_batterDataList, t_getdatalist))
                except Exception as e:
                    print("例外args:", e.args)

            elif t_player_role == g.t_picher_key_str:
                t_picherDataList = np.row_stack((t_picherDataList, t_getdatalist))
        elif t_exception_flag == True:
            # 例外の場合、引退or出場していない年のデータのため追加しない。
            pass

# mysqlへ登録
sql_mod.addsql_batter(t_batterDataList)
sql_mod.addsql_picher(t_picherDataList)

# 時間計測終了
t_time_end = time.time()
# 経過時間（min）
t_time, t_unit_flag = time_pack.calc_exec_time_mod.calc_exec_time_fnc(t_time_sta, t_time_end)

# gmailへ実行完了メールを送信
sendgmail_pack.sendgmail_mod.sendgmail(t_time, t_unit_flag)

print("########## all end ################")


