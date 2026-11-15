
import customtkinter as ctk
from tkinter import ttk


class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("800x500")

        # Konfigurasi Grid Utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # FRAME KIRI: FORM DATA BUKU
        # ==========================================

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
            text="Form Data Buku",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Input Judul
        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Judul Buku"
        )
        self.entry_judul.pack(
            pady=10,
            padx=15,
            fill="x"
        )

        # Input Penulis
        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Penulis"
        )
        self.entry_penulis.pack(
            pady=10,
            padx=15,
            fill="x"
        )

        # Input Tahun
        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Tahun Terbit"
        )
        self.entry_tahun.pack(
            pady=10,
            padx=15,
            fill="x"
        )

        # ==========================================
        # TOMBOL AKSI
        # ==========================================

        # Tombol Simpan
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green",
            hover_color="darkgreen"
        )
        self.btn_simpan.pack(
            pady=8,
            padx=15,
            fill="x"
        )

        # Tombol Update
        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data",
            fg_color="blue",
            hover_color="darkblue"
        )
        self.btn_update.pack(
            pady=5,
            padx=15,
            fill="x"
        )

        # Tombol Hapus
        self.btn_hapus = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data",
            fg_color="red",
            hover_color="darkred"
        )
        self.btn_hapus.pack(
            pady=5,
            padx=15,
            fill="x"
        )

        # Tombol Logout
        self.btn_logout = ctk.CTkButton(
            self.frame_kiri,
            text="Logout",
            fg_color="gray",
            hover_color="darkgray"
        )
        self.btn_logout.pack(
            pady=10,
            padx=15,
            fill="x"
        )

        # ==========================================
        # FRAME KANAN: TABEL BUKU
        # ==========================================

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
            text="Daftar Koleksi Buku",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # ==========================================
        # STYLE TABEL
        # ==========================================

        style = ttk.Style()

        style.theme_use("default")

        style.configure(
            "Buku.Treeview",
            background="white",
            foreground="black",
            rowheight=27,
            fieldbackground="white",
            font=("Arial", 10)
        )

        style.configure(
            "Buku.Treeview.Heading",
            background="#D9D9D9",
            foreground="black",
            font=("Arial", 10, "bold")
        )

        # Warna ketika baris dipilih
        style.map(
            "Buku.Treeview",
            background=[
                ("selected", "#1F6AA5")
            ],
            foreground=[
                ("selected", "white")
            ]
        )

        # ==========================================
        # TABEL DATA BUKU
        # ==========================================

        kolom = (
            "id",
            "judul",
            "penulis",
            "tahun"
        )

        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings",
            height=15,
            selectmode="browse",
            style="Buku.Treeview"
        )

        # Header Tabel
        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")

        # Lebar Kolom
        self.tabel.column(
            "id",
            width=40,
            anchor="center"
        )

        self.tabel.column(
            "judul",
            width=150
        )

        self.tabel.column(
            "penulis",
            width=120
        )

        self.tabel.column(
            "tahun",
            width=80,
            anchor="center"
        )

        # Menampilkan Tabel
        self.tabel.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )


# ==========================================
# MENJALANKAN TAMPILAN
# ==========================================

if __name__ == "__main__":
    app = BukuView()
    app.mainloop()
