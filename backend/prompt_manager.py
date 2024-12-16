import sqlite3

def create_prompt(content, version):
    conn = sqlite3.connect("llmops.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO prompts (content, version, is_active)
        VALUES (?, ?, ?)
    """, (content, version, 0))
    prompt_id = cursor.lastrowid
    cursor.execute("""
        INSERT INTO prompt_history (prompt_id, version, content)
        VALUES (?, ?, ?)
    """, (prompt_id, version, content))
    conn.commit()
    conn.close()

def set_active_prompt(prompt_id):
    conn = sqlite3.connect("llmops.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE prompts SET is_active = 0")
    cursor.execute("UPDATE prompts SET is_active = 1 WHERE prompt_id = ?", (prompt_id,))
    conn.commit()
    conn.close()

def get_prompt_history(prompt_id):
    conn = sqlite3.connect("llmops.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prompt_history WHERE prompt_id = ?", (prompt_id,))
    history = cursor.fetchall()
    conn.close()
    return history
