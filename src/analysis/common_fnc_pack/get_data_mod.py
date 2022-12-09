import numpy as np
import common_fnc_pack

# 打数
def get_atbat_fnc(a_np_array):
    ## 打数
    t_atbats = a_np_array[:,46].astype(int)
    return t_atbats

# 打席数
def get_plateappearance_fnc(a_np_array):
    t_plateappearance = a_np_array[:,36].astype(int)
    return t_plateappearance

# 選手名
def get_playername_fnc(a_np_array):
    # 選手名
    t_player_name = a_np_array[:,3]
    return t_player_name

# ボール球被投球数
def get_pitchedballsum_fnc(a_np_array):
    t_pitchedballsum = a_np_array[:,31].astype(int)
    return t_pitchedballsum

# ボール球見逃し数
def get_ballnoswing_fnc(a_np_array):
    t_ballnoswing = a_np_array[:,32].astype(int)
    return t_ballnoswing

# ストライク被投球数
def get_pitchedstrikesum_fnc(a_np_array):
    t_pitchedstrikesum = a_np_array[:,33].astype(int)
    return t_pitchedstrikesum

# ストライク見逃し数
def get_strikenoswing_fnc(a_np_array):
    t_strikenoswing = a_np_array[:,34].astype(int)
    return t_strikenoswing

# ストライク空振り数
def get_strikeeirswing_fnc(a_np_array):
    t_strikeeirswing = a_np_array[:,35].astype(int)
    return t_strikeeirswing

# 安打数
def get_allhit_fnc(a_np_array):
    t_allhit = a_np_array[:,37].astype(int)
    return t_allhit

# 死球数
def get_hitbypitch_fnc(a_np_array):
    t_hitbypitch = a_np_array[:,43].astype(int)
    return t_hitbypitch

# 四球数
def get_walk_fnc(a_np_array):
    t_walk = a_np_array[:,42].astype(int)
    return t_walk

# 犠飛
def get_sacrificeflight_fnc(a_np_array):
    t_sacrificeflight = a_np_array[:,47].astype(int)
    return t_sacrificeflight