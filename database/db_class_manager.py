import database.db_connect_manager as db
from mysql.connector import Error

def delete_class_by_id(id: int) -> None:
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM Classes WHERE class_id = %s",(id,))
    conn.commit()
    cursor.close()
    conn.close()
                        
def update_class_by_id(class_id: int, cn: str, prof_id: int) -> None:
    conn = db.get_connection()
    try:
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT prof_ID FROM Professors WHERE prof_ID = %s", (prof_id,))
        if cursor.fetchone() is None:
            print(f"No professor found with ID {prof_id}.")
            return

        cursor.execute(
            "UPDATE Classes SET class_name = %s, professor_id = %s WHERE class_id = %s",
            (cn, prof_id, class_id)
        )
        if cursor.rowcount == 0:
            print(f"No class found with ID {class_id}.")
        else:
            print("Class updated.")
    except Error as e:
        print(f"Error updating class: {e}")
        conn.rollback()
    finally:
        conn.commit()
        cursor.close()
        conn.close()
        
def view_all_classes() -> None:
    conn = db.get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Classes")
        rows = cursor.fetchall()

        if not rows:
            print("No classes found.")
            return

        for i, row in enumerate(rows, start=1):
            print(f"[{i}] (ID: {row['class_id']}) {row['class_name']} | Professor's ID: {row['professor_id']}")
    except Exception as e:
        print(f"Error fetching classes: {e}")
    finally:
        cursor.close()
        conn.close()

def insert_professor(cn: str, id: int) -> None:
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT prof_ID FROM Professors WHERE prof_ID = %s", (id,))
    if cursor.fetchone() is None:
        print(f"No professor found with ID {id}.")
        return
    
    cursor.execute("INSERT INTO Classes (class_name,professor_id) VALUES (%s, %s)",(cn,id))
    conn.commit()
    cursor.close()
    conn.close()