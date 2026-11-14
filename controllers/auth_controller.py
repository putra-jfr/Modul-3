
import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controllers import BukuController


class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()

        # Menghubungkan tombol Login
        self.view.btn_login.configure(
            command=self.proses_login
        )

    def proses_login(self):
        print("Tombol Masuk diklik!")

        # Mengambil username dan password
        username = self.view.entry_username.get()
        password = self.view.entry_password.get()

        # Validasi input kosong
        if not username or not password:
            messagebox.showwarning(
                "Peringatan",
                "Username dan Password wajib diisi!"
            )
            return

        # Memeriksa akun ke database
        user = self.model.authenticate(username, password)

        if user:
            messagebox.showinfo(
                "Login Berhasil",
                f"Selamat datang, {user['username']} ({user['role']})!"
            )

            # Menutup jendela Login
            self.view.destroy()

            # Membuka halaman utama sesuai role
            app_utama = BukuController(
                user_role=user['role']
            )

            app_utama.run()

        else:
            messagebox.showerror(
                "Login Gagal",
                "Username atau Password salah!"
            )

    def run(self):
        self.view.mainloop()
