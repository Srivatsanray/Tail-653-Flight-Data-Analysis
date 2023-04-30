import connect
from insert import insert
from reader import reader


def main():

    connection = connect.connect()
# cursor object that deals with making changes in our database
    mycursor = connection.cursor()
# Get the column names, data -- contained in freq and the path to the .mat files
    col, freq, path = reader()

    insert(freq, col, path, connection, mycursor)

    # Close the connection
    connection.close()


if __name__ == "__main__":
    main()
