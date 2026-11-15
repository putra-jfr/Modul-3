
import mysql.connector
from config.database import Database


class BukuModel:

    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"
        self.last_error = None

    # ==========================================
    # MENAMPILKAN SEMUA DATA BUKU (READ)
    # ==========================================

    def get_all_buku(self):

        if not self.conn:
            self.last_error = "Koneksi database tidak tersedia."
            return []

        cursor = None

        try:
            cursor = self.conn.cursor(dictionary=True)

            query = "SELECT * FROM buku ORDER BY id_buku ASC"
            cursor.execute(query)

            self.last_error = None
            return cursor.fetchall()

        except mysql.connector.Error as e:
            self.last_error = str(e)
            return []

        finally:
            if cursor:
                cursor.close()

    # ==========================================
    # MENAMBAHKAN DATA BUKU (CREATE)
    # ==========================================

    def create_buku(self, judul, penulis, tahun_terbit):

        if not self.conn:
            self.last_error = "Koneksi database tidak tersedia."
            return False

        cursor = None

        try:
            cursor = self.conn.cursor()

            query = """
                INSERT INTO buku
                (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
            """

            val = (judul, penulis, tahun_terbit)

            cursor.execute(query, val)
            self.conn.commit()

            self.last_error = None
            return True

        except mysql.connector.Error as e:
            self.conn.rollback()
            self.last_error = str(e)
            return False

        finally:
            if cursor:
                cursor.close()

    # ==========================================
    # MEMPERBARUI DATA BUKU (UPDATE)
    # ==========================================

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):

        if not self.conn:
            self.last_error = "Koneksi database tidak tersedia."
            return False

        cursor = None

        try:
            cursor = self.conn.cursor()

            query = """
                UPDATE buku
                SET judul = %s,
                    penulis = %s,
                    tahun_terbit = %s
                WHERE id_buku = %s
            """

            val = (judul, penulis, tahun_terbit, id_buku)

            cursor.execute(query, val)
            self.conn.commit()

            self.last_error = None
            return True

        except mysql.connector.Error as e:
            self.conn.rollback()
            self.last_error = str(e)
            return False

        finally:
            if cursor:
                cursor.close()

    # ==========================================
    # MENGHAPUS DATA BUKU (DELETE)
    # ==========================================

    def delete_buku(self, id_buku):

        if not self.conn:
            self.last_error = "Koneksi database tidak tersedia."
            return False

        cursor = None

        try:
            cursor = self.conn.cursor()

            query = """
                DELETE FROM buku
                WHERE id_buku = %s
            """

            cursor.execute(query, (id_buku,))

            if cursor.rowcount == 0:
                self.last_error = "Data buku tidak ditemukan."
                self.conn.rollback()
                return False

            self.conn.commit()

            self.last_error = None
            return True

        except mysql.connector.IntegrityError:
            self.conn.rollback()

            self.last_error = (
                "Buku tidak dapat dihapus karena masih memiliki "
                "riwayat peminjaman. Periksa transaksi peminjaman "
                "terlebih dahulu."
            )

            return False

        except mysql.connector.Error as e:
            self.conn.rollback()

            self.last_error = (
                f"Terjadi kesalahan database: {e}"
            )

            return False

        finally:
            if cursor:
                cursor.close()
