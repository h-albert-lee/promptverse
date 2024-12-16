import sqlite3

def create_application(prompt_id, model_options):
    conn = sqlite3.connect("llmops.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO applications (prompt_id, model_options)
        VALUES (?, ?)
    """, (prompt_id, model_options))
    conn.commit()
    conn.close()

def get_application(app_id):
    conn = sqlite3.connect("llmops.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM applications WHERE app_id = ?", (app_id,))
    app = cursor.fetchone()
    conn.close()
    return app