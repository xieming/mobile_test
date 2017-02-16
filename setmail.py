# -*- coding: cp936 -*-
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# mail_host = 'smtp.office365.com'
# smtp_port = 587
# mail_user = 'ming.xiesh@ef.com'
# mail_pwd = 'Good_Luck777'
# mail_to = 'ming.xiesh@ef.com'

mailto_list = ["mobileqa@EF.com"]  # 邮件接收方的邮件地址
mail_host = "smtp.office365.com"    # 邮件传送协议服务器
smtp_port = 587
mail_user = "ming.xiesh@ef.com"  # 邮件发送方的邮箱账号
mail_pass = "Good_Luck777"  # 邮件发送方的邮箱密码

def send_mail(to_list, sub, content):
    me = "Mobile QA"+"<"+mail_user+">"

    msg = MIMEMultipart()
    msg['Subject'] = sub    # 邮件主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    txt = MIMEText("Devices", _subtype='plain', _charset='utf8')
    msg.attach(txt)

    # <b>：黑体  <i>：斜体
    msgText = MIMEText('<b><i>This is a testing email</i> for mobile device management</b> mobile QA team.<img alt="" src="cid:image1" />please ignore it!', 'html', 'utf-8')
    msg.attach(msgText)

    file1 = "/Users/anderson/work/autotest/mobile_test/mobile_test/PieChart.png"
    image = MIMEImage(open(file1, 'rb').read())
    image.add_header('Content-ID', '<image1>')
    msg.attach(image)

    try:
        server = smtplib.SMTP(mail_host,smtp_port)
        #server.connect(mail_host,)
        server.starttls()
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        print("pass")
        return True

    except Exception:
        print("fail")
        return False

if __name__ == '__main__':

    sub = "mobile device management test email"

    html = '<html></html>'

    if send_mail(mailto_list, sub, html):

        print("发送成功")
    else:

        print("发送失败")


# -*- coding: cp936 -*-
# import smtplib
# from email.mime.text import MIMEText
#
# mail_host = 'smtp.office365.com'
# smtp_port = 587
# mail_user = 'ming.xiesh@ef.com'
# mail_pwd = 'Good_Luck777'
# mail_to = 'ming.xiesh@ef.com'
# # mail_cc = 'ming.xiesh@ef.com'
# #mail_bcc = 'xx@qq.com'
# content = 'this is a mail sent with python'
#
# # 表头信息www.iplaypython.com
# msg = MIMEText(content)
# msg['From'] = mail_user
# msg['Subject'] = 'this is a python test mail'
# msg['To'] = mail_to
# #msg['Cc'] = mail_cc
# #msg['Bcc'] = mail_bcc
# try:
#     s = smtplib.SMTP(mail_host,smtp_port)
#     s.starttls()
#     # s.connect(mail_host)
#     # login
#     print("login")
#     s.login(mail_user, mail_pwd)
#
#     # send mail
#     s.sendmail(mail_user, [mail_to], msg.as_string())
#     s.close()
#     print ('success')
#
# except Exception:
#     print("fail")

    # # -*- coding: cp936 -*-
    #
    # import smtplib
    # from email.mime.text import MIMEText
    #
    # mail_host = 'smtp.163.com'
    # mail_user = 'passionboyxie@163.com'
    # mail_pwd = 'Good_Luck888'
    # mail_to = 'passionboyxie@163.COM'
    # mail_cc = 'ming.xiesh@ef.com'
    # # mail_bcc = 'xx@qq.com'
    # content = 'this is a mail sent with python'
    #
    # # 表头信息www.iplaypython.com
    # msg = MIMEText(content)
    # msg['From'] = mail_user
    # msg['Subject'] = 'this is a python test mail'
    # msg['To'] = mail_to
    # msg['Cc'] = mail_cc
    # # msg['Bcc'] = mail_bcc
    # try:
    #     s = smtplib.SMTP()
    #     s.connect(mail_host)
    #     # login
    #     print("login")
    #     s.login(mail_user, mail_pwd)
    #
    #     # send mail
    #     s.sendmail(mail_user, [mail_to, mail_cc], msg.as_string())
    #     s.close()
    #     print('success')
    #
    # except Exception:
    #     print("fail")


# import smtplib
# from email.mime.text import MIMEText
#
# # mailto_list=[YYY@YYY.com]
# mailto_list = ['lucklly@163.com']
# mail_host = "smtp.163.com"
# mail_user = "passionboyxie@163.com"
# mail_pass = "Good_Luck888"
# mail_postfix = "163.com"
#
#
# def send_mail(to_list, sub, content):
#     me = "hello" + "<" + mail_user + "@" + mail_postfix + ">"
#     msg = MIMEText(content, _subtype='plain', _charset='gb2312')
#     msg['Subject'] = sub
#     msg['From'] = me
#     msg['To'] = ";".join(to_list)
#     try:
#         server = smtplib.SMTP()
#         server.connect(mail_host)
#         server.login(mail_user, mail_pass)
#         server.sendmail(me, to_list, msg.as_string())
#         server.close()
#         return True
#     except Exception:
#
#         return False
#
#
# if __name__ == '__main__':
#     if send_mail(mailto_list, "hello", "hello world！"):
#         print("success")
#     else:
#         print("fail")

# # !/usr/bin/env python3
# # coding: utf-8
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = 'passionboyxie@163.com'
# receiver = 'lucklly@163.com'
# subject = 'python email test'
# smtpserver = 'smtp.163.com'
# username = 'passionboyxie@163.com'
# password = 'Good_Luck888'
#
# msg = MIMEText('你好', 'text', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
# msg['Subject'] = Header(subject, 'utf-8')
#
# smtp = smtplib.SMTP()
# smtp.connect('smtp.163.com')
# smtp.login(username, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()