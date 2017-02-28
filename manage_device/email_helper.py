import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.text import MIMEText
from globals import *

mail_host = MAIL_HOST
smtp_port = SMTP_PORT
mail_user = username + "@ef.com"
mail_password = password


class EMAIL:
    def __init__(self, mail_to_list, title="Please return mobile device as soon as possible"):
        self.mail_to_list = mail_to_list
        self.subject = title

    def sent_mail(self):
        try:
            server = smtplib.SMTP(mail_host, smtp_port)
            server.starttls()

            server.login(mail_user, mail_password)
            me = mail_user

            msg = MIMEText(EMAIL_TEXT.format(self.mail_to_list, "iphone", MAX_DAY), 'text', 'utf-8')
            msg['From'] = me
            msg['To'] = ";".join(self.mail_to_list)
            msg['Subject'] = Header(self.subject, 'utf-8')
            server.sendmail(me, self.mail_to_list, msg.as_string())
            server.close()
            print("pass")
            return True

        except Exception:
            print("fail")
            return False


if __name__ == '__main__':
    email = EMAIL(["ming.xiesh@ef.com"])
    if (email.sent_mail()):
        print("success")
