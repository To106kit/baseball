# %%
import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import os
import time

pd.set_option('display.max_rows', 100)

# 出力csvファイルの絶対パスを作成
file_name = "ppa_sample.csv"
file_path = os.path.join(os.getcwd(),file_name)  # type: ignore

url_c = 'https://baseballdata.jp/ctop.html'
url_p = 'https://baseballdata.jp/ptop.html'

df_c = pd.read_html(url_c)
df_p = pd.read_html(url_p)

df_c = df_c[0]
df_p = df_p[0]

df1 = pd.concat([df_c, df_p])
# df1 = df1.drop([16, 31])
df1 = df1.reset_index(drop=True)
df1 = df1.drop(df1.index[[16, 28, 45, 51]])  # type: ignore
# 意味が分からないのでコメントアウト
df1 = df1.drop(df1.columns[[1, 2, 10]], axis=1)
df1 = df1.reset_index(drop=True)
df1['選手名'] = df1['選手名'].str.strip('1234567890:')

##########

url = 'https://baseballdata.jp/mdata/SQG.html'
df2 = pd.read_html(url)

pd.set_option('display.max_rows', 100)

df2 = df2[0]
df2 = df2.drop([16, 17, 33, 34, 50, 51])

df2.to_csv(file_path, index=False)

df2 = pd.read_csv(file_path, header=None, names=('球団', '選手名', 'ボール球計', '見極数', '見極率', 'ストライクゾーン計', '見逃', '空振', 'スイング率', '見逃率', '空振率'))
df2 = df2.reset_index(drop=True)
df2 = df2.drop([0, 1])

df2['ボール球計'] = df2['ボール球計'].astype(int)
df2['ストライクゾーン計'] = df2['ストライクゾーン計'].astype(int)
df2['被投球数'] = df2['ボール球計'] + df2['ストライクゾーン計']

df2 = df2.drop(df2.columns[[0, 2, 3, 4, 5, 6, 7, 8, 9 ,10]], axis=1)
##########

df = pd.merge(df1, df2, on='選手名')

df['PPA'] = round(df['被投球数'].astype(int) / df['打 席 数'].astype(int), 3)
df['BPA'] = round(df['四 球'].astype(int) / df['打 席 数'].astype(int), 3)
df['KPA'] = round(df['三 振'].astype(int) / df['打 席 数'].astype(int), 3)
df['出 塁 率'] = ('0' + df['出 塁 率'].astype(str)).astype(float)

df = df.sort_values('PPA')

# indexを更新
df = df.reset_index(drop=True)

# PPAチャート
ax = df.plot.barh('選手名', 'PPA')
fig1 = ax.get_figure()
plt.xticks((0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0))
plt.yticks(fontsize=6)

plt.xlabel('PPA')
plt.ylabel('選手名')
plt.grid(True)
plt.savefig("ppa.png")
plt.show(block=False)
plt.close(fig1)

# KPAチャート
df_kpa = df.sort_values('KPA')
# indexを更新
df_kpa = df_kpa.reset_index(drop=True)
ax = df_kpa.plot.barh('選手名', 'KPA')
fig2 = ax.get_figure()
plt.xticks((0.0, 0.05, 0.075, 0.100, 0.125, 0.150, 0.175, 0.200, 0.225, 0.250, 0.275, 0.300))
plt.yticks(fontsize=6)
plt.xlabel('KPA')
plt.ylabel('選手名')
plt.grid(True)
plt.savefig("kpa.png")
plt.show(block=False)
plt.close(fig2)

# KPAチャート
df_kpa = df.sort_values('BPA')
# indexを更新
df_kpa = df_kpa.reset_index(drop=True)
ax = df_kpa.plot.barh('選手名', 'BPA')
fig2 = ax.get_figure()
plt.xticks((0.0, 0.025, 0.05, 0.075, 0.100, 0.125, 0.150, 0.175, 0.200, 0.225, 0.250))
plt.yticks(fontsize=6)
plt.xlabel('BPA')
plt.ylabel('選手名')
plt.grid(True)
plt.savefig("bpa.png")
plt.show(block=False)
plt.close(fig2)

for i, txt in enumerate(df['選手名'].values):
   plt.scatter(x=df['PPA'], y=df['出 塁 率'], c="blue")
   plt.annotate(txt, (df['PPA'][i], df['出 塁 率'][i]), size=df['BPA'][i]*120)

# %%
plt.xlabel('PPA')
plt.ylabel('出塁率')
plt.grid(True)
plt.savefig("ppa_shuturui.png")
plt.show(block=False)
plt.close()
# %%
