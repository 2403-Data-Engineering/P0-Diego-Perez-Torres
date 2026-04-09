import database.db_connect_manager as db
from mysql.connector import Error

def delete_student_by_id(id: int) -> None:
    conn = db.get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT student_id FROM Student WHERE student_ID = %s", (id,))
        if cursor.fetchone() is None:
            print(f"No student found with ID {id}.")
            return

        cursor.execute("SELECT class_id FROM Classes_Students WHERE student_id = %s", (id,))
        assigned_students = cursor.fetchall()
        if assigned_students:
            print(f"Cannot delete — student is enrolled to {len(assigned_students)} class(es):")
            for c in assigned_students:
                print(f"  - Class ID: {c['class_id']}")
            print("Please unenrolled from those classes first.")
            return

        cursor.execute("DELETE FROM Students WHERE student_id = %s", (id,))
        print("Student deleted.")
    except Exception as e:
        print(f"Error deleting student: {e}")
        conn.rollback()
    finally:
        conn.commit()
        cursor.close()
        conn.close()
                        
def update_student_by_id(fn: str, ln:str, major: str,email:str, year: int, id: int) -> None:
    conn = db.get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "UPDATE Students SET first_name = %s, last_name = %s, major = %s,email = %s, year = %s WHERE student_id = %s",
            (fn, ln, major,email, year, id)
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
            print(f"[{i}] (ID: {row['student_id']}) {row['first_name']} {row['last_name']} | {row['major']} | {row['email']} | {row['year']}")
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