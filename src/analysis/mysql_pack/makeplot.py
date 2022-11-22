# MYSQLdbのインポート
#%%
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt

# DBへの接続とカーソルの生成
connection = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='to106kita9ma',
    db='python_db',
    # テーブル内部で日本語を扱うために追加
    charset='utf8'
)

# コネクションが切れたときに再接続してくれるように設定
# connection.ping(reconnect=True)

# 接続できているかの確認
# print(connection.is_connected())

cursor = connection.cursor()

cursor.execute("SELECT * from batter_course_list")

# 全てのデータを取得
rows = cursor.fetchall()
t_list = list(rows)
t_np_array = np.array(t_list)

# %%

# plot用
# x軸(年度)
x = t_np_array[:,3]

# "---"は0に変換
t_np_array = np.char.replace(t_np_array, "---","0.000")


# y軸(ストライクゾーン毎の打率)
y_s1 = [float(i) for i in t_np_array[:,4]]
y_s2 = [float(i) for i in t_np_array[:,5]]
y_s3 = [float(i) for i in t_np_array[:,6]]
y_s4 = [float(i) for i in t_np_array[:,7]]
y_s5 = [float(i) for i in t_np_array[:,8]]
y_s6 = [float(i) for i in t_np_array[:,9]]
y_s7 = [float(i) for i in t_np_array[:,10]]
y_s8 = [float(i) for i in t_np_array[:,11]]
y_s9 = [float(i) for i in t_np_array[:,12]]

# プロット
plt.plot(x,y_s1,label="s1")
plt.plot(x,y_s2,label="s2")
plt.plot(x,y_s3,label="s3")
plt.plot(x,y_s4,label="s4")
plt.plot(x,y_s5,label="s5")
plt.plot(x,y_s6,label="s6")
plt.plot(x,y_s7,label="s7")
plt.plot(x,y_s8,label="s8")
plt.plot(x,y_s9,label="s9")
plt.legend()
plt.show()
#%%
for row in rows:
    print(row)


# DB操作が終わったらコネクションを閉じる
cursor.close()
connection.close()