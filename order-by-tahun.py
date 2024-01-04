import sqlite3

koneksi = sqlite3.connect('hewan.db')
kursor = koneksi.cursor()
kursor.execute(
    "SELECT * FROM HEWAN ORDER BY thn_ditemukan ASC")
rows = kursor.fetchall()

print("="*104)
print("{:<5} {:<20} {:<20} {:<20} {:<20}{:<20}".format(
    "ID", "Nama Hewan", "Jenis", "Asal", "Jumlah Saat Ini", "Tahun Ditemukan"))
print("-"*104)
for row in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20}{:<20}".format(
        row[0], row[1], row[2], row[3], row[4], row[5]))

koneksi.close()
