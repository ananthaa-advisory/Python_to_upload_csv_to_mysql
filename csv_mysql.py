##########
# Below code tested in Ubuntu 16.04.
########
#!/usr/bin/python3
import mysql.connector


# Below details for DBconnection as a dictonary
dbconfig = { 'host': '127.0.01', 'user': 'root', 'password': 'root', 'database' :'testdb' }
######
#below ** asterik --> Python will expands the single dictonary argument into four individual arguments  --> head first Python
#################
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()


#Reading the comma separated files:
with open("test","r") as file:
    file = file.readlines()
    for i in file:

        id = i.split(',')[0]
        user = i.split(',')[1]
        comment = i.rstrip('\n').split(',')[2]
        hello = (id,user,comment)
        print hello
        _sql = """insert into testtable (id,userid,comments) VALUES (%s,%s,%s)"""
        cursor.execute(_sql, hello)
        conn.commit()
