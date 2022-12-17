# MYSQLdbのインポート
import MySQLdb

def set_sql_batter_total(a_getdatalist):
    t_getdatalist = a_getdatalist
    # DBへの接続とカーソルの生成
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='to106kita9ma',
        # db='python_db',
        db='python_test',
        # db='a',
        # テーブル内部で日本語を扱うために追加
        charset='utf8'
    )
    cursor = connection.cursor()

    # ここに実行したいコードを入力します

    # テーブルの初期化
    cursor.execute("DROP TABLE IF EXISTS total_batter_list")

        # データの追加
    for t_idx, t_elm in enumerate(t_getdatalist):
        # テーブルの作成
        cursor.execute("""CREATE TABLE IF NOT EXISTS total_batter_list(
            id INT(11) AUTO_INCREMENT NOT NULL,
            year VARCHAR(10) NOT NULL,
            team VARCHAR(10) NOT NULL COLLATE utf8mb4_unicode_ci,
            打率 VARCHAR(10) NOT NULL,
            打点 VARCHAR(10) NOT NULL,
            本塁打 VARCHAR(10) NOT NULL,
            安打数 VARCHAR(10) NOT NULL,
            単打 VARCHAR(10) NOT NULL,
            二塁打 VARCHAR(10) NOT NULL,
            三塁打 VARCHAR(10) NOT NULL,
            出塁率 VARCHAR(10) NOT NULL,
            長打率 VARCHAR(10) NOT NULL,
            OPS VARCHAR(10) NOT NULL,
            得点圏打数 VARCHAR(10) NOT NULL,
            得点圏安打 VARCHAR(10) NOT NULL,
            得点圏打率 VARCHAR(10) NOT NULL,
            UC打数 VARCHAR(10) NOT NULL,
            UC安打 VARCHAR(10) NOT NULL,
            UC率 VARCHAR(10) NOT NULL,
            UC本塁打 VARCHAR(10) NOT NULL,
            試合数 VARCHAR(10) NOT NULL,
            打席数 VARCHAR(10) NOT NULL,
            打数 VARCHAR(10) NOT NULL,
            得点 VARCHAR(10) NOT NULL,
            四球 VARCHAR(10) NOT NULL,
            死球 VARCHAR(10) NOT NULL,
            企盗塁 VARCHAR(10) NOT NULL,
            盗塁 VARCHAR(10) NOT NULL,
            盗塁成功率 VARCHAR(10) NOT NULL,
            企犠打 VARCHAR(10) NOT NULL,
            犠打 VARCHAR(10) NOT NULL,
            犠打成功率 VARCHAR(10) NOT NULL,
            犠飛 VARCHAR(10) NOT NULL,
            代打数 VARCHAR(10) NOT NULL,
            代打安打 VARCHAR(10) NOT NULL,
            代打率 VARCHAR(10) NOT NULL,
            併殺 VARCHAR(10) NOT NULL,
            失策 VARCHAR(10) NOT NULL,
            三振 VARCHAR(10) NOT NULL,
            PRIMARY KEY (id)
            )""")


        cursor.execute("""INSERT INTO total_batter_list (year, team, 打率, 打点, 本塁打, 安打数, 単打, 二塁打, 三塁打, 出塁率,\
                                                        長打率, OPS, 得点圏打数, 得点圏安打, 得点圏打率, UC打数, UC安打, UC率, UC本塁打, 試合数,\
                                                        打席数, 打数, 得点, 四球, 死球, 企盗塁, 盗塁, 盗塁成功率, 企犠打, 犠打,\
                                                        犠打成功率, 犠飛, 代打数, 代打安打, 代打率, 併殺, 失策, 三振)

            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (t_elm[0], t_elm[1], t_elm[2], t_elm[3], t_elm[4], t_elm[5], t_elm[6], t_elm[7], t_elm[8], t_elm[9], t_elm[10],\
                    t_elm[11], t_elm[12], t_elm[13], t_elm[14], t_elm[15], t_elm[16], t_elm[17], t_elm[18], t_elm[19], t_elm[20],\
                    t_elm[21], t_elm[22], t_elm[23], t_elm[24], t_elm[25], t_elm[26], t_elm[27], t_elm[28], t_elm[29], t_elm[30],\
                    t_elm[31], t_elm[32], t_elm[33], t_elm[34], t_elm[35], t_elm[36], t_elm[37]
                ))

    # 保存を実行
    connection.commit()

    # 接続を閉じる
    connection.close()

    print("########## addsql_batter_total end ################")
