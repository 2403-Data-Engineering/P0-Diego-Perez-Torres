import database.db_connect_manager as db
from mysql.connector import Error
  
  
def delete_professor_by_id(id: int) -> None:
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM Professors WHERE prof_ID = %s",(id,))
    conn.commit()
    cursor.close()
    conn.close()
                        
def update_professor_by_id(id: int,fn: str,ln: str, dpt:str, em:str) -> None:
    conn = db.get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE Professors SET first_name = %s , last_name = %s, department = %s, email = %s WHERE prof_ID = %s", (fn,ln,dpt,em,id))
        if cursor.rowcount == 0:
            print(f"No professor found with ID {id}.")
        else:
            print("Professor updated.")
    except Error as e:
        print(f"Error fetching professor: {e}")
    finally:
        conn.commit()
        cursor.close()
        conn.close()
        
def view_all_professors() -> None:
    conn = db.get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Professors")
        rows = cursor.fetchall()

        if not rows:
            print("No professors found.")
            return

        for i, row in enumerate(rows, start=1):
            print(f"[{i}] (ID: {row['prof_ID']}) {row['first_name']} {row['last_name']} | {row['department']} | {row['email']}")
    except Exception as e:
        print(f"Error fetching professors: {e}")
    finally:
        cursor.close()
        conn.close()

def insert_professor(fn: str,ln: str, dpt:str, em:str) -> None:
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("INSERT INTO Professors (first_name, last_name, department, email) VALUES (%s, %s, %s, %s)",(fn, ln, dpt, em))
    conn.commit()
    cursor.close()
    conn.close()