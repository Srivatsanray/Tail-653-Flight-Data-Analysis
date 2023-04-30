from execute import execute
import os
from tqdm import tqdm


def insert(freq, col, path, connection, cursor):

    col.append('DATE')  # Inserting the date (final column)

    # Date extraction from the .mat file name
    date = (os.path.split(path)[1])
    date = date[3:7] + '-' + date[7:9]+'-' + date[9:11] # Refer the .mat file name and change accordingly

    print(f"\nInserting data in {os.path.split(path)[1]}")

    # automating the sql command to insert data
    column_names = ', '.join(
        [f'{column.lower()}' for column in col])
    column_values = ', '.join(
        ['%s' for column in col])

    # sql command to insert the row. Here we specify which table, column and datatype here.
    sql_com = f"""INSERT INTO avi_data
              ({column_names})
               VALUES ({column_values}); """

    no_of_lines = len(freq[0])  # no of rows

    # Progress Bar
    with tqdm(total=no_of_lines, desc="Uploading", ascii=' █', initial=0, colour='green') as pbar:
        # Looping through the rows, reading and inserting into the database
        for row in range(no_of_lines):
            # this is to identify the paritcular row index to insert
            row_values = ', '.join(
                [f'freq[{i}][{row}]' for i in range(len(freq))])

            # Adding date to row_values
            row_values = row_values + ', ' + 'date'

            try:
                # Executing the sql command
                # match the string to reference the data in the list
                values = eval(row_values)
                execute(sql_com, values, cursor)

                # Commit the changes to the server
                connection.commit()
                pbar.update(1)  # Update the progress bar
            except Exception as e:
                # clse the progress bar
                pbar.close()
                
                # For handling exceptions, we print the error message
                print(f"Error inserting row: {e}")

                connection.rollback()  # close the connection
                # We finally break out of the loop to debug
                break

        pbar.close()
