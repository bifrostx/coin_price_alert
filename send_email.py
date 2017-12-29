import smtplib
from os.path import basename
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication


def send_email(from_addr, to_addr_list, subject, content, files=None):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = from_addr
    msg['to'] = ', '.join(to_addr_list)
    msg['subject'] = subject
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', '25')              # smtp server
    smtp.login('bifrost_xin@163.com', 'test12345')  # login to the server
    smtp.sendmail(from_addr, to_addr_list, msg.as_string())
    smtp.quit()
    print("email sent successful.")




