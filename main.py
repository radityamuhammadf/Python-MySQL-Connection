# importing module
import mysql.connector

# initiate connection to mysql server
mydb=mysql.connector.connect(
    host='localhost',
    username='root',
    password=''
)

# print(mydb)

# instantitate cursor class for executing sql command 
cursor = mydb.cursor()

database_name="enpemo"

# query for checking database avalability
check_db_query=f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{database_name}' "
# execute the query
cursor.execute(check_db_query)
# fetch the execution result
result=cursor.fetchone()

# Check if the database exists
if result:
    print(f"The database '{database_name}' already exists.")
else:
    # If the database doesn't exist, you can create it here
    create_database_query = f"CREATE DATABASE {database_name}"
    cursor.execute(create_database_query)
    print(f"The database '{database_name}' has been created.")

# select the 'enpemo' database
cursor.execute(f"USE {database_name}")

counter_table_name="kehadiran"
# SQL query to create the table with auto-increment primary key
create_table_query = f"""
    CREATE TABLE IF NOT EXISTS `{counter_table_name}` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `jumlah` INT NOT NULL,
        `createdAt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `updatedAt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=3;
"""
cursor.execute(create_table_query)
# sql query for checking the table availability
check_table_query=f"SHOW TABLES LIKE '{counter_table_name}'"
# execute the query
cursor.execute(check_table_query)
result=cursor.fetchone()
if result:
    print(f"The table '{counter_table_name}' is exists in the '{database_name}' database.")

# close the cursor and database connection
cursor.close()
mydb.close()