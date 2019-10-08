#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '379207614@qq.com'  # 发件人邮箱账号
my_pass = 'syoqrrprjxnfbjee'  # 发件人邮箱密码
my_user = '1354091575@qq.com'  # 收件人邮箱账号，我这边发送给自己

def mail():
    ret = True
    try:
        msg = MIMEText(u"很多人都表示，在还没有功成名就的时候，没有资格去谈论爱情，"
                       u"所以他会眼睁睁看着自己爱的人离开，而不敢冲过去说：“我养你啊！”"
                       u"但事实上，等到他名利双收的时候，却已经忘记了爱，也是成就自我的一部分。"
                       u"尹天仇和柳飘飘这两个边缘人，他们在人世的苦海中相遇，刚开始互相嘲笑和打击对方，"
                       u"然而命运的几番周折，却将这两个受苦的灵魂终于连接在了一起。这里面，无关于身份，"
                       u"无关于金钱和地位，有的是双方的的怜悯和心疼，有共同坚守的位置，有一起看眺望的远方。",
                       'plain', 'utf-8')
        msg['From'] = formataddr(["AAAAAAA", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["BBBBBBB", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "---教程发送邮件测试---"  # 邮件的主题，也可以说是标题
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,my_user,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret




ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")