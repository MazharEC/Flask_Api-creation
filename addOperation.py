import sqlite3
import uuid
from datetime import date


def create_user(
        name, password, address, email, phone_number, pin_code
):
    conn = sqlite3.connect("my_shop.db")
    cursor = conn.cursor()

    dateOfCreation = date.today()
    user_id = str(uuid.uuid4())

    cursor.execute('''

    INSERT INTO Users (user_id, name, password, date_of_creation, isApproved, blocked, address, email, pin_code, phone_number)
                   
                   VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

                    ''', (user_id, name, password, dateOfCreation, 0, 0, address, email, pin_code, phone_number)
                    
                    )
    conn.commit()
    conn.close()

    return user_id