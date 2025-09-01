import sqlite3


def approve_user(userID, isApproved):
    conn = sqlite3.connect("my_shop.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Users SET isApproved =? WHERE user_id =?", (isApproved,userID))

    conn.commit()
    conn.close()

    