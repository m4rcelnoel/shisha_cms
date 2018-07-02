import mysql.connector
from mysql.connector import Error
 

def connect():

    """ Connect to MySQL database """

    cnx = mysql.connector.connect(host='62.108.32.183',
                                  port=3306,
                                  database='aumcfuom_allgemein',
                                  user='aumcf_info2',
                                  password='An4pu3$3')
    if cnx.is_connected():
            print('Connected to MySQL database')
    
    
    cursor = cnx.cursor()    
    query =("SELECT * FROM sort ")      
    result = []
    cursor.execute(query)
    
    for (i) in cursor:
        result.append(i)
    print(result)
 

    cnx.close()
    if (not cnx.is_connected()):
            print('Disconnected from MySQL database')
 
 
if __name__ == '__main__':
    connect()
    
'''
cursor = cnx.cursor()

query = ("SELECT * FROM brand ")


cursor.execute(query)

for i in cursor:
    print(i)

cursor.close()
cnx.close()
'''