# data.py yang berisi array dipisah beda file, sehingga membutuhkan import.0
from data import barang_array, harga_array, stok_array, kategori_array

# KAMUS PROGRAM VENDING MACHINE ITB
# program_jalan   : boolean, menentukan apakah program utama masih berjalan.
# pilihan_login   : input dari user di menu utama (1 untuk pembeli, 2 untuk admin, 3 untuk keluar).
# role            : string, menyimpan peran pengguna ('user' atau 'admin').
# lanjut_login    : boolean, menandakan apakah user boleh lanjut ke tahap berikut setelah login.
# pwd             : string, menyimpan password admin untuk verifikasi akses.
# lanjut_admin    : boolean, kontrol loop menu admin.
# valid_admin     : boolean, untuk mengecek apakah input admin valid.
# barang_array    : list of string, nama-nama barang di vending machine.
# harga_array     : list of int, harga tiap barang dalam satuan rupiah.
# stok_array      : list of int, jumlah stok tersedia untuk setiap barang.
# kategori_array  : list of string, kategori barang ('makanan' atau 'minuman').
# inp             : string input dari user untuk memilih nomor barang.
# tahap           : integer, menentukan tahap interaksi user (0=kategori, 1=daftar barang, 2=pembelian).
# kategori        : string, kategori yang dipilih user ('makanan' atau 'minuman').
# indeks_barang   : list of int, menyimpan indeks barang yang cocok dengan kategori pilihan user.
# idx_barang      : int, indeks dari barang yang sedang dibeli user.
# jumlah_beli     : int, jumlah barang yang ingin dibeli (maksimal 3).
# total_harga     : int, total biaya pembelian (harga x jumlah).
# uang_inp        : string, input uang dari pembeli.
# uang            : int, nilai uang yang dimasukkan pembeli.
# kembalian       : int, selisih antara uang dan total harga.
# ulang_lower     : string, hasil konversi input ulang menjadi huruf kecil.
# lanjut_user     : boolean, kontrol loop untuk pembeli.
# ==========================================

# Adapun command khusus seperti \033[1;31m hanya mengubah tampilan teks warna
# Beberapa algoritma diambil dari modul praktikum berkomputasional "python-id.pdf" seperti pengunaan str dan len() dalam konteks Modul 2: Perulangan dan Array

program_jalan = True

