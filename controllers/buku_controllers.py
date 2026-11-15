
import tkinter.messagebox as messagebox

from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:

    def __init__(self, user_role="anggota"):

        self.user_role = user_role.lower()

        self.model = BukuModel()
        self.view = BukuView()

        self.view.title(
            f"Sistem Manajemen Perpustakaan - "
            f"Mode: {self.user_role.upper()}"
        )

        # ==========================================
        # BINDING TOMBOL
        # ==========================================

        self.view.btn_simpan.configure(
            command=self.simpan_data
        )

        self.view.btn_update.configure(
            command=self.perbarui_data
        )

        self.view.btn_hapus.configure(
            command=self.hapus_data
        )

        self.view.btn_logout.configure(
            command=self.logout
        )

        # Event pemilihan data pada tabel
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        # ==========================================
        # HAK AKSES ADMIN DAN ANGGOTA
        # ==========================================

        if self.user_role != "admin":

            self.view.btn_simpan.configure(
                state="disabled",
                text="Khusus Admin"
            )

            self.view.btn_update.configure(
                state="disabled"
            )

            self.view.btn_hapus.configure(
                state="disabled"
            )

            self.view.entry_judul.configure(
                state="disabled"
            )

            self.view.entry_penulis.configure(
                state="disabled"
            )

            self.view.entry_tahun.configure(
                state="disabled"
            )

        # Memuat data buku
        self.muat_data_tabel()

    # ==========================================
    # MEMUAT DATA BUKU
    # ==========================================

    def muat_data_tabel(self):

        # Menghapus isi tabel sebelumnya
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari database
        data_buku = self.model.get_all_buku()

        # Memasukkan data ke tabel
        for buku in data_buku:

            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    # ==========================================
    # MEMILIH DATA BUKU
    # ==========================================

    def pilih_data(self, event=None):

        if self.user_role != "admin":
            return

        selected = self.view.tabel.selection()

        if not selected:
            return

        data = self.view.tabel.item(
            selected[0],
            "values"
        )

        # Membersihkan input tanpa menghapus seleksi tabel
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

        # Memasukkan data buku ke formulir
        self.view.entry_judul.insert(0, data[1])
        self.view.entry_penulis.insert(0, data[2])
        self.view.entry_tahun.insert(0, data[3])

    # ==========================================
    # MENYIMPAN DATA BUKU (CREATE)
    # ==========================================

    def simpan_data(self):

        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin!"
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        # Validasi input kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!"
            )
            return

        # Validasi tahun
        try:
            int(tahun)
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!"
            )
            return

        # Menyimpan data
        if self.model.create_buku(
            judul,
            penulis,
            tahun
        ):

            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )

            self.bersihkan_form()
            self.muat_data_tabel()

        else:
            messagebox.showerror(
                "Gagal Menyimpan",
                self.model.last_error or
                "Gagal menyimpan data buku!"
            )

    # ==========================================
    # MEMPERBARUI DATA BUKU (UPDATE)
    # ==========================================

    def perbarui_data(self):

        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin!"
            )
            return

        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin diperbarui!"
            )
            return

        # Mengambil ID buku yang dipilih
        data = self.view.tabel.item(
            selected[0],
            "values"
        )

        id_buku = data[0]

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        # Validasi input
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!"
            )
            return

        try:
            int(tahun)
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!"
            )
            return

        # Memperbarui data
        if self.model.update_buku(
            id_buku,
            judul,
            penulis,
            tahun
        ):

            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!"
            )

            self.bersihkan_form()
            self.muat_data_tabel()

        else:
            messagebox.showerror(
                "Gagal Memperbarui",
                self.model.last_error or
                "Gagal memperbarui data buku!"
            )

    # ==========================================
    # MENGHAPUS DATA BUKU (DELETE)
    # ==========================================

    def hapus_data(self):

        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin!"
            )
            return

        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin dihapus!"
            )
            return

        # Mengambil data buku yang dipilih
        data = self.view.tabel.item(
            selected[0],
            "values"
        )

        id_buku = data[0]
        judul_buku = data[1]

        # Konfirmasi penghapusan
        konfirmasi = messagebox.askyesno(
            "Konfirmasi Hapus",
            f"Apakah Anda yakin ingin menghapus "
            f"buku '{judul_buku}'?"
        )

        if not konfirmasi:
            return

        # Menghapus data dari database
        if self.model.delete_buku(id_buku):

            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil dihapus!"
            )

            self.bersihkan_form()
            self.muat_data_tabel()

        else:
            # Menampilkan penyebab kegagalan dari Model
            messagebox.showwarning(
                "Penghapusan Ditolak",
                self.model.last_error or
                "Gagal menghapus data buku!"
            )

    # ==========================================
    # MEMBERSIHKAN FORM DAN PILIHAN TABEL
    # ==========================================

    def bersihkan_form(self):

        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

        # Menghilangkan pilihan pada tabel
        for item in self.view.tabel.selection():
            self.view.tabel.selection_remove(item)

    # ==========================================
    # LOGOUT / KEMBALI KE LOGIN
    # ==========================================

    def logout(self):

        konfirmasi = messagebox.askyesno(
            "Konfirmasi Logout",
            "Apakah Anda yakin ingin keluar dari sistem?"
        )

        if konfirmasi:

            # Menutup halaman buku
            self.view.destroy()

            # Membuka halaman login kembali
            from controllers.auth_controller import AuthController

            login_controller = AuthController()
            login_controller.run()

    # ==========================================
    # MENJALANKAN APLIKASI
    # ==========================================

    def run(self):

        self.view.mainloop()
