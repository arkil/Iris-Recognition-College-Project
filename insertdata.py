from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def insert_iris(iristb):
    query = "INSERT INTO iristb(ssn,fname,lname) " \
            "VALUES(%s,%s,%s)"
    
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.executemany(query, iristb)
 
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
    iristb = [('314654','krupali','mane'),
             ('23416541','arkil','thakkar'),
             ('65412','suhani','agrawal')]
    insert_iris(iristb)
if __name__ == '__main__':
    main()
