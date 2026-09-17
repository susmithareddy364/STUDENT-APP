from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)


# Connect to database
def get_db_connection():
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    return connection


# Create database table
def create_table():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# POST API - Save student
@app.route("/api/students", methods=["POST"])
def add_student():

    data = request.get_json()

    name = data["name"]
    email = data["email"]
    age = data["age"]
    course = data["course"]

    connection = get_db_connection()

    connection.execute("""
        INSERT INTO students (name, email, age, course)
        VALUES (?, ?, ?, ?)
    """, (name, email, age, course))

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Student saved successfully"
    }), 201


# GET API - Get students
@app.route("/api/students", methods=["GET"])
def get_students():

    connection = get_db_connection()

    students = connection.execute(
        "SELECT * FROM students"
    ).fetchall()

    connection.close()

    student_list = []

    for student in students:
        student_list.append({
            "id": student["id"],
            "name": student["name"],
            "email": student["email"],
            "age": student["age"],
            "course": student["course"]
        })

    return jsonify(student_list)


if __name__ == "__main__":
    create_table()
    app.run(debug=True)