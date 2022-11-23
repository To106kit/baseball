import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import os
from globaldef_pack import globalvalue_mod as g


def makedict(a_url_list):

    # 初期化
    t_np_ele = []
    t_np_list = np.empty((0,3), str)
    t_role_str = ""
    t_base_replace_url = ""

    for t_url in a_url_list:
        # 対象サイトがバッターデータかピッチャーデータかを判別
        # バッター
        if "ctop" in t_url:
            t_role_str = g.t_batter_key_str
        # ピッチャー
        elif "cptop" in t_url:
            t_role_str = g.t_picher_key_str

        # # 年度別url作成
        for t_year_idx in range(2012, 2023, 1):
            if t_year_idx != 2022:
                # 打席数打取得用url(年度別)を作成
                t_base_split = t_url.split('/')
                t_base_replace = t_base_split.copy()
                t_base_replace.insert(3, str(t_year_idx))
                t_base_replace_url = '/'.join(t_base_replace)
            # 今シーズンのデータを取得
            elif t_year_idx == 2022:
                t_base_replace_url = t_url
            #対象サイトにリクエスト
            r = requests.get(t_base_replace_url)
            # html情報を取得
            soup = BeautifulSoup(r.content, 'html.parser')
            # 表データ部分を取得
            t_player_list = soup.find_all('th', class_= 'pnm')

            for t_player_info in t_player_list:
                # 選手名取得
                # contentsリストの1つめに選手情報が格納されるため
                t_contents = t_player_info.contents[1].text.split(':')
                if t_contents[0] == ' ':
                    t_player_name = t_player_info.text.strip().split(':')[1]
                else:
                    t_player_name = t_contents[1]

                # 選手ごとのリンクから、選手idを取得
                t_link = t_player_info.find('a').get('href')
                t_player_id = os.path.splitext(os.path.basename(t_link))[0]

                # 配列の場合
                t_np_ele = t_player_id
                t_np_ele = np.append(t_np_ele, t_player_name.replace("\u3000", " "))
                t_np_ele = np.append(t_np_ele, t_role_str)

                # 既に格納済みのplayeridであれば追加しない。
                if t_np_ele[0] in t_np_list[:,0]:
                    pass
                else:
                    # 縦結合
                    t_np_list = np.row_stack((t_np_list, t_np_ele))

    return t_np_list

if __name__ == "__main__":
    import sys
    makedict(sys.argv[1])