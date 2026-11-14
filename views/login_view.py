import customtkinter as ctk


class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Sistem Perpustakaan")
        self.geometry("360x320")
        self.resizable(False, False)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=25, pady=20, fill="both", expand=True)

        ctk.CTkLabel(
            self.frame, text="LOGIN SISTEM",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 15))

        self.entry_username = ctk.CTkEntry(
            self.frame, placeholder_text="Username"
        )
        self.entry_username.pack(padx=20, pady=8, fill="x")

        self.entry_password = ctk.CTkEntry(
            self.frame, placeholder_text="Password", show="*"
        )
        self.entry_password.pack(padx=20, pady=8, fill="x")

        self.btn_login = ctk.CTkButton(
            self.frame, text="Masuk"
        )
        self.btn_login.pack(padx=20, pady=(15, 8), fill="x")