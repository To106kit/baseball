from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import numpy as np

def getaverage(a_dataUrlList, a_year_idx):
    # 初期化
    t_courseList = []
    t_teamName = ""
    url = a_dataUrlList
    t_year_idx = a_year_idx
    t_invalid_flag = False

    # BeautifulSoupでデータを取得
    # requests1回につき1s待つ
    time.sleep(1)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # ガード処理(検索対象の年度のデータと不整合である場合)
    t_h2_text = soup.find_all('h2')[0].text
    # if ~t_h2_text.find(str(t_year_idx)):
    if str(t_year_idx) not in t_h2_text:
        t_invalid_flag = True

    # 選手名取得
    t_playerName = soup.find_all('h1')[0].text
    t_playerName = t_playerName.replace(" ","\u3000")

    # ストライクゾーン
    for t_strikeIdx in range(27):
        t_all_Course = soup.find_all('td', class_= 'hpb-cnt-tb-cell6')[t_strikeIdx].text
        if t_strikeIdx < 9:
            t_allData = re.split('\n|本|三振', t_all_Course)[0]

            # 打率
            # "---"データなしの場合は飛ばす
            if t_allData == "---":
                t_courseList = t_courseList + [t_allData]
            # 例外:htmlフォーマットの違いで""が取得される場合も"---"と同義のため、補間処理を行う
            elif t_allData == "":
                t_allData = "---"
                t_courseList = t_courseList + [t_allData]
            # 打率を計算する
            else:
                t_list = [int(t_batIdx) for t_batIdx in t_allData.split("-")]
                t_strikeAverage = t_list[1]/t_list[0]
                t_strikeAverageRound = Decimal(str(t_strikeAverage)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
                t_courseList = t_courseList + [str(t_strikeAverageRound)]  # type: ignore

    # ボールゾーン(通算)
    for t_ballIdx in range(48):
        t_all_Course = soup.find_all('td', class_= 'hpb-cnt-tb-cell5')[t_ballIdx].text
        if t_ballIdx < 16:
            t_allData = re.split('\n|本|三振', t_all_Course)[0]

            # 打率
            # "---"データなしの場合は飛ばす
            if t_allData == "---":
                t_courseList = t_courseList + [t_allData]
            # 例外:htmlフォーマットの違いで""が取得される場合も"---"と同義のため、補間処理を行う
            elif t_allData == "":
                t_allData = "---"
                t_courseList = t_courseList + [t_allData]
            # 打率を計算する
            else:
                t_list = [int(t_batIdx) for t_batIdx in t_allData.split("-")]
                t_ballAverage = t_list[1]/t_list[0]
                t_ballAverageRound = Decimal(str(t_ballAverage)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
                t_courseList = t_courseList + [str(t_ballAverageRound)]  # type: ignore

################### チーム名取得仕様 ###################
# 2022年以外：日本人
# t_playerNameSplit[6]
# 0:年度
# 1:姓
# 2:名
# 3:チーム名
# 4:''
# 5:コース別云々

# 2022年：日本人
# t_playerNameSplit[5]
# 0:姓
# 1:名
# 2:チーム名
# 3:''
# 4:コース別云々

# 2022年以外：外人
# t_playerNameSplit[5]
# 0:年度
# 1:名前
# 2:チーム名
# 3:''
# 4:コース別云々

# 2022年：外人
# t_playerNameSplit[4]
# 0:名前
# 1:チーム名
# 2:''
# 3:コース別云々
################### チーム名取得仕様 ###################

    t_playerNameSplit = re.split("\u3000|【|】", t_playerName)
    if len(t_playerNameSplit) == 6:
        t_teamName = t_playerNameSplit[3]
    elif len(t_playerNameSplit) == 5:
        t_teamName = t_playerNameSplit[2]
    elif len(t_playerNameSplit) == 4:
        t_teamName = t_playerNameSplit[1]

    # DeNAは全角の場合と半角の場合があるため、ここで半角に統一
    if t_teamName == "ＤｅＮＡ":
        t_teamName = "DeNA"

    return t_courseList, t_teamName, t_invalid_flag

# 被投球数を取得
def getpitchedpiches(a_selectionEye_url):
    # 初期化
    t_sabr_list = []

    # Beautifulsoupでデータを取得
    # requests1回につき1s待つ
    time.sleep(1)
    r = requests.get(a_selectionEye_url)
    soup = BeautifulSoup(r.content, 'html.parser')

    t_sabr_list = t_sabr_list + [soup.select('body > div > div.main > div:nth-child(8) > table > tbody > tr > td.pnm')[0].text] # ボール球合計
    t_sabr_list = t_sabr_list + [soup.select('body > div > div.main > div:nth-child(8) > table > tbody > tr > td:nth-child(2)')[0].text] # ボール球見極数
    t_sabr_list = t_sabr_list + [soup.select('body > div > div.main > div:nth-child(8) > table > tbody > tr > td:nth-child(4)')[0].text] # ストライク球合計
    t_sabr_list = t_sabr_list + [soup.select('body > div > div.main > div:nth-child(8) > table > tbody > tr > td:nth-child(5)')[0].text] # ストライク見逃し数
    t_sabr_list = t_sabr_list + [soup.select('body > div > div.main > div:nth-child(8) > table > tbody > tr > td:nth-child(6)')[0].text] # ストライク空振り数

    return t_sabr_list

def getbasebatterdata(a_base_url):
    # デバッグ用に追加
    t_basedata_list = []
    try:
        # 初期化
        t_basedata_list = []
        t_exception_flag = False    # 例外フラグ

        # Beautifulsoupでデータを取得
        # requests1回につき1s待つ
        time.sleep(1)
        r = requests.get(a_base_url)
        soup = BeautifulSoup(r.content, 'html.parser')

        # 通算成績行を取得(文字列)
        t_total_str = soup.select('body > div > div.main > div.table-responsive > table > tbody > tr:nth-child(1)')[0].text
        # 改行文字列系を削除し、空白行でリスト分割
        t_total_list = t_total_str.replace("\n","").replace("\r","").split() # 引数なしのsplitは空白文字列による分割
        t_basedata_list = t_basedata_list + [t_total_list[20]] # 打席数(plateappearance)
        t_basedata_list = t_basedata_list + [t_total_list[5]]  # 安打数(hit)
        t_basedata_list = t_basedata_list + [t_total_list[6]]  # 単打数(single)
        t_basedata_list = t_basedata_list + [t_total_list[7]]  # 二塁打数(twobase)
        t_basedata_list = t_basedata_list + [t_total_list[8]]  # 三塁打数(threebase)
        t_basedata_list = t_basedata_list + [t_total_list[4]]  # 本塁打数(homerun)
        t_basedata_list = t_basedata_list + [t_total_list[23]] # 四球数(walk)
        t_basedata_list = t_basedata_list + [t_total_list[24]] # 死球数(hit-by-pitch)
        t_basedata_list = t_basedata_list + [t_total_list[37]] # 三振数(strikeout)
        t_basedata_list = t_basedata_list + [t_total_list[35]] # 併殺数(doubleplay)
        # 追加221118
        t_basedata_list = t_basedata_list + [t_total_list[21]] # 打数(atbats)
        t_basedata_list = t_basedata_list + [t_total_list[31]] # 犠飛(sacrificeflight)
        t_basedata_list = t_basedata_list + [t_total_list[28]] # 企犠打(allbunt)
        t_basedata_list = t_basedata_list + [t_total_list[29]] # 犠打(okbunt)
        t_basedata_list = t_basedata_list + [t_total_list[25]] # 企盗塁(allstolenbase)
        t_basedata_list = t_basedata_list + [t_total_list[26]] # 盗塁(stolenbase)

    except Exception as e:
        # 基本設計書の例外定義を参照すること。
        # 例外処理として、すべてノーデータとして埋め、SQLへ登録する。
        t_basedata_list = ["---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---"]
        t_exception_flag = True
        print("例外args:", e.args)

    return t_basedata_list, t_exception_flag

# sabrを取得
def getpitchersabr(a_sabr_archive_url):
    # 初期化
    t_sabr_list = []

    # Beautifulsoupでデータを取得
    # requests1回につき1s待つ
    time.sleep(1)
    r = requests.get(a_sabr_archive_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    t_qs = soup.select('body > div.container > div.main > div.table-responsive > table > tbody > tr > td:nth-child(6)')[0].text # QS数
    t_sabr_list = t_sabr_list + [''.join(t_qs.split())] # QS数

    return t_sabr_list

# TODO: feat: 投手ベースデータを取得 #20
def getbasepitcherdata(a_base_url):
    # デバッグ用に追加
    t_basedata_list = []
    try:
        # 初期化
        t_basedata_list = []
        t_exception_flag = False    # 例外フラグ

        # Beautifulsoupでデータを取得
        # requests1回につき1s待つ
        time.sleep(1)
        r = requests.get(a_base_url)
        soup = BeautifulSoup(r.content, 'html.parser')

        # 通算成績行を取得(文字列)
        t_total_str = soup.select('body > div > div.main > div.table-responsive > table > tbody > tr:nth-child(1)')[0].text
        # 改行文字列系を削除し、空白行でリスト分割
        t_total_list = t_total_str.replace("\n","").replace("\r","").split() # 引数なしのsplitは空白文字列による分割
        # リストサイズが35の場合、投球回に分数を含む
        if len(t_total_list) != 35:
            t_basedata_list = t_basedata_list + [t_total_list[3]] # 勝(win)
            t_basedata_list = t_basedata_list + [t_total_list[4]]  # 負(lose)
            t_basedata_list = t_basedata_list + [t_total_list[5]]  # セーブ(save)
            t_basedata_list = t_basedata_list + [t_total_list[6]]  # 奪三振(strikeout)
            t_basedata_list = t_basedata_list + [t_total_list[7]]  # 試合数(numofmatches)
            t_basedata_list = t_basedata_list + [t_total_list[8]]  # 投球回(innings)
            t_basedata_list = t_basedata_list + [t_total_list[9]]  # 奪三振率(strikeoutrate)
            t_basedata_list = t_basedata_list + [t_total_list[10]]  # 投球数(numofpitches)
            t_basedata_list = t_basedata_list + [t_total_list[11]]  # 打者数(numofbatters)
            t_basedata_list = t_basedata_list + [t_total_list[12]]  # 被安打(hitsallowed)
            t_basedata_list = t_basedata_list + [t_total_list[13]]  # 被本塁打(homerunallowed)
            t_basedata_list = t_basedata_list + [t_total_list[14]]  # 与四球(Bases on Balls)
            t_basedata_list = t_basedata_list + [t_total_list[15]]  # 与死球(Hit by Pitch)
            t_basedata_list = t_basedata_list + [t_total_list[16]]  # 敬遠(intentional walk)
            t_basedata_list = t_basedata_list + [t_total_list[17]]  # 失点(Runs Allowed)
            t_basedata_list = t_basedata_list + [t_total_list[18]]  # 自責点(Earned Runs)
            t_basedata_list = t_basedata_list + [t_total_list[19]]  # 完投(Complete Games)
            t_basedata_list = t_basedata_list + [t_total_list[20]]  # 完封(Shutouts)
            t_basedata_list = t_basedata_list + [t_total_list[21]]  # 無四球(nowalk)
            t_basedata_list = t_basedata_list + [t_total_list[22]]  # 被打率(Opponents Batting Average)
            t_basedata_list = t_basedata_list + [t_total_list[23]]  # QS率(QSrate)
            t_basedata_list = t_basedata_list + [t_total_list[24]]  # 援護点(support point)
            t_basedata_list = t_basedata_list + [t_total_list[25]]  # 援護率(run support)
            t_basedata_list = t_basedata_list + [t_total_list[26]]  # WHIP()
            t_basedata_list = t_basedata_list + [t_total_list[31]]  # 最高球速(max speed)
            t_basedata_list = t_basedata_list + [t_total_list[32]]  # 最低球速(min speed)
            t_basedata_list = t_basedata_list + [t_total_list[33]]  # 球速差(ball speed difference)
        elif len(t_total_list) == 35:
            t_basedata_list = t_basedata_list + [t_total_list[3]] # 勝(win)
            t_basedata_list = t_basedata_list + [t_total_list[4]]  # 負(lose)
            t_basedata_list = t_basedata_list + [t_total_list[5]]  # セーブ(save)
            t_basedata_list = t_basedata_list + [t_total_list[6]]  # 奪三振(strikeout)
            t_basedata_list = t_basedata_list + [t_total_list[7]]  # 試合数(numofmatches)
            t_basedata_list = t_basedata_list + [t_total_list[8]+'+'+t_total_list[9]]  # 投球回(innings)
            t_basedata_list = t_basedata_list + [t_total_list[10]]  # 奪三振率(strikeoutrate)
            t_basedata_list = t_basedata_list + [t_total_list[11]]  # 投球数(numofpitches)
            t_basedata_list = t_basedata_list + [t_total_list[12]]  # 打者数(numofbatters)
            t_basedata_list = t_basedata_list + [t_total_list[13]]  # 被安打(hitsallowed)
            t_basedata_list = t_basedata_list + [t_total_list[14]]  # 被本塁打(homerunallowed)
            t_basedata_list = t_basedata_list + [t_total_list[15]]  # 与四球(Bases on Balls)
            t_basedata_list = t_basedata_list + [t_total_list[16]]  # 与死球(Hit by Pitch)
            t_basedata_list = t_basedata_list + [t_total_list[17]]  # 敬遠(intentional walk)
            t_basedata_list = t_basedata_list + [t_total_list[18]]  # 失点(Runs Allowed)
            t_basedata_list = t_basedata_list + [t_total_list[19]]  # 自責点(Earned Runs)
            t_basedata_list = t_basedata_list + [t_total_list[20]]  # 完投(Complete Games)
            t_basedata_list = t_basedata_list + [t_total_list[21]]  # 完封(Shutouts)
            t_basedata_list = t_basedata_list + [t_total_list[22]]  # 無四球(nowalk)
            t_basedata_list = t_basedata_list + [t_total_list[23]]  # 被打率(Opponents Batting Average)
            t_basedata_list = t_basedata_list + [t_total_list[24]]  # QS率(QSrate)
            t_basedata_list = t_basedata_list + [t_total_list[25]]  # 援護点(support point)
            t_basedata_list = t_basedata_list + [t_total_list[26]]  # 援護率(run support)
            t_basedata_list = t_basedata_list + [t_total_list[27]]  # WHIP()
            t_basedata_list = t_basedata_list + [t_total_list[32]]  # 最高球速(max speed)
            t_basedata_list = t_basedata_list + [t_total_list[33]]  # 最低球速(min speed)
            t_basedata_list = t_basedata_list + [t_total_list[34]]  # 球速差(ball speed difference)
            print("投球回数端数")
    except Exception as e:
        # 基本設計書の例外定義を参照すること。
        # 例外処理として、すべてノーデータとして埋め、SQLへ登録する。
        t_basedata_list = ["---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---"]
        t_exception_flag = True
        print("例外args:", e.args)


    return t_basedata_list, t_exception_flag

if __name__ == "__main__":
    import sys
    # getaverage(sys.argv[1])
    # getpitchedpiches(sys.argv[1])
    # getbasebatterdata(sys.argv[1])
    getbasebatterdata("https://baseballdata.jp/playerB/700027.html")
    # getatbatsnum("https://baseballdata.jp/playerB/1600089.html")
    # getaverage("https://baseballdata.jp/2018/playerP/800022_course.html")
    # getaverage("https://baseballdata.jp/2012/playerB/1100061_course.html")
# %%
