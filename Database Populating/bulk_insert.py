from psycopg2.extras import execute_values
import os


def insert(freq, col, path, connection, cursor):

    col.append('DATE')  # Inserting the date (final column)

    # Date extraction
    date = (os.path.split(path)[1])
    date = date[3:7] + '-' + date[7:9]+'-' + date[9:11]

    # automating the sql command to insert data
    column_names = ', '.join(
        [f'{column.lower()}' for column in col])
    column_values = ', '.join(
        ['%s' for column in col])

    # sql command to insert the row. Here we specify which table, column and datatype here.
    sql_com = f"""INSERT INTO bulk_data
              ({column_names})
               VALUES  %s; """

    var = [date] * len(freq[0])

    freq.append(var) # Appending date into our 2d array

    # Transpose of the 2d array
    freq = list(zip(*freq))
    # this is to identify the paritcular row index to
    # insert
    # Executing the sql command
    # match the string to reference the data in the list
    column_values = f"({column_values})::bulk_data"
    try:
        execute_values(cursor, sql_com, freq, template=None)
        connection.commit()  # Update the progress bar
    except Exception as e:
        print(f"Error inserting row: {e}")
        connection.rollback()  # close the connection
    # We finally break out of the loop to debug
