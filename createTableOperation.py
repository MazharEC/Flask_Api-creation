import sqlite3




def createTables():
    conn = sqlite3.connect("my_shop.db")
    cursor = conn.cursor()

    cursor.execute('''

            CREATE TABLE IF NOT EXISTS Users(

                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(255),
                password VARCHAR(255),
                date_of_creation  DATE,
                isApproved BOOLEAN,
                blocked BOOLEAN,
                name VARCHAR(255),
                address VARCHAR(255),
                email VARCHAR(255),
                phone_number VARCHAR(255),
                pin_code VARCHAR(255)


            )

        ''')
    

    cursor.execute('''

        CREATE TABLE IF NOT EXISTS Sell_History(
                   
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   sell_id VARCHAR(255),
                   product_id VARCHAR(255),
                   quantity INT,
                   remaining_stock INT,
                   date_of_sell DATE,
                   price FLOAT,
                   product_name VARCHAR(255),
                   user_id VARCHAR(255)
                   )

''')
    

    
    cursor.execute('''

        CREATE TABLE IF NOT EXISTS User_Stock(
                   
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product_id VARCHAR(255),
                   product_name VARCHAR(255),
                   stock INT,
                   price FLOAT,
                   product_name VARCHAR(255),
                   user_id VARCHAR(255),
                   user_name VARCHAR(255)
                   )

''')

    
    conn.commit()
    conn.close()