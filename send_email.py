import smtplib
import email.mime.multipart
import email.mime.text


def send_email(from_addr, to_addr_list, subject, content):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = from_addr
    msg['to'] = ', '.join(to_addr_list)
    msg['subject'] = subject
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', '25')              # smtp server
    smtp.login('bifrost_xin@163.com', 'test12345')  # login to the server
    smtp.sendmail(from_addr, to_addr_list, str(msg))
    smtp.quit()
    print("email sent successful.")




