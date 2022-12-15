# MYSQLdbのインポート
import MySQLdb

def addsql_batter(a_batterDataList):
    t_batterDataList = a_batterDataList
    # DBへの接続とカーソルの生成
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='to106kita9ma',
        db='python_db',
        # db='python_test',
        # db='a',
        # テーブル内部で日本語を扱うために追加
        charset='utf8'
    )
    cursor = connection.cursor()

    # ここに実行したいコードを入力します

    # テーブルの初期化
    cursor.execute("DROP TABLE IF EXISTS batter_course_list")

        # データの追加
    for t_idx, t_elm in enumerate(t_batterDataList):
        # テーブルの作成
        cursor.execute("""CREATE TABLE IF NOT EXISTS batter_course_list(
            id INT(11) AUTO_INCREMENT NOT NULL,
            playerid VARCHAR(8) NOT NULL,
            role VARCHAR(8) NOT NULL,
            name VARCHAR(30) NOT NULL COLLATE utf8mb4_unicode_ci,
            team VARCHAR(10) NOT NULL COLLATE utf8mb4_unicode_ci,
            year VARCHAR(10) NOT NULL,
            s1 VARCHAR(10) NOT NULL,
            s2 VARCHAR(10) NOT NULL,
            s3 VARCHAR(10) NOT NULL,
            s4 VARCHAR(10) NOT NULL,
            s5 VARCHAR(10) NOT NULL,
            s6 VARCHAR(10) NOT NULL,
            s7 VARCHAR(10) NOT NULL,
            s8 VARCHAR(10) NOT NULL,
            s9 VARCHAR(10) NOT NULL,
            b1 VARCHAR(10) NOT NULL,
            b2 VARCHAR(10) NOT NULL,
            b3 VARCHAR(10) NOT NULL,
            b4 VARCHAR(10) NOT NULL,
            b5 VARCHAR(10) NOT NULL,
            b6 VARCHAR(10) NOT NULL,
            b7 VARCHAR(10) NOT NULL,
            b8 VARCHAR(10) NOT NULL,
            b9 VARCHAR(10) NOT NULL,
            b10 VARCHAR(10) NOT NULL,
            b11 VARCHAR(10) NOT NULL,
            b12 VARCHAR(10) NOT NULL,
            b13 VARCHAR(10) NOT NULL,
            b14 VARCHAR(10) NOT NULL,
            b15 VARCHAR(10) NOT NULL,
            b16 VARCHAR(10) NOT NULL,
            ballsum VARCHAR(10) NOT NULL,
            ballnoswing VARCHAR(10) NOT NULL,
            strikesum VARCHAR(10) NOT NULL,
            strikenoswing VARCHAR(10) NOT NULL,
            strikeeirswing VARCHAR(10) NOT NULL,
            plateappearance VARCHAR(10) NOT NULL,
            hit VARCHAR(10) NOT NULL,
            single VARCHAR(10) NOT NULL,
            twobase VARCHAR(10) NOT NULL,
            threebase VARCHAR(10) NOT NULL,
            homerun VARCHAR(10) NOT NULL,
            walk VARCHAR(10) NOT NULL,
            hitbypitch VARCHAR(10) NOT NULL,
            strikeout VARCHAR(10) NOT NULL,
            doubleplay VARCHAR(10) NOT NULL,
            atbats VARCHAR(10) NOT NULL,
            sacrificeflight VARCHAR(10) NOT NULL,
            allbunt VARCHAR(10) NOT NULL,
            okbunt VARCHAR(10) NOT NULL,
            allstolenbase VARCHAR(10) NOT NULL,
            stolenbase VARCHAR(10) NOT NULL,
            PRIMARY KEY (id)
            )""")


        cursor.execute("""INSERT INTO batter_course_list (playerid, role, name, team, year, \
                        s1, s2, s3, s4, s5, s6, s7, s8, s9, b1, b2, b3, b4, b5, b6, b7, b8, b9, \
                        b10, b11, b12, b13, b14, b15, b16, \
                        ballsum, ballnoswing, strikesum, strikenoswing, strikeeirswing, \
                        plateappearance, hit, single, twobase, threebase, homerun, walk, hitbypitch, strikeout, doubleplay, \
                        atbats , sacrificeflight, allbunt, okbunt, allstolenbase, stolenbase)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (t_batterDataList[t_idx][28], t_batterDataList[t_idx][29], t_batterDataList[t_idx][25], t_batterDataList[t_idx][27], t_batterDataList[t_idx][26], \
                    t_batterDataList[t_idx][0],t_batterDataList[t_idx][1], t_batterDataList[t_idx][2], \
                    t_batterDataList[t_idx][3], t_batterDataList[t_idx][4], t_batterDataList[t_idx][5], \
                    t_batterDataList[t_idx][6],t_batterDataList[t_idx][7],t_batterDataList[t_idx][8], \
                    t_batterDataList[t_idx][9],t_batterDataList[t_idx][10],t_batterDataList[t_idx][11], \
                    t_batterDataList[t_idx][12],t_batterDataList[t_idx][13],t_batterDataList[t_idx][14], \
                    t_batterDataList[t_idx][15],t_batterDataList[t_idx][16],t_batterDataList[t_idx][17], \
                    t_batterDataList[t_idx][18],t_batterDataList[t_idx][19],t_batterDataList[t_idx][20], \
                    t_batterDataList[t_idx][21],t_batterDataList[t_idx][22],t_batterDataList[t_idx][23], \
                    t_batterDataList[t_idx][24],t_batterDataList[t_idx][30],t_batterDataList[t_idx][31], \
                    t_batterDataList[t_idx][32],t_batterDataList[t_idx][33],t_batterDataList[t_idx][34], \
                    t_batterDataList[t_idx][35],t_batterDataList[t_idx][36],t_batterDataList[t_idx][37], \
                    t_batterDataList[t_idx][38],t_batterDataList[t_idx][39],t_batterDataList[t_idx][40], \
                    t_batterDataList[t_idx][41],t_batterDataList[t_idx][42],t_batterDataList[t_idx][43], \
                    t_batterDataList[t_idx][44],t_batterDataList[t_idx][45],t_batterDataList[t_idx][46], \
                    t_batterDataList[t_idx][47],t_batterDataList[t_idx][48],t_batterDataList[t_idx][49], \
                    t_batterDataList[t_idx][50]
                ))

    # 保存を実行
    connection.commit()

    # 接続を閉じる
    connection.close()

    print("########## addsql_batter end ################")


def addsql_picher(a_picherDataList):
    t_picherDataList = a_picherDataList

    # DBへの接続とカーソルの生成
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='to106kita9ma',
        db='python_db',
        # db='python_test',
        # db='a',
        # テーブル内部で日本語を扱うために追加
        charset='utf8'
    )
    cursor = connection.cursor()

    # ここに実行したいコードを入力します

    # テーブルの初期化
    cursor.execute("DROP TABLE IF EXISTS pitcher_course_list")
    # データの追加
    for t_idx, t_elm in enumerate(t_picherDataList):
        # テーブルの作成
        cursor.execute("""CREATE TABLE IF NOT EXISTS pitcher_course_list(
            id INT(11) AUTO_INCREMENT NOT NULL,
            playerid VARCHAR(8) NOT NULL,
            role VARCHAR(8) NOT NULL,
            name VARCHAR(30) NOT NULL COLLATE utf8mb4_unicode_ci,
            team VARCHAR(10) NOT NULL COLLATE utf8mb4_unicode_ci,
            year VARCHAR(10) NOT NULL,
            s1 VARCHAR(10) NOT NULL,
            s2 VARCHAR(10) NOT NULL,
            s3 VARCHAR(10) NOT NULL,
            s4 VARCHAR(10) NOT NULL,
            s5 VARCHAR(10) NOT NULL,
            s6 VARCHAR(10) NOT NULL,
            s7 VARCHAR(10) NOT NULL,
            s8 VARCHAR(10) NOT NULL,
            s9 VARCHAR(10) NOT NULL,
            b1 VARCHAR(10) NOT NULL,
            b2 VARCHAR(10) NOT NULL,
            b3 VARCHAR(10) NOT NULL,
            b4 VARCHAR(10) NOT NULL,
            b5 VARCHAR(10) NOT NULL,
            b6 VARCHAR(10) NOT NULL,
            b7 VARCHAR(10) NOT NULL,
            b8 VARCHAR(10) NOT NULL,
            b9 VARCHAR(10) NOT NULL,
            b10 VARCHAR(10) NOT NULL,
            b11 VARCHAR(10) NOT NULL,
            b12 VARCHAR(10) NOT NULL,
            b13 VARCHAR(10) NOT NULL,
            b14 VARCHAR(10) NOT NULL,
            b15 VARCHAR(10) NOT NULL,
            b16 VARCHAR(10) NOT NULL,
            numqs VARCHAR(10) NOT NULL,
            win VARCHAR(10) NOT NULL,
            lose VARCHAR(10) NOT NULL,
            save VARCHAR(10) NOT NULL,
            strikeout VARCHAR(10) NOT NULL,
            numofmatches VARCHAR(10) NOT NULL,
            innings VARCHAR(10) NOT NULL,
            strikeoutrate VARCHAR(10) NOT NULL,
            numofpitches VARCHAR(10) NOT NULL,
            numofbatters VARCHAR(10) NOT NULL,
            hitsallowed VARCHAR(10) NOT NULL,
            homerunallowed VARCHAR(10) NOT NULL,
            basesonballs VARCHAR(10) NOT NULL,
            hitbypitch VARCHAR(10) NOT NULL,
            intentionalwalk VARCHAR(10) NOT NULL,
            runsallowed VARCHAR(10) NOT NULL,
            earnedruns VARCHAR(10) NOT NULL,
            completegames VARCHAR(10) NOT NULL,
            shutouts VARCHAR(10) NOT NULL,
            nowalk VARCHAR(10) NOT NULL,
            opponentsbattingaverage VARCHAR(10) NOT NULL,
            qsrate VARCHAR(10) NOT NULL,
            supportpoint VARCHAR(10) NOT NULL,
            runsupport VARCHAR(10) NOT NULL,
            whip VARCHAR(10) NOT NULL,
            maxspeed VARCHAR(10) NOT NULL,
            minspeed VARCHAR(10) NOT NULL,
            ballspeeddifference VARCHAR(10) NOT NULL,
            PRIMARY KEY (id)
            )""")


        cursor.execute("""INSERT INTO pitcher_course_list (playerid, role, name, team, year, \
                        s1, s2, s3, s4, s5, s6, s7, s8, s9, b1, b2, b3, b4, b5, b6, b7, b8, b9, \
                        b10, b11, b12, b13, b14, b15, b16, \
                        numqs, win, lose, save, strikeout, numofmatches, innings, strikeoutrate, numofpitches, numofbatters, \
                        hitsallowed, homerunallowed, basesonballs, hitbypitch, intentionalwalk, runsallowed, earnedruns, completegames, shutouts, \
                        nowalk, opponentsbattingaverage, qsrate, supportpoint, runsupport, whip, maxspeed, minspeed, ballspeeddifference)

            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (t_picherDataList[t_idx][28], t_picherDataList[t_idx][29], t_picherDataList[t_idx][25], t_picherDataList[t_idx][27], t_picherDataList[t_idx][26], \
                    t_picherDataList[t_idx][0],t_picherDataList[t_idx][1], t_picherDataList[t_idx][2], \
                    t_picherDataList[t_idx][3], t_picherDataList[t_idx][4], t_picherDataList[t_idx][5], \
                    t_picherDataList[t_idx][6],t_picherDataList[t_idx][7],t_picherDataList[t_idx][8], \
                    t_picherDataList[t_idx][9],t_picherDataList[t_idx][10],t_picherDataList[t_idx][11], \
                    t_picherDataList[t_idx][12],t_picherDataList[t_idx][13],t_picherDataList[t_idx][14], \
                    t_picherDataList[t_idx][15],t_picherDataList[t_idx][16],t_picherDataList[t_idx][17], \
                    t_picherDataList[t_idx][18],t_picherDataList[t_idx][19],t_picherDataList[t_idx][20], \
                    t_picherDataList[t_idx][21],t_picherDataList[t_idx][22],t_picherDataList[t_idx][23], \
                    t_picherDataList[t_idx][24],\
                    t_picherDataList[t_idx][30],t_picherDataList[t_idx][31],t_picherDataList[t_idx][32], \
                    t_picherDataList[t_idx][33],t_picherDataList[t_idx][34],t_picherDataList[t_idx][35], \
                    t_picherDataList[t_idx][36],t_picherDataList[t_idx][37],t_picherDataList[t_idx][38], \
                    t_picherDataList[t_idx][39],t_picherDataList[t_idx][40],t_picherDataList[t_idx][41], \
                    t_picherDataList[t_idx][42],t_picherDataList[t_idx][43],t_picherDataList[t_idx][44], \
                    t_picherDataList[t_idx][45],t_picherDataList[t_idx][46],t_picherDataList[t_idx][47], \
                    t_picherDataList[t_idx][48],t_picherDataList[t_idx][49],t_picherDataList[t_idx][50], \
                    t_picherDataList[t_idx][51],t_picherDataList[t_idx][52],t_picherDataList[t_idx][53], \
                    t_picherDataList[t_idx][54],t_picherDataList[t_idx][55],t_picherDataList[t_idx][56], \
                    t_picherDataList[t_idx][57]
                ))

    # 保存を実行
    connection.commit()

    # 接続を閉じる
    connection.close()

    print("########## addsql_picher end ################")
