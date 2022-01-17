from sql_connection import get_sql_connection

connection = get_sql_connection()

def check(connection):
    a=False
    cursor = connection.cursor()
    an = input("Are you the admin or not? ")
    if an.lower() == "yes":
        query = ("Select * from owner ;")
        cursor.execute(query)
        response = []

        for (uq,pq) in cursor:
            response.append(uq)
            response.append(pq)
        ue = input("Enter username : ")
        pe = input("Enter password : ")
        if ue==response[0] and pe==response[1]:
            a=True
    else :
        a=False
    print(a)
    return a

check(connection)
        

