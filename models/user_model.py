
import hashlib
from config.database import Database


class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = None

    # Mengubah password menjadi hash SHA-256
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(
            password.encode("utf-8")
        ).hexdigest()

    # Mengambil koneksi database
    def get_connection(self):
        if self.conn is not None:
            return self.conn, False

        return self.db.get_connection(), True

    # Proses autentikasi pengguna
    def authenticate(self, username, password):
        conn, owned = self.get_connection()

        if conn is None:
            return None

        cursor = None

        try:
            cursor = conn.cursor(dictionary=True)

            password_hash = self.hash_password(password)

            query = """
                SELECT id_user, username, role
                FROM users
                WHERE username = %s AND password = %s
            """

            cursor.execute(query, (username, password_hash))

            return cursor.fetchone()

        except Exception as e:
            print("Error autentikasi:", e)
            return None

        finally:
            if cursor:
                cursor.close()

            if owned:
                conn.close()

    # Registrasi pengguna baru
    def register_user(self, username, password, role="anggota"):
        if not username or not password:
            return False

        if role not in ("admin", "anggota"):
            return False

        conn, owned = self.get_connection()

        if conn is None:
            return False

        cursor = None

        try:
            cursor = conn.cursor()

            query = """
                INSERT INTO users (username, password, role)
                VALUES (%s, %s, %s)
            """

            cursor.execute(
                query,
                (username, self.hash_password(password), role)
            )

            conn.commit()
            return True

        except Exception as e:
            print("Error registrasi:", e)
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()

            if owned:
                conn.close()