while program_jalan:
    print("\033[1;31m==========================================\033[0m")
    print("\033[1;31m||            VENDING MACHINE ITB       ||\033[0m")
    print("\033[1;31m==========================================\033[0m")
    print("\033[1;36m"""" 
⠀⠀⠀⠀   """""" 
⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣷⢸⣿⣿⡜⢯⣷⡌⡻⣿⣿⣿⣆⢈⠻⠿⢿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡁⢳⣿⣿⣿⣿⣿⣿⡜⣿⣿⣧⢀⢻⣷⠰⠈⢿⣿⣿⣧⢣⠉⠑⠪⢙⠿⠿⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣱⡇⡞⣿⣿⣿⣿⣿⣿⡇⣿⣿⡏⡄⣧⠹⡇⠧⠈⢻⣿⣿⡇⢧⢢⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣇⢃⢿⣿⣿⣿⣿⣿⣷⣿⣿⠇⢃⣡⣤⡹⠐⣿⣀⢻⣿⣿⢸⡎⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⣾⣿⣿⠘⡸⣿⣿⣿⣿⣿⣿⣿⡿⣰⣿⣿⢟⡷⠈⠋⠃⠎⢿⣿⡏⣿⠀⠘⢆⠀⠀⠀⠀⠀
⠀⡐⢹⣿⣿⡐⢡⢹⣿⣿⣿⣿⡏⣿⢣⣿⣿⡑⠁⠔⠀⠉⠉⠢⡘⣿⡇⣿⡇⠀⡀⠡⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡇⠘⣿⣿⣇⠇⢣⢻⣿⣿⣿⡇⢇⣾⣿⣿⡆⢸⣤⡀⠚⢂⠀⢡⢿⡇⣿⡇⠀⢿⠀⠀⠄⠀⠀⠀
⠀⣿⠠⠹⣿⣿⡘⣆⢣⠻⣿⣿⢈⣾⣿⣿⣿⣶⣸⣏⢀⣬⣋⡼⣠⢸⢹⣿⡇⢠⣼⠙⡄⠀⠀⠀⠀⠀
⠀⢹⡇⠁⠹⣿⣇⠹⡃⠃⠙⡇⠘⢿⣿⣿⣿⣿⣿⣏⣓⣉⣭⣴⣿⠘⢸⣿⠁⠘⠋⠀⠹⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢷⠀⠀⠈⢿⣇⠂⣷⠄⠐⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⢸⡏⠀⢀⣠⣴⣾⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⢆⠀⠀⠀⠙⠆⠈⠢⠲⠥⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡞⣸⠁⠀⢸⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⠃⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡏⠹⣿⣿⡿⠫⠊⠀⠀⠀⣶⠀⢻⣿⣿⣿⣿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    \033[0m""")

    print("Pilih:")
    print("1. Pembeli")
    print("2. Admin")
    print("3. Keluar program")

    pilihan_login = input("Masukkan pilihan (1/2/3): ")

    lanjut_login = True
    role = ""

    if pilihan_login == "1":
        role = "user"
    elif pilihan_login == "2":
        role = "admin"
    elif pilihan_login == "3":
        print("Terima kasih telah menggunakan vending machine!")
        program_jalan = False
        lanjut_login = False
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
        lanjut_login = False

    if role == "admin" and lanjut_login:
        pwd = input("Masukkan password admin: ")
        if pwd != "itb123":
            print("Password salah. Kembali ke menu login.\n")
            lanjut_login = False

    if role == "admin" and lanjut_login:
        lanjut_admin = True
        while lanjut_admin:
            print("\033[1;31m=======================================================\033[0m")
            print("\033[1;31m||              MENU ADMIN VENDING ITB               ||\033[0m")
            print("\033[1;31m=======================================================\033[0m")

            for i in range(len(barang_array)):
                # Buat nama dengan padding manual
                nama = barang_array[i]
                while len(nama) < 15:
                    nama = nama + " "
                
                # Buat harga dengan padding manual
                harga_str = "Rp" + str(harga_array[i])
                while len(harga_str) < 8:
                    harga_str = " " + harga_str
                
                # Buat stok dengan padding manual
                stok_str = "stok:" + str(stok_array[i])
                while len(stok_str) < 10:
                    stok_str = " " + stok_str
                
                # Buat kategori dengan padding manual
                kategori_str = "(" + kategori_array[i] + ")"
                while len(kategori_str) < 11:
                    kategori_str = " " + kategori_str
                
                baris = str(i+1) + ". " + nama + " " + harga_str + " " + stok_str + " " + kategori_str
                while len(baris) < 38:
                    baris = baris + " "
                print("\033[1;31m|| " + baris + "||\033[0m")

            print("\033[1;31m==========================================\033[0m")
            print("1. Tambah stok barang")
            print("2. Ubah harga barang")
            print("3. Tambah barang baru")
            print("4. Logout ke menu login")

            pilihan = input("Pilih menu (1-4): ")
            valid_admin = True

            if pilihan == "1":
                inp = input("Masukkan nomor barang: ")
                # Cek apakah input adalah angka
                is_digit = True
                if len(inp) == 0:
                    is_digit = False
                else:
                    for char in inp:
                        if char < "0" or char > "9":
                            is_digit = False
                
                if is_digit:
                    idx = int(inp) - 1
                    if 0 <= idx < len(barang_array):
                        tambah_inp = input("Tambah stok sebanyak: ")
                        # Cek apakah tambah_inp adalah angka
                        is_digit_tambah = True
                        if len(tambah_inp) == 0:
                            is_digit_tambah = False
                        else:
                            for char in tambah_inp:
                                if char < "0" or char > "9":
                                    is_digit_tambah = False
                        
                        if is_digit_tambah:
                            stok_array[idx] = stok_array[idx] + int(tambah_inp)
                            print("Stok " + barang_array[idx] + " sekarang " + str(stok_array[idx]))
                        else:
                            print("Input harus berupa angka!")
                            valid_admin = False
                    else:
                        print("Nomor tidak valid.")
                        valid_admin = False
                else:
                    print("Input harus berupa angka!")
                    valid_admin = False

            elif pilihan == "2":
                inp = input("Masukkan nomor barang: ")
                # Cek apakah input adalah angka
                is_digit = True
                if len(inp) == 0:
                    is_digit = False
                else:
                    for char in inp:
                        if char < "0" or char > "9":
                            is_digit = False
                
                if is_digit:
                    idx = int(inp) - 1
                    if 0 <= idx < len(barang_array):
                        harga_inp = input("Masukkan harga baru: ")
                        # Cek apakah harga_inp adalah angka
                        is_digit_harga = True
                        if len(harga_inp) == 0:
                            is_digit_harga = False
                        else:
                            for char in harga_inp:
                                if char < "0" or char > "9":
                                    is_digit_harga = False
                        
                        if is_digit_harga:
                            harga_array[idx] = int(harga_inp)
                            print("Harga " + barang_array[idx] + " sekarang Rp" + str(harga_array[idx]))
                        else:
                            print("Input harus berupa angka!")
                            valid_admin = False
                    else:
                        print("Nomor tidak valid.")
                        valid_admin = False
                else:
                    print("Input harus berupa angka!")
                    valid_admin = False

            elif pilihan == "3":
                nama_baru = input("Masukkan nama barang baru: ")
                harga_inp = input("Masukkan harga barang: ")
                stok_inp = input("Masukkan stok barang: ")
                
                # Cek apakah harga_inp adalah angka
                is_digit_harga = True
                if len(harga_inp) == 0:
                    is_digit_harga = False
                else:
                    for char in harga_inp:
                        if char < "0" or char > "9":
                            is_digit_harga = False
                
                # Cek apakah stok_inp adalah angka
                is_digit_stok = True
                if len(stok_inp) == 0:
                    is_digit_stok = False
                else:
                    for char in stok_inp:
                        if char < "0" or char > "9":
                            is_digit_stok = False
                
                if is_digit_harga and is_digit_stok:
                    print("Pilih kategori:")
                    print("1. Makanan")
                    print("2. Minuman")
                    kategori_input = input("Masukkan pilihan (1/2): ")
                    if kategori_input == "1":
                        kategori_baru = "makanan"
                    elif kategori_input == "2":
                        kategori_baru = "minuman"
                    else:
                        print("Kategori tidak valid! Barang tidak ditambahkan.")
                        valid_admin = False
                        kategori_baru = ""
                    if kategori_baru != "":
                        # Tambah barang baru ke array secara manual
                        barang_array = barang_array + [nama_baru]
                        harga_array = harga_array + [int(harga_inp)]
                        stok_array = stok_array + [int(stok_inp)]
                        kategori_array = kategori_array + [kategori_baru]
                        print("Barang '" + nama_baru + "' berhasil ditambahkan ke kategori '" + kategori_baru + "'!")
                else:
                    print("Harga dan stok harus berupa angka!")
                    valid_admin = False

            elif pilihan == "4":
                lanjut_admin = False
                print("\nLogout berhasil. Kembali ke menu login.")
            else:
                print("Menu tidak valid.")
                valid_admin = False

            if lanjut_admin and valid_admin:
                ulang = input("Apakah ingin melakukan aksi lain (y/n)? ")
                # Convert ke lowercase manual
                ulang_lower = ""
                for char in ulang:
                    if char >= "A" and char <= "Z":
                        ulang_lower = ulang_lower + chr(ord(char) + 32)
                    else:
                        ulang_lower = ulang_lower + char
                
                if ulang_lower != "y":
                    lanjut_admin = False

    elif role == "user" and lanjut_login:
        lanjut_user = True
        tahap = 0
        kategori = ""

        while lanjut_user:
            if tahap == 0:
                print("\033[1;31m\n==========================================\033[0m")
                print("\033[1;31m||        PILIH KATEGORI PRODUK          ||\033[0m")
                print("\033[1;31m==========================================\033[0m")
                print("Ketik:")
                print("\033[1;34m1 - Makanan\033[0m")
                print("\033[1;33m2 - Minuman\033[0m")
                print("\033[1;31m0 - Kembali ke menu utama\033[0m")

                pilih_kategori = input("Masukkan pilihan: ")
                # Convert ke lowercase manual
                pilih_kategori_lower = ""
                for char in pilih_kategori:
                    if char >= "A" and char <= "Z":
                        pilih_kategori_lower = pilih_kategori_lower + chr(ord(char) + 32)
                    else:
                        pilih_kategori_lower = pilih_kategori_lower + char
                
                if pilih_kategori_lower == "0":
                    print("Kembali ke menu utama...\n")
                    lanjut_user = False
                elif pilih_kategori_lower == "1":
                    kategori = "makanan"
                    tahap = 1
                elif pilih_kategori_lower == "2":
                    kategori = "minuman"
                    tahap = 1
                else:
                    print("Input tidak valid. Coba lagi.")
                    tahap = 0

            elif tahap == 1:
                print("\033[1;31m\n==========================================\033[0m")
                
                # Convert kategori ke uppercase manual
                kategori_upper = ""
                for char in kategori:
                    if char >= "a" and char <= "z":
                        kategori_upper = kategori_upper + chr(ord(char) - 32)
                    else:
                        kategori_upper = kategori_upper + char
                
                print("\033[1;31m||     MENU " + kategori_upper + " VENDING ITB          ||\033[0m")
                print("\033[1;31m==========================================\033[0m")

                # Buat list indeks barang dengan kategori yang dipilih
                indeks_barang = []
                for i in range(len(barang_array)):
                    if kategori_array[i] == kategori:
                        indeks_barang = indeks_barang + [i]

                if len(indeks_barang) == 0:
                    print("Belum ada barang dalam kategori ini.")
                    tahap = 0
                else:
                    for j in range(len(indeks_barang)):
                        i = indeks_barang[j]
                        # Buat nama dengan padding manual
                        nama = barang_array[i]
                        while len(nama) < 15:
                            nama = nama + " "
                        
                        # Buat harga dengan padding manual
                        harga_str = "Rp" + str(harga_array[i])
                        while len(harga_str) < 8:
                            harga_str = " " + harga_str
                        
                        # Buat stok dengan padding manual
                        stok_str = "stok:" + str(stok_array[i])
                        while len(stok_str) < 10:
                            stok_str = " " + stok_str
                        
                        baris = str(j+1) + ". " + nama + " " + harga_str + " " + stok_str
                        while len(baris) < 38:
                            baris = baris + " "
                        print("\033[1;31m|| " + baris + "||\033[0m")

                    print("\033[1;31m==========================================\033[0m")
                    print("\033[1;32mKetik 0 untuk kembali ke pilihan kategori.\033[0m")

                    inp = input("Masukkan nomor barang yang ingin dibeli: ")
                    # Cek apakah input adalah angka
                    is_digit = True
                    if len(inp) == 0:
                        is_digit = False
                    else:
                        for char in inp:
                            if char < "0" or char > "9":
                                is_digit = False
                    
                    if is_digit:
                        pilihan = int(inp)
                        if pilihan == 0:
                            tahap = 0
                        else:
                            pilihan = pilihan - 1
                            if 0 <= pilihan < len(indeks_barang):
                                idx_barang = indeks_barang[pilihan]
                                if stok_array[idx_barang] == 0:
                                    print("\033[1;31mMaaf, stok barang tersebut habis.\033[0m")
                                    tahap = 1
                                else:
                                    tahap = 2
                            else:
                                print("\033[1;31mNomor tidak valid.\033[0m")
                                tahap = 1
                    else:
                        print("\033[1;31mMasukkan angka yang valid.\033[0m")
                        tahap = 1

            elif tahap == 2:
                idx = idx_barang
                print("\033[1;34m\nAnda memilih " + barang_array[idx] + " seharga Rp" + str(harga_array[idx]) + " per item\033[0m")
                print("\033[1;34mStok tersedia: " + str(stok_array[idx]) + "\033[0m")
                print("\033[1;32mKetik 0 untuk kembali ke daftar barang.\033[0m")

                jumlah_inp = input("Mau beli berapa? (maksimal 3): ")
                # Cek apakah jumlah_inp adalah angka
                is_digit = True
                if len(jumlah_inp) == 0:
                    is_digit = False
                else:
                    for char in jumlah_inp:
                        if char < "0" or char > "9":
                            is_digit = False
                
                if is_digit:
                    jumlah_beli = int(jumlah_inp)
                    if jumlah_beli == 0:
                        tahap = 1
                    elif jumlah_beli < 0 or jumlah_beli > 3:
                        print("Jumlah tidak valid (1–3 saja).")
                        tahap = 2
                    elif jumlah_beli > stok_array[idx]:
                        print("Stok tidak mencukupi.")
                        tahap = 2
                    else:
                        total_harga = harga_array[idx] * jumlah_beli
                        print("\033[1;34mTotal harga: Rp" + str(total_harga) + "\033[0m")
                        uang_inp = input("Masukkan uang anda (Rp): ")
                        # Cek apakah uang_inp adalah angka
                        is_digit_uang = True
                        if len(uang_inp) == 0:
                            is_digit_uang = False
                        else:
                            for char in uang_inp:
                                if char < "0" or char > "9":
                                    is_digit_uang = False
                        
                        if is_digit_uang:
                            uang = int(uang_inp)
                            if uang == 0:
                                tahap = 1
                            elif uang < total_harga:
                                print("\033[1;31mGagal, uang anda kurang Rp" + str(total_harga - uang) + ".\033[0m")
                                tahap = 1
                            else:
                                kembalian = uang - total_harga
                                stok_array[idx] = stok_array[idx] - jumlah_beli
                                print("\033[1;33mAnda membeli " + str(jumlah_beli) + " " + barang_array[idx] + ". Kembalian anda: Rp" + str(kembalian) + ".\033[0m")
                                print("\033[1;33mSisa stok " + barang_array[idx] + ": " + str(stok_array[idx]) + "\033[0m")
                                ulang = input("Apakah ingin membeli lagi? (y/n): ")
                                # Convert ke lowercase manual
                                ulang_lower = ""
                                for char in ulang:
                                    if char >= "A" and char <= "Z":
                                        ulang_lower = ulang_lower + chr(ord(char) + 32)
                                    else:
                                        ulang_lower = ulang_lower + char
                                
                                if ulang_lower == "y":
                                    tahap = 0
                                else:
                                    lanjut_user = False
                                    print("\nTerima kasih telah berbelanja di vending machine!\n")
                        else:
                            print("Masukkan angka yang valid untuk uang.")
                            tahap = 2
                else:
                    print("Masukkan angka yang valid untuk jumlah.")
                    tahap = 2
