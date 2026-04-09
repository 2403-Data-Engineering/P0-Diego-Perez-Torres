import database.db_connect_manager as db
from mysql.connector import Error

def delete_student_by_id(id: int) -> None:
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM Students WHERE student_id = %s",(id,))
    conn.commit()
    cursor.close()
    conn.close()
                        
def update_student_by_id(fn: str, ln:str, major: str, year: int, id: int) -> None:
    conn = db.get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "UPDATE Students SET first_name = %s, last_name = %s, major = %s, year = %s WHERE student_id = %s",
            (fn, ln, major, year, id)
        )
        if cursor.rowcount == 0:
            print(f"No student found with ID {id}.")
        else:
            print("student updated.")
    except Error as e:
        print(f"Error updating student: {e}")
        conn.rollback()
    finally:
        conn.commit()
        cursor.close()
        conn.close()
        
def view_all_students() -> None:
    conn = db.get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Students")
        rows = cursor.fetchall()

        if not rows:
            print("No students found.")
            return

        for i, row in enumerate(rows, start=1):
            print(f"[{i}] (ID: {row['student_ID']}) {row['first_name']} {row['last_name']} | {row['major']} | {row['email']} | {row['year']}")
    except Exception as e:
        print(f"Error fetching Students: {e}")
    finally:
        cursor.close()
        conn.close()

def insert_student(fn: str, ln:str, major:str, email:str, year: int) -> None:
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("INSERT INTO Students (first_name,last_name,major,email,year) VALUES (%s, %s, %s, %s, %s)",(fn,ln,major,email,year))
    conn.commit()
    cursor.close()
    conn.close()