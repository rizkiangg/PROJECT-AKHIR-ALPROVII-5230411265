import sqlite3

koneksi = sqlite3.connect('hewan.db')
kursor = koneksi.cursor()

print("Data sebelum dihapus : ")
kursor.execute("SELECT * FROM HEWAN")
rows = kursor.fetchall()

print("="*104)
print("{:<5} {:<20} {:<20} {:<20} {:<20}{:<20}".format(
    "ID", "Nama Hewan", "Jenis", "Asal", "Jumlah Saat Ini", "Tahun Ditemukan"))
print("-"*104)
for row in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20}{:<20}".format(
        row[0], row[1], row[2], row[3], row[4], row[5]))

jenis = "Mamalia"
kursor.execute(f"DELETE FROM HEWAN WHERE jenis = ?", (jenis,))
koneksi.commit()

# if kursor.rowcount > 0:
#     print(f"Data hewan dengan jenis {jenis} berhasil dihapus.")
# else:
#     print(f"Tidak ada data hewan dengan jenis {jenis}.")

print(f"Data hewan {jenis} berhasil dihapus.")
print("\nData setelah dihapus : ")
print("="*104)
print("{:<5} {:<20} {:<20} {:<20} {:<20}{:<20}".format(
    "ID", "Nama Hewan", "Jenis", "Asal", "Jumlah Saat Ini", "Tahun Ditemukan"))
print("-"*104)
for row in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20}{:<20}".format(
        row[0], row[1], row[2], row[3], row[4], row[5]))


koneksi.close()
