import sqlite3
koneksi = sqlite3.connect('hewan.db')
kursor = koneksi.cursor()

orangutan = 900
nama_hewan = "Orangutan"

kursor.execute(
    f'''
    UPDATE HEWAN SET jml_sekarang = {orangutan} WHERE nama_hewan = "{nama_hewan}"'''
)

koneksi.commit()

if kursor.rowcount > 0:
    print(f"Data {nama_hewan} berhasil diubah")
else:
    print(f"Data {nama_hewan} tidak ditemukan")

koneksi.close()
