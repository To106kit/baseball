import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import numpy as np
import sys

def sendgmail(a_exec_time, a_unit_flag):
    # 初期化
    bodyText = ""

    # メール送信必要項目
    sendAddress = 't.to106ki@gmail.com' #自分のメールアドレス
    password = 'eqyezsefmxmuwqux' #パスワード
    subject = '【実行完了】[BaseballPrj]getdata'
    fromAddress = 'BaseballPrj:getdata'
    toAddress = 't.to106ki@gmail.com'
    # 本文
    # minの場合
    if a_unit_flag == "sec":
        bodyText = f'''BaseballPrj:getdataの定期実行タスクが完了しました。\n実行時間は{a_exec_time}[sec]でした。\n '''
    elif a_unit_flag == "min":
        bodyText = f'''BaseballPrj:getdataの定期実行タスクが完了しました。\n実行時間は{a_exec_time}[min]でした。\n '''
    elif a_unit_flag == "hour":
        bodyText = f'''BaseballPrj:getdataの定期実行タスクが完了しました。\n実行時間は{a_exec_time}[hour]でした。\n '''


    # SMTPサーバに接続
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(sendAddress, password)

    # メール作成
    msg = MIMEText(bodyText)
    msg['Subject'] = subject
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Date'] = formatdate()

    # 作成したメールを送信
    smtpobj.send_message(msg)
    smtpobj.close()

    print("mail was send.")

if __name__ == "__main__":
    import sys
    sendgmail(sys.argv[1],sys.argv[2])