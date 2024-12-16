import sqlite3

def initialize_database():
    conn = sqlite3.connect("llmops.db")
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prompts (
            prompt_id INTEGER PRIMARY KEY AUTOINCREMENT,
            version INTEGER,
            content TEXT,
            is_active BOOLEAN DEFAULT 0
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            app_id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt_id INTEGER,
            model_options TEXT,
            FOREIGN KEY (prompt_id) REFERENCES prompts (prompt_id)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datasets (
            dataset_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            data TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            app_id INTEGER,
            dataset_id INTEGER,
            result TEXT,
            FOREIGN KEY (app_id) REFERENCES applications (app_id),
            FOREIGN KEY (dataset_id) REFERENCES datasets (dataset_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prompt_history (
            history_id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt_id INTEGER,
            version INTEGER,
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (prompt_id) REFERENCES prompts (prompt_id)
        )
    """)
    
    conn.commit()
    conn.close()