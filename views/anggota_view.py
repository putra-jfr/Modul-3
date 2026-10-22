import customtkinter as ctk
from tkinter import ttk, messagebox


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Anggota Perpustakaan")
        self.geometry("800x450")

        # ==================================================
        # KONFIGURASI GRID UTAMA
        # ==================================================

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # ==================================================
        # FRAME KIRI: FORM DATA ANGGOTA
        # ==================================================

        self.frame_kiri = ctk.CTkFrame(self)

        self.frame_kiri.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Anggota",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # ==================================================
        # INPUT NAMA ANGGOTA
        # ==================================================

        self.entry_nama = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Anggota"
        )

        self.entry_nama.pack(
            pady=10,
            padx=15,
            fill="x"
        )

        # ==================================================
        # INPUT ALAMAT
        # ==================================================

        self.entry_alamat = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Alamat Anggota"
        )

        self.entry_alamat.pack(
            pady=10,
            padx=15,
            fill="x"
        )

        # ==================================================
        # TOMBOL SIMPAN
        # ==================================================

        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green",
            command=self.simpan_data
        )

        self.btn_simpan.pack(
            pady=10,
            padx=15,
            fill="x"
        )

        # ==================================================
        # TOMBOL UPDATE
        # ==================================================

        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data (Update)",
            fg_color="blue",
            command=self.update_data
        )

        self.btn_update.pack(
            pady=5,
            padx=15,
            fill="x"
        )

        # ==================================================
        # TOMBOL DELETE
        # ==================================================

        self.btn_delete = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data (Delete)",
            fg_color="red",
            command=self.delete_data
        )

        self.btn_delete.pack(
            pady=5,
            padx=15,
            fill="x"
        )

        # ==================================================
        # FRAME KANAN: TABEL ANGGOTA
        # ==================================================

        self.frame_kanan = ctk.CTkFrame(self)

        self.frame_kanan.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Anggota Perpustakaan",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # ==================================================
        # TABEL ANGGOTA
        # ==================================================

        kolom = (
            "id",
            "nama",
            "alamat"
        )

        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings",
            height=15
        )

        # ==================================================
        # HEADER TABEL
        # ==================================================

        self.tabel.heading(
            "id",
            text="ID"
        )

        self.tabel.heading(
            "nama",
            text="Nama Anggota"
        )

        self.tabel.heading(
            "alamat",
            text="Alamat"
        )

        # ==================================================
        # LEBAR KOLOM
        # ==================================================

        self.tabel.column(
            "id",
            width=50,
            anchor="center"
        )

        self.tabel.column(
            "nama",
            width=180
        )

        self.tabel.column(
            "alamat",
            width=250
        )

        self.tabel.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # Klik data pada tabel
        self.tabel.bind(
            "<ButtonRelease-1>",
            self.pilih_data
        )

    # ==================================================
    # FUNGSI SIMPAN DATA
    # ==================================================

    def simpan_data(self):

        nama = self.entry_nama.get()
        alamat = self.entry_alamat.get()

        # Memeriksa input
        if nama == "" or alamat == "":
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat harus diisi!"
            )
            return

        # Membuat ID otomatis
        id_anggota = len(self.tabel.get_children()) + 1

        # Memasukkan data ke tabel
        self.tabel.insert(
            "",
            "end",
            values=(
                id_anggota,
                nama,
                alamat
            )
        )

        # Mengosongkan input
        self.entry_nama.delete(0, "end")
        self.entry_alamat.delete(0, "end")

        messagebox.showinfo(
            "Berhasil",
            "Data anggota berhasil disimpan!"
        )

    # ==================================================
    # FUNGSI PILIH DATA
    # ==================================================

    def pilih_data(self, event):

        selected = self.tabel.selection()

        if not selected:
            return

        data = self.tabel.item(selected[0])

        nilai = data["values"]

        if nilai:
            self.entry_nama.delete(0, "end")
            self.entry_nama.insert(0, nilai[1])

            self.entry_alamat.delete(0, "end")
            self.entry_alamat.insert(0, nilai[2])

    # ==================================================
    # FUNGSI UPDATE DATA
    # ==================================================

    def update_data(self):

        selected = self.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data yang ingin diperbarui!"
            )
            return

        nama = self.entry_nama.get()
        alamat = self.entry_alamat.get()

        if nama == "" or alamat == "":
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat harus diisi!"
            )
            return

        self.tabel.item(
            selected[0],
            values=(
                self.tabel.item(selected[0])["values"][0],
                nama,
                alamat
            )
        )

        messagebox.showinfo(
            "Berhasil",
            "Data anggota berhasil diperbarui!"
        )

    # ==================================================
    # FUNGSI DELETE DATA
    # ==================================================

    def delete_data(self):

        selected = self.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data yang ingin dihapus!"
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data ini?"
        )

        if konfirmasi:
            self.tabel.delete(selected[0])

            self.entry_nama.delete(0, "end")
            self.entry_alamat.delete(0, "end")

            messagebox.showinfo(
                "Berhasil",
                "Data anggota berhasil dihapus!"
            )


# ==================================================
# MENJALANKAN PROGRAM
# ==================================================

if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()