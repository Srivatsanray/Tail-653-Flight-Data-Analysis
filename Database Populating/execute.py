'''
   Execute the sql command
'''


def execute(sql, arrayList, cursor):
    # Executing the sql command
    cursor.execute(sql, arrayList)
    # Commit the changes to the server
