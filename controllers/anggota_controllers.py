
from tkinter import messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Menghubungkan tombol dengan fungsi Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_delete.configure(command=self.hapus_data)

        # Menghubungkan klik tabel dengan fungsi pilih_data
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        # Memuat data saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data anggota dari Model
        data_anggota = self.model.get_all_anggota()

        # Memasukkan data ke dalam tabel
        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota['id_anggota'],
                    anggota['nama'],
                    anggota['alamat']
                )
            )

    def simpan_data(self):
        # Mengambil data dari form
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        # Validasi form kosong
        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat harus diisi!"
            )
            return

        # Mengirim data ke Model
        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil disimpan!"
            )

            # Membersihkan form
            self.view.entry_nama.delete(0, "end")
            self.view.entry_alamat.delete(0, "end")

            # Memuat ulang tabel
            self.muat_data_tabel()

        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal disimpan!"
            )

    def pilih_data(self, event):
        # Mengambil baris yang dipilih
        selected = self.view.tabel.selection()

        if selected:
            data = self.view.tabel.item(
                selected[0],
                "values"
            )

            # Memasukkan data ke form
            self.view.entry_nama.delete(0, "end")
            self.view.entry_nama.insert(0, data[1])

            self.view.entry_alamat.delete(0, "end")
            self.view.entry_alamat.insert(0, data[2])

    def perbarui_data(self):
        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data anggota yang ingin diperbarui!"
            )
            return

        data = self.view.tabel.item(
            selected[0],
            "values"
        )

        id_anggota = data[0]
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat harus diisi!"
            )
            return

        # Mengirim perubahan ke Model
        berhasil = self.model.update_anggota(
            id_anggota,
            nama,
            alamat
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil diperbarui!"
            )
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal diperbarui!"
            )

    def hapus_data(self):
        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data anggota yang ingin dihapus!"
            )
            return

        data = self.view.tabel.item(
            selected[0],
            "values"
        )

        id_anggota = data[0]

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data anggota ini?"
        )

        if konfirmasi:
            berhasil = self.model.delete_anggota(id_anggota)

            if berhasil:
                messagebox.showinfo(
                    "Sukses",
                    "Data anggota berhasil dihapus!"
                )

                self.view.entry_nama.delete(0, "end")
                self.view.entry_alamat.delete(0, "end")

                self.muat_data_tabel()

            else:
                messagebox.showerror(
                    "Error",
                    "Data anggota gagal dihapus!"
                )

    # Fungsi menjalankan aplikasi
    def run(self):
        self.view.mainloop()

# Menjalankan Controller
if __name__ == "__main__":
    app = AnggotaController()
    app.run()
