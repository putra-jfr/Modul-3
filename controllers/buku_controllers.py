
import tkinter.messagebox as messagebox

from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        # Inisialisasi Model, View, dan Role
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        self.view.title(
            f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}"
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

        # Binding pemilihan data pada tabel
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        # ==========================================
        # PENGATURAN HAK AKSES
        # ==========================================

        if self.user_role != "admin":

            # Mengunci tombol Simpan
            self.view.btn_simpan.configure(
                state="disabled",
                text="Akses Terkunci (Khusus Admin)"
            )

            # Mengunci tombol Update
            self.view.btn_update.configure(
                state="disabled"
            )

            # Mengunci tombol Hapus
            self.view.btn_hapus.configure(
                state="disabled"
            )

            # Mengunci seluruh input
            self.view.entry_judul.configure(
                state="disabled"
            )

            self.view.entry_penulis.configure(
                state="disabled"
            )

            self.view.entry_tahun.configure(
                state="disabled"
            )

        else:
            self.view.btn_simpan.configure(
                state="normal"
            )

            self.view.btn_update.configure(
                state="normal"
            )

            self.view.btn_hapus.configure(
                state="normal"
            )

        # Memuat data buku
        self.muat_data_tabel()

    # ==========================================
    # MEMUAT DATA KE TABEL
    # ==========================================

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

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
    # MEMILIH DATA DARI TABEL
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

        self.bersihkan_form()

        self.view.entry_judul.insert(
            0, data[1]
        )

        self.view.entry_penulis.insert(
            0, data[2]
        )

        self.view.entry_tahun.insert(
            0, data[3]
        )

    # ==========================================
    # MENAMBAHKAN DATA BUKU (CREATE)
    # ==========================================

    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk menambah data!"
            )
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )

            self.bersihkan_form()
            self.muat_data_tabel()

        else:
            messagebox.showerror(
                "Error",
                "Gagal menyimpan data buku."
            )

    # ==========================================
    # MEMPERBARUI DATA BUKU (UPDATE)
    # ==========================================

    def perbarui_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk memperbarui data!"
            )
            return

        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin diperbarui!"
            )
            return

        data = self.view.tabel.item(
            selected[0],
            "values"
        )

        id_buku = data[0]

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

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
                "Error",
                "Gagal memperbarui data buku."
            )

    # ==========================================
    # MENGHAPUS DATA BUKU (DELETE)
    # ==========================================

    def hapus_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk menghapus data!"
            )
            return

        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin dihapus!"
            )
            return

        data = self.view.tabel.item(
            selected[0],
            "values"
        )

        id_buku = data[0]

        konfirmasi = messagebox.askyesno(
            "Konfirmasi Hapus",
            f"Apakah Anda yakin ingin menghapus buku '{data[1]}'?"
        )

        if konfirmasi:
            if self.model.hapus_buku(id_buku):
                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil dihapus!"
                )

                self.bersihkan_form()
                self.muat_data_tabel()

            else:
                messagebox.showerror(
                    "Error",
                    "Gagal menghapus data buku."
                )

    # ==========================================
    # MEMBERSIHKAN FORM
    # ==========================================

    def bersihkan_form(self):
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

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
            # Menutup jendela BukuView
            self.view.destroy()

            # Membuka kembali halaman LoginView
            from controllers.auth_controller import AuthController

            login_controller = AuthController()
            login_controller.run()

    # ==========================================
    # MENJALANKAN APLIKASI
    # ==========================================

    def run(self):
        self.view.mainloop()
