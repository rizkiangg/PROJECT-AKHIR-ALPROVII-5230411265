import sqlite3

koneksi = sqlite3.connect('hewan.db')
Kursor = koneksi.cursor()

Kursor.execute("SELECT SUM(jml_sekarang) FROM HEWAN")
jml_hewan = Kursor.fetchone()[0]

print(f"Total jumlah seluruh hewan langka : {jml_hewan}")

koneksi.close()
