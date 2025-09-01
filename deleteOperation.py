import sqlite3



def delete_specificUser(userid):

    conn = sqlite3.connect("my_shop.db")
    cursor = conn.cursor()


    cursor.execute("DELETE FROM Users WHERE user_id = ?", (userid,))


    conn.commit()
    conn.close()