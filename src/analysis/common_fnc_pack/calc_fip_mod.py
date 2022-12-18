import numpy as np
import common_fnc_pack
from fractions import Fraction


# イニングの端数を計算する
def convert_innings_local_fnc(a_innings):
    # 初期化
    t_totalInnings = []
    t_innings = a_innings.copy()
    t_fraction_innings_list = []


    t_invalid_str = "/" # イニングが端数の場合はその行を計算する。
    for t_idx in range(a_innings.shape[0]):
        if np.any(t_invalid_str in a_innings[t_idx]):
            # イニングの端数を分数に表現
            t_split_list = t_innings[t_idx].split('+')
            # 端数
            t_fraction_list = t_split_list[1].split('/')

            # イニング→打者数に変換(*3)
            t_main = int(t_split_list[0]) * 3
            t_fraction = int(t_fraction_list[0]) / int(t_fraction_list[1]) * 3
            t_allout = t_main + t_fraction

            # Fractionモジュール使用して端数分数化
            t_totalInnings = t_totalInnings + [int(t_allout)]
        else:
            t_totalInnings = t_totalInnings + [a_innings[t_idx].astype(int).tolist() * 3]

    return t_totalInnings


# FIPを計算
def calc_fip_fnc(a_year_idx, a_team, a_np_pitcher_array):
    # 被本塁打
    t_np_homerunallowed = common_fnc_pack.get_pitcher_data_mod.get_homerunallowed_fnc(a_np_pitcher_array)
    # 与四球
    t_np_basesonballs = common_fnc_pack.get_pitcher_data_mod.get_basesonballs_fnc(a_np_pitcher_array)
    # 与死球
    t_np_hitbypitch = common_fnc_pack.get_pitcher_data_mod.get_hitbypitch_fnc(a_np_pitcher_array)
    # 敬遠
    t_np_intentionalwalk = common_fnc_pack.get_pitcher_data_mod.get_intentionalwalk_fnc(a_np_pitcher_array)
    # 奪三振
    t_np_strikeout = common_fnc_pack.get_pitcher_data_mod.get_strikeout_fnc(a_np_pitcher_array)
    # 投球回
    t_np_innings = common_fnc_pack.get_pitcher_data_mod.get_innings_fnc(a_np_pitcher_array)
    # イニングの端数を計算する
    t_totalOut = convert_innings_local_fnc(t_np_innings)
    t_np_totalOut = np.array(t_totalOut)

    # リーグトータルデータ取得
    ## リーグ平均防御率を取得
    t_np_era = common_fnc_pack.calc_league_total_era_mod.calc_league_total_era_fnc(a_year_idx, a_team)
    ## リーグトータル被本塁打
    t_league_total_homerunallowed = common_fnc_pack.calc_league_total_homerunallowed_mod.calc_league_total_homerunallowed_fnc(a_year_idx, a_team)
    ## リーグトータル四球数
    t_league_total_basesonballs = common_fnc_pack.calc_league_total_basesonballs_mod.calc_league_total_basesonballs_fnc(a_year_idx, a_team)
    ## リーグトータル死球数
    t_league_total_hitbypitch = common_fnc_pack.calc_league_total_hitbypitch_mod.calc_league_total_hitbypitch_fnc(a_year_idx, a_team)
    ## リーグトータル敬遠数
    t_league_total_intentionalwalk = common_fnc_pack.calc_league_total_intentionalwalk_mod.calc_league_total_intentionalwalk_fnc(a_year_idx, a_team)
    ## リーグトータル奪三振数
    t_league_total_strikeout = common_fnc_pack.calc_league_total_strikeout_mod.calc_league_total_strikeout_fnc(a_year_idx, a_team)
    ## リーグトータル投球回数
    t_league_total_innings = common_fnc_pack.calc_league_total_innings_mod.calc_league_total_innings_fnc(a_year_idx, a_team)

    # FIP計算
    ## 計算式
    #※リーグ補正値＝リーグ全体の防御率−｛１３×全被本塁打数＋３×（全四死球数−全敬遠数）−２×全奪三振数｝／全投球回数(=総アウト数/3)
    t_correction_value = t_np_era - (((t_league_total_homerunallowed * 13) + ((t_league_total_basesonballs - t_league_total_intentionalwalk + t_league_total_hitbypitch) * 3) \
                        - (t_league_total_strikeout * 2)) / t_league_total_innings)

    # FIP ＝ [(被本塁打×13) ＋ {(与四球 ＋ 与死球 － 敬遠) × 3} － (奪三振×2)] ÷ 投球回 ＋ リーグ補正値
    # t_fip = ((t_np_homerunallowed * 13) + ((t_np_basesonballs - t_np_intentionalwalk + t_np_hitbypitch) * 3) - (t_np_strikeout * 2)) / t_np_totalOut * 3 + t_correction_value
    # リーグ補正値=3.12固定の場合※データで楽しむプロ野球では3.12固定にしている。
    t_fip = ((t_np_homerunallowed * 13) + ((t_np_basesonballs - t_np_intentionalwalk + t_np_hitbypitch) * 3) - (t_np_strikeout * 2)) / t_np_totalOut * 3 + 3.12
    t_fip_round = np.round(t_fip, 3)

    return t_fip_round