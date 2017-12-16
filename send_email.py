# -*- coding: utf-8 -*-
import time
import smtplib
import email.mime.multipart
import email.mime.text
from coin_price import get_total


def send_email(asset):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = 'bifrost_xin@163.com'
    msg['to'] = 'bifrost_xin@163.com'
    msg['subject'] = '虚拟资产通知'
    content = "目前总资产为" + str(asset) + "人民币。"
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', '25')
    smtp.login('bifrost_xin@163.com', 'test12345')
    smtp.sendmail('bifrost_xin@163.com', 'bifrost_xin@163.com', str(msg))
    smtp.quit()
    print("email sent succesful.")


if __name__ == "__main__":
    upper = 600000
    lower = 500000
    scale = 100000
    while True:
        asset = get_total()
        if asset > upper:
            send_email(asset)
            upper += scale
            lower += scale
        elif asset < lower:
            send_email(asset)
            upper -= scale
            lower -= scale
        else:
            print("nothing happened today.")

        time.sleep(24 * 3600)


