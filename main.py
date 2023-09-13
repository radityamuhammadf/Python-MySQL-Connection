import mysql.connector

def checkDatabaseExistance(database_name, cursor):
    check_db_query = f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{database_name}' "
    cursor.execute(check_db_query)
    result = cursor.fetchone()
    return result is not None

def createDatabase(database_name, cursor):
    create_database_query = f"CREATE DATABASE {database_name}"
    cursor.execute(create_database_query)
    print(f"The database '{database_name}' has been created.")

def createTableIfNotExist(table_name, cursor):
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS `{table_name}` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `jumlah` INT NOT NULL,
            `createdAt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `updatedAt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=3;
    """
    cursor.execute(create_table_query)

def checkTableExistence(table_name, cursor):
    check_table_query = f"SHOW TABLES LIKE '{table_name}'"
    cursor.execute(check_table_query)
    result = cursor.fetchone()
    return result is not None

def main():
    # Initiate connection to MySQL server
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )

    # Instantiate cursor class for executing SQL commands
    cursor = mydb.cursor()

    database_name = "enpemo"
    counter_table_name = "kehadiran"

    if checkDatabaseExistance(database_name, cursor):
        print(f"The database '{database_name}' already exists.")
    else:
        createDatabase(database_name, cursor)

    # Select the 'enpemo' database
    cursor.execute(f"USE {database_name}")

    if checkTableExistence(counter_table_name, cursor):
        print(f"The table '{counter_table_name}' exists in the '{database_name}' database.")
    else:
        createTableIfNotExist(counter_table_name, cursor)

    # Close the cursor and database connection
    cursor.close()
    mydb.close()

if __name__ == "__main__":
    main()
