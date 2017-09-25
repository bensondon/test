#! /usr/bin/python
import smtplib
import string

HOST="smtp.youshang.cn"
SUBJECT="TEST MY PYTHON"
TO="biao_tang@kingdee.com"
FROM="ysmonitor@youshang.cn"
text="test my python"
BODY=string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
),"\r\n")

server = smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("ysmonitor@youshang.cn","qwerty")
server.sendmail(FROM,[TO],BODY)
server.quit()