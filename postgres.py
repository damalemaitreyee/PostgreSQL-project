import psycopg2

class student:
    name = "dj"
    course = "adb"
    section = 3
    id = 10

def insert_student_data():
    conn = connect()
    cur = conn.cursor()
    student_data = student()
    query = """ INSERT INTO STUDENT (sname, sid, course, coursesection) VALUES (%s,%s,%s,%s)"""
    record_to_insert = (student_data.name, student_data.id, student_data.course, student_data.section)
    try:
        cur.execute(query,record_to_insert)
        conn.commit()
        print("records inserted")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def get_student_data():
    conn = connect()
    cur = conn.cursor()
    query = """ SELECT * FROM student"""
    try:
        cur.execute(query)
        results=cur.fetchall()
        print("records printed")
        for res in results:
            print("Name = ", res[0], )
            print("ID = ", res[1])
            print("Course  = ", res[2])
            print("Section  = ", res[3], "\n")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
    # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")




def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="test")
        
        print('PostgreSQL database version:')
        # cur.execute('SELECT version()')
        # db_version = cur.fetchone()
        # print(db_version)
        # cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    #         print('Database connection closed.')
    return conn

if __name__ == '__main__':
    connect()
    #insert_student_data()
    get_student_data()