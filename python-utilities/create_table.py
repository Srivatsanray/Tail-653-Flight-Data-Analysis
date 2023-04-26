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

    cur = conn.cursor()

    # Assign column names according for your database schema

    column_names = ', '.join([f'{column.lower()}' for column in data])

    column_definitions = ', '.join(
        [f'{column.lower()} {datatype}' for column in column_names])  # Assign the datatype required to your project
    create_table_query = f"""
            CREATE TABLE sr_16
            (
                {column_definitions}
            )
        """
    print("Creating table")
    cur.execute(create_table_query)

    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

except:
    print("I am unable to connect to the database")
