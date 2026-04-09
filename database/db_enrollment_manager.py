import database.db_connect_manager as db
from mysql.connector import Error

def view_enrolled_classes(student_id: int) -> None:
    conn = db.get_connection()
    try:
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT student_id FROM Students WHERE student_id = %s", (student_id,))
        if cursor.fetchone() is None:
            print(f"No student found with ID {student_id}.")
            return

        cursor.execute("""
            SELECT c.class_id, c.class_name, c.professor_id
            FROM Classes c
            JOIN Classes_Students cs ON c.class_id = cs.class_id
            WHERE cs.student_id = %s
        """, (student_id,))

        rows = cursor.fetchall()

        if not rows:
            print(f"No students enrolled in class {student_id}.")
            return

        for i, row in enumerate(rows, start=1):
            print(f"[{i}] (ID: {row['class_id']}) {row['class_name']} | (Professor ID: {row['professor_id']})")
    except Exception as e:
        print(f"Error fetching students: {e}")
    finally:
        cursor.close()
        conn.close()
                        
def view_students_in_a_class(class_id: int) -> None:
    conn = db.get_connection()
    try:
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT class_id FROM Classes WHERE class_id = %s", (class_id,))
        if cursor.fetchone() is None:
            print(f"No class found with ID {class_id}.")
            return

        cursor.execute("""
            SELECT s.student_id, s.first_name, s.last_name, s.email, s.major, s.year
            FROM Students s
            JOIN Classes_Students cs ON s.student_id = cs.student_id
            WHERE cs.class_id = %s
        """, (class_id,))

        rows = cursor.fetchall()

        if not rows:
            print(f"No students enrolled in class {class_id}.")
            return

        for i, row in enumerate(rows, start=1):
            print(f"[{i}] (ID: {row['student_id']}) {row['first_name']} {row['last_name']} | {row['major']} | {row['email']}")
    except Exception as e:
        print(f"Error fetching students: {e}")
    finally:
        cursor.close()
        conn.close()
        
def drop_student_from_a_class(class_id: int, student_id: int) -> None:
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT class_id FROM Classes WHERE class_id = %s", (class_id,))
    if cursor.fetchone() is None:
        print(f"No class found with ID {class_id}.")
        return
    
    cursor.execute("SELECT student_id FROM Students WHERE student_id = %s", (student_id,))
    if cursor.fetchone() is None:
        print(f"No student found with ID {student_id}.")
        return
    
    cursor.execute("DELETE FROM Classes_Students WHERE class_id = %s AND student_id = %s",(class_id,student_id))
    conn.commit()
    cursor.close()
    conn.close()

def enroll_student_to_class(class_id: int, student_id: int) -> None:
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT class_id FROM Classes WHERE class_id = %s", (class_id,))
    if cursor.fetchone() is None:
        print(f"No class found with ID {class_id}.")
        return
    
    cursor.execute("SELECT student_id FROM Students WHERE student_id = %s", (student_id,))
    if cursor.fetchone() is None:
        print(f"No student found with ID {student_id}.")
        return
    
    cursor.execute("INSERT INTO Classes_Students (class_id,student_id) VALUES (%s, %s)",(class_id,student_id))
    conn.commit()
    cursor.close()
    conn.close()