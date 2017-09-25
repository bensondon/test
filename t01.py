import cx_Oracle
connection = cx_Oracle.connect("monitor", "kingdee", "10.244.6.58/DBMONITOR");
cursor = connection.cursor()
cursor.execute("select sysdate from dual")
for date in cursor:
    print ("SYSDATE:", date)