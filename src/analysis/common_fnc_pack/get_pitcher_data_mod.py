import numpy as np
import common_fnc_pack

# playerid
def get_playerid_fnc(a_np_array):
    t_playerid = a_np_array[:,1]
    return t_playerid

# roll
def get_roll_fnc(a_np_array):
    t_roll = a_np_array[:,2]
    return t_roll

# 選手名
def get_playername_fnc(a_np_array):
    t_player_name = a_np_array[:,3]
    return t_player_name

# 選手名
def get_team_fnc(a_np_array):
    t_team = a_np_array[:,4]
    return t_team

# year
def get_year_fnc(a_np_array):
    t_year = a_np_array[:,5]
    return t_year

# qs数
def get_numqs_fnc(a_np_array):
    t_numqs = a_np_array[:,31].astype(int)
    return t_numqs

# 勝
def get_win_fnc(a_np_array):
    t_win = a_np_array[:,32].astype(int)
    return t_win

# 負け
def get_lose_fnc(a_np_array):
    t_lose = a_np_array[:,33].astype(int)
    return t_lose

# セーブ
def get_save_fnc(a_np_array):
    t_save = a_np_array[:,34].astype(int)
    return t_save

# 奪三振
def get_strikeout_fnc(a_np_array):
    t_strikeout = a_np_array[:,35].astype(int)
    return t_strikeout

# 登板数
def get_numofmatches_fnc(a_np_array):
    t_numofmatches = a_np_array[:,36].astype(int)
    return t_numofmatches

# イニング
def get_innings_fnc(a_np_array):
    t_innings = a_np_array[:,37]
    return t_innings

# 奪三振率
def get_strikeoutrate_fnc(a_np_array):
    t_strikeoutrate = a_np_array[:,38].astype(float)
    return t_strikeoutrate

# 投球数
def get_numofpitches_fnc(a_np_array):
    t_numofpitches = a_np_array[:,39].astype(int)
    return t_numofpitches

# 対戦打者数
def get_numofbatters_fnc(a_np_array):
    t_numofbatters = a_np_array[:,40].astype(int)
    return t_numofbatters

# 被安打数
def get_hitsallowed_fnc(a_np_array):
    t_hitallowed = a_np_array[:,41].astype(int)
    return t_hitallowed

# 被本塁打数
def get_homerunallowed_fnc(a_np_array):
    t_homerunallowed = a_np_array[:,42].astype(int)
    return t_homerunallowed

# 与四球
def get_basesonballs_fnc(a_np_array):
    t_basesonballs = a_np_array[:,43].astype(int)
    return t_basesonballs

# 与死球
def get_hitbypitch_fnc(a_np_array):
    t_hitbypitch = a_np_array[:,44].astype(int)
    return t_hitbypitch

# 敬遠
def get_intentionalwalk_fnc(a_np_array):
    t_intentionalwalk = a_np_array[:,45].astype(int)
    return t_intentionalwalk

# 失点
def get_runsallowed_fnc(a_np_array):
    t_runsallowed = a_np_array[:,46].astype(int)
    return t_runsallowed

# 自責点
def get_earnedruns_fnc(a_np_array):
    t_earnedruns = a_np_array[:,47].astype(int)
    return t_earnedruns

# 被打率
def get_opponentsbattingaverage_fnc(a_np_array):
    # # dtype=object にすれば + 演算子で先頭文字"0"を付与可能
    t_opponentsbattingaverage = a_np_array[:,51].astype(object)
    t_opponentsbattingaverage = "0" + t_opponentsbattingaverage
    # データ型をfloatに変更
    t_opponentsbattingaverage = t_opponentsbattingaverage.astype(float)
    return t_opponentsbattingaverage

# qs率
def get_qsrate_fnc(a_np_array):
    t_qsrate = a_np_array[:,52]
    t_qsrate = np.char.strip(t_qsrate, "%")
    t_qsrate = t_qsrate.astype(float)
    return t_qsrate

# 援護点
def get_supportpoint_fnc(a_np_array):
    t_supportpoint = a_np_array[:,53].astype(int)
    return t_supportpoint

# 援護率
def get_supportpointrate_fnc(a_np_array):
    t_supportpointrate = a_np_array[:,54].astype(float)
    return t_supportpointrate

# Whip
def get_whip_fnc(a_np_array):
    t_whip = a_np_array[:,55].astype(float)
    return t_whip

# 最高球速
def get_maxspeed_fnc(a_np_array):
    t_maxspeed = a_np_array[:,56].astype(int)
    return t_maxspeed

# 最低球速
def get_minspeed_fnc(a_np_array):
    t_minspeed = a_np_array[:,57].astype(int)
    return t_minspeed

# 球速差
def get_ballspeeddifference_fnc(a_np_array):
    t_ballspeeddifference = a_np_array[:,58].astype(int)
    return t_ballspeeddifference