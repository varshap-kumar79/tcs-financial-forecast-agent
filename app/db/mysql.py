import json
import os

try:
    import mysql.connector
except Exception:
    mysql = None


MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DB", "tcs_ai"),
}


def log_request_response(endpoint: str, request_payload: dict, response_payload: dict):
    if mysql is None:
        print("⚠️ MySQL module not available. Skipping DB logging.")
        return

    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS forecast_logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                endpoint VARCHAR(255),
                request_payload JSON,
                response_payload JSON,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            INSERT INTO forecast_logs (endpoint, request_payload, response_payload)
            VALUES (%s, %s, %s)
        """, (
            endpoint,
            json.dumps(request_payload),
            json.dumps(response_payload)
        ))

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print("⚠️ MySQL logging skipped:", str(e))
