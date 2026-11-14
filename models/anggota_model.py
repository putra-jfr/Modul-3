from config.database import Database


class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    # ==========================================
    # 1. MENAMBAHKAN DATA ANGGOTA
    # ==========================================
    def create_anggota(self, nama, alamat):
        if self.conn:
            cursor = self.conn.cursor()

            query = f"""
                INSERT INTO {self.table_name} (nama, alamat)
                VALUES (%s, %s)
            """

            val = (nama, alamat)

            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()

            return True
        return False

    # ==========================================
    # 2. MENAMPILKAN SEMUA DATA ANGGOTA
    # ==========================================
    def get_all_anggota(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)

            query = f"SELECT * FROM {self.table_name}"

            cursor.execute(query)
            result = cursor.fetchall()

            cursor.close()

            return result
        return []

    # ==========================================
    # 3. MEMPERBARUI DATA ANGGOTA
    # ==========================================
    def update_anggota(self, id_anggota, nama, alamat):
        if self.conn:
            cursor = self.conn.cursor()

            query = f"""
                UPDATE {self.table_name}
                SET nama = %s, alamat = %s
                WHERE id_anggota = %s
            """

            val = (nama, alamat, id_anggota)

            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()

            return True
        return False

    # ==========================================
    # 4. MENGHAPUS DATA ANGGOTA
    # ==========================================
    def delete_anggota(self, id_anggota):
        if self.conn:
            cursor = self.conn.cursor()

            query = f"""
                DELETE FROM {self.table_name}
                WHERE id_anggota = %s
            """

            val = (id_anggota,)

            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()

            return True
        return False