import cx_Oracle
import smtplib
import string

connection = cx_Oracle.connect("monitor", "kingdee", "10.244.6.58/DBMONITOR")
cursor = connection.cursor()
result = cursor.execute(
        "select t.product_name,substr(t.sql_txt,0,50) sqltext,t.sql_id,t.eqs,t.executions,t.last_active_time,t.create_date  from t_db_slow_even t where t.last_active_time>sysdate- 1/24 ORDER BY create_date DESC")

a2=cursor.fetchall()

# for a1 in result:
#    a2.append(a1)

print str(a2)


#
# HOST="smtp.youshang.cn"
# SUBJECT="Oracle Slow SQL Report"
# TO="biao_tang@kingdee.com"
# FROM="ysmonitor@youshang.cn"
# BODY=string.join((
#     "From: %s" % FROM,
#     "To: %s" % TO,
#     "Subject: %s" % SUBJECT,
#     "",
#     text1),"\r\n")
# server = smtplib.SMTP()
# server.connect(HOST,"25")
# server.starttls()
# server.login("ysmonitor@youshang.cn","ysicinga#2014")
# server.sendmail(FROM,[TO],BODY)
# server.quit()