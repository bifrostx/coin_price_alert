# -*- coding: utf-8 -*-
import time
import datetime
import smtplib
import email.mime.multipart
import email.mime.text
from coin_price import get_total


def send_email(asset):
    now = datetime.datetime.now() 
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = 'bifrost_xin@163.com'
    msg['to'] = 'cindy881216@126.com'
    msg['subject'] = 'Crypto Currency Alert'
    content = "Your asset is now about " + str(asset) + " CNY."
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', '25')
    smtp.login('bifrost_xin@163.com', 'test12345')
    smtp.sendmail('bifrost_xin@163.com', 'cindy881216@126.com', str(msg))
    smtp.quit()
    print(now, end=': ')
    print("email sent succesful.")



if __name__ == "__main__":
    upper = 700000
    lower = 600000
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
            now = datetime.datetime.now()
            print(now, end=': ')
            print("not reach the next level, no email sent.")

        time.sleep(24 * 3600)


