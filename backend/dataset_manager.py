import sqlite3

def create_dataset(name, data):
    conn = sqlite3.connect("llmops.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO datasets (name, data)
        VALUES (?, ?)
    """, (name, data))
    conn.commit()
    conn.close()

def get_dataset(dataset_id):
    conn = sqlite3.connect("llmops.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datasets WHERE dataset_id = ?", (dataset_id,))
    dataset = cursor.fetchone()
    conn.close()
    return dataset