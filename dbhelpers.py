import mariadb
import dbcreds

def connect_db():
    try: 
        conn=mariadb.connect(
        host =dbcreds.host,
        port=dbcreds.port,
        user=dbcreds.user,
        password=dbcreds.password,
        database=dbcreds.database,
        autocommit=True 
        )
        cursor = conn.cursor()
        return cursor
    except mariadb.Operationalerror as e:
        print("Could not connect to the database",e)
    except Exception as e:
        print("Something went very wrong:",e)


def execute_statement(cursor, statement, args=[]):
    try:
        cursor.execute(statement, args)
        result = cursor.fetchall()
        return result
    except mariadb.IntegrityError as e:
        if "exploits_FK" in e.msg:
            print("The user ID is not valid:")
        else:
            print("Data was not valid:",e)
    except mariadb.ProgrammingError as e:
        if "doesn't have a result set" in e.msg:
            return
        else:
            print("You suck. Get back to the docs. Check SQL", e)
    except mariadb.OperationalError as e:
        print("Something went wrong with the connection to the DB")
    except Exception as e:
        print("Something went wrong:", e)



def close_connection(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close
    except Exception:
        print("Something went wrong with closing the connection")