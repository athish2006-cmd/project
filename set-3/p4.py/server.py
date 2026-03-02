import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def init_db():
    """
    Initializes the database with a table and some dummy data.
    Run this once to set up the environment.
    """
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    
    # 1. Create a table named 'students'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            branch TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    ''')
    
    # 2. Check if table is empty, if so, add dummy data
    cursor.execute('SELECT count(*) FROM students')
    if cursor.fetchone()[0] == 0:
        students_data = [
            ('Alice Johnson', 'CSE', 2),
            ('Bob Smith', 'Mechanical', 3),
            ('Charlie Brown', 'Civil', 1),
            ('David Lee', 'CSE', 4)
        ]
        cursor.executemany('INSERT INTO students (name, branch, year) VALUES (?, ?, ?)', students_data)
        conn.commit()
        print("Database initialized with dummy data.")
    
    conn.close()

# Initialize database when the script starts
init_db()

@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect('college.db')
    # Use Row factory to access columns by name (optional but good practice)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Fetch all records
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    
    conn.close()
    
    # Pass the data (rows) to the HTML template
    return render_template('index.html', students=rows)

if __name__ == '__main__':
    app.run(debug=True)