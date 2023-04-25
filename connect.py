import psycopg2

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

    # a database object that allows us to retrieve each row at a time and manipulate its data
    cur = conn.cursor()

    # With the cursor, we can retrieve/write/read the data by sending query string

    conn.commit()  # commit the changes to the database

    # Close the cursor and connection
    cur.close()
    conn.close()

except:
    print("I am unable to connect to the database")
