import psycopg2

# Add your database credentials

def connect():

    print('Connecting to the PostgreSQL database...')
    try:
        # Providing credentials to connect to the database
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("connection successful\n")
        # conn object to connect to database
        return conn

    except:
        print("I am unable to connect to the database")
