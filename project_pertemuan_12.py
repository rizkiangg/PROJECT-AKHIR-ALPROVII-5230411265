import sqlite3

# buat connection db
koneksi = sqlite3.connect('hewan.db')

kursor = koneksi.cursor()

# create table baru
koneksi.execute('''
                CREATE TABLE HEWAN(
                    id_hewan INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_hewan VARCHAR(50),
                    jenis VARCHAR(50),
                    asal VARCHAR(50),
                    jml_sekarang INTEGER(10),
                    thn_ditemukan INTEGER(10)
                );
                ''')


# BREAK
koneksi.close()
