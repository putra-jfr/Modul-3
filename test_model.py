from models.buku_model import BukuModel

model = BukuModel()

# =========================
# CREATE
# =========================
print("=== Menambah Buku ===")
model.create_buku(
    "Pemrograman Python MVC",
    "Guido van Rossum",
    2023
)
print("Data berhasil disimpan ke Laragon MySQL!")

# =========================
# READ
# =========================
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )

# Ambil ID buku terakhir
id_buku = daftar_buku[-1]["id_buku"]

# =========================
# UPDATE
# =========================
print("\n=== Update Buku ===")

model.update_buku(
    id_buku,
    "Pemrograman Python Lanjutan",
    "Guido van Rossum",
    2024
)

print(f"Buku dengan ID {id_buku} berhasil di-update!")

# Tampilkan hasil update
print("\n=== Daftar Buku Setelah Update ===")
daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )

# =========================
# DELETE
# =========================
print("\n=== Delete Buku ===")

model.delete_buku(id_buku)

print(f"Buku dengan ID {id_buku} berhasil dihapus!")

# Tampilkan hasil delete
print("\n=== Daftar Buku Setelah Delete ===")
daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )

from models.anggota_model import AnggotaModel

anggota = AnggotaModel()

print("\n=== Menambah Anggota ===")
anggota.create_anggota("Andi", "Palu")
print("Data anggota berhasil disimpan ke Laragon MySQL!")

print("\n=== Daftar Anggota ===")
daftar_anggota = anggota.get_all_anggota()

for item in daftar_anggota:
    print(
        f"[{item['id_anggota']}] "
        f"{item['nama']} - "
        f"{item['alamat']}"
    )