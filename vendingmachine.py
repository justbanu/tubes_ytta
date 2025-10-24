from data import barang_array, harga_array, stok_array, kategori_array  # import semua array

program_jalan = True # Selama True, program akan terus berulang hingga user memilih keluar (3. Keluar program).

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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⠿⠿⠿⢋⠀⠀⠀⠀⢀⣼⣿⡆⠈⣿⣿⣿⡟⣱⡷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⣁⡀⠨⣛⠿⠶⠄⢀⣠⣾⣿⣿⣷⠀⢹⣿⡟⣴⠈⢃⣶⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⣿⣿⡿⠀⡀⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⠻⣿⣿⢀⠙⠻⠿⣿⣿⣿⣿⣿⣿⡇⠁⣿⠟⡀⠈⣧⢰⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠴⠮⣥⠻⢧⣤⣄⣀⡉⢩⣭⣍⣃⣀⣩⠎⢀⣼⠉⣼⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠁⣛⠓⢒⣒⣢⡭⢁⡈⠿⠿⠟⠹⠛⠁⠀⠀⠀⠰⠃⠂⠀⠀⠀ 
    \033[0m""") # Yaudahlahya, ASCII ART

    print("Pilih:")
    print("1. Pembeli")
    print("2. Admin")
    print("3. Keluar program")

    pilihan_login = input("Masukkan pilihan (1/2/3): ") # Input sesuai pilihan

    #Menentukan peran yang dipilih user, lewat percabangan
    if pilihan_login == "1":
        role = "user"
    elif pilihan_login == "2":
        role = "admin"
    elif pilihan_login == "3":
        print("Terima kasih telah menggunakan vending machine!")
        program_jalan = False
        continue # Tidak bisa running sisa kode di bawahnya, langsung ulang ke atas loop.
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
        continue # Tidak bisa running sisa kode di bawahnya, langsung ulang ke atas loop.

    # ========== LOGIN ADMIN ==========
    if role == "admin":
        pwd = input("Masukkan password admin: ")
        if pwd != "itb123":
            print("Password salah. Kembali ke menu login.\n")
            continue  # Tidak bisa running sisa kode di bawahnya, langsung ulang ke atas loop.

    # ========== MODE ADMIN ==========
    if role == "admin":
        lanjut_admin = True
        while lanjut_admin: #Selama lanjut_admin=ture, maka program akan looping
            print("\033[1;31m=======================================================\033[0m")
            print("\033[1;31m||              MENU ADMIN VENDING ITB               ||\033[0m")
            print("\033[1;31m=======================================================\033[0m")
            for i, barang in enumerate(barang_array): # Melakukan looping untuk setiap elemen di barang_array (daftar barang di mesin). enumerate() memberikan indeks i (dimulai dari 0) dan nilai barang (nama barang
                # Format kolom biar rapi
                nama = barang.ljust(15) #barang.ljust Bikin teks barang rata kiri dan panjang total 15 karakter.
                harga = f"Rp{harga_array[i]}".rjust(8) # Rata kanan sepanjang 8 karakter.
                stok = f"stok:{stok_array[i]}".rjust(10) # Menampilkan stok tiap barang, misalnya "stok:5", dengan rata kanan sepanjang 10 karakter
                kategori = f"({kategori_array[i]})".rjust(11) # Ini buat menampilkan kategori (misalnya (makanan) atau (minuman)) dengan posisi rata kanan juga.
                baris = f"{i+1}. {nama} {harga} {stok} {kategori}" #Menggabungkan semua komponen jadi satu baris lengkap untuk satu barang, misalnya: 1. Aqua           Rpxx    Stok:x      (minuman)
                print(f"\033[1;31m|| {baris.ljust(38)}||\033[0m") #Mencetak setiap baris dengan warna merah (\033[1;31m) dan batas kiri-kanan || agar tampil rapi seperti tabel. baris.ljust(38) memastikan panjang teks dalam tabel sejajar
            print("\033[1;31m==========================================\033[0m")
            print("1. Tambah stok barang")
            print("2. Ubah harga barang")
            print("3. Tambah barang baru")
            print("4. Logout ke menu login")

            pilihan = input("Pilih menu (1-4): ") # Pilian menu

            if pilihan == "1": # jika milih 2
                try: # Mencegah program error dan berhenti saat admin salah input, jika error lompat ke except
                    idx = int(input("Masukkan nomor barang: ")) - 1 # digunakan untuk memasukkan nomor barang, lalu dikurangi 1 (karena indeks array mulai dari 0).
                    if 0 <= idx < len(barang_array): # Percabangan, berfungis mengecek apakah nomor barang valid (tidak melebihi jumlah barang).
                        tambah = int(input("Tambah stok sebanyak: ")) # Admin memasukkan berapa stok yang mau ditambahkan
                        stok_array[idx] += tambah # Nilai stok di stok_array ditambah.
                        print(f"Stok {barang_array[idx]} sekarang {stok_array[idx]}") #Lalu hasilnya ditampilkan
                    else: # Jika nomor barang tidak valid
                        print("Nomor tidak valid.") 
                except ValueError: # Kalau ada error, pada input awal
                    print("Input harus berupa angka!")
            #Belaku juga di pilihan 2
            elif pilihan == "2": 
                try:
                    idx = int(input("Masukkan nomor barang: ")) - 1
                    if 0 <= idx < len(barang_array):
                        harga_baru = int(input("Masukkan harga baru: "))
                        harga_array[idx] = harga_baru
                        print(f"Harga {barang_array[idx]} sekarang Rp{harga_baru}")
                    else:
                        print("Nomor tidak valid.")
                except ValueError:
                    print("Input harus berupa angka!")

            elif pilihan == "3":
                nama_baru = input("Masukkan nama barang baru: ")
                try:
                    harga_baru = int(input("Masukkan harga barang: "))
                    stok_baru = int(input("Masukkan stok barang: "))
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
                        continue

                    # Kalau semua input valid, barang baru disimpan ke dalam daftar, append() artinya menambahkan satu data baru ke bagian paling akhir dari list
                    barang_array.append(nama_baru)
                    harga_array.append(harga_baru)
                    stok_array.append(stok_baru)
                    kategori_array.append(kategori_baru)

                    print(f"Barang '{nama_baru}' berhasil ditambahkan ke kategori '{kategori_baru}'!")
                except ValueError:
                    print("Harga dan stok harus berupa angka!")

            elif pilihan == "4": 
                lanjut_admin = False # karnea pilihan 4 maka keluar dari loop lanjut_admin
                print("\nLogout berhasil. Kembali ke menu login.")
            else:
                print("Menu tidak valid.")

            if lanjut_admin: # kondisi lanjut atau tidak
                ulang = input("Apakah ingin melakukan aksi lain (y/n)? ").lower() # Lower buat all cases kapital dan tidak
                if ulang != "y": # Kalau jawaban bukan y
                    lanjut_admin = False # Menghentikan loop lanjut_admin

    # ========== MODE USER ==========
    elif role == "user": # Jika milih user dari percabangan sebelumnya
        lanjut_user = True #S elama lanjut_user bernilai True, maka menu user akan terus diulang
        tahap = 0 # Dimulai dari 0 yaitu tahap pilih kategori
        kategori = "" # Ini untuk menyimpan kategori yang dipilih user nanti
        while lanjut_user: # Loop utama untuk menu pembeli

            # ====== Tahap 0: pilih kategori ======
            if tahap == 0:
                print("\033[1;31m\n==========================================\033[0m")
                print("\033[1;31m||        PILIH KATEGORI PRODUK          ||\033[0m")
                print("\033[1;31m==========================================\033[0m")
                print("Ketik:")
                print("\033[1;34m1 - Makanan\033[0m")
                print("\033[1;33m2 - Minuman\033[0m")
                print("\033[1;31m0 - Kembali ke menu utama\033[0m")

                pilih_kategori = input("Masukkan pilihan: ").lower()
                if pilih_kategori == "0": # jika pilihan 0
                    print("Kembali ke menu utama...\n") 
                    lanjut_user = False # lanjut_user = False, supaya loop while lanjut_user berhenti (keluar dari mode user).
                    continue # lompat ke program berikutnya dalam loop, jadi baris di bawahnya tidak dijalankan
                elif pilih_kategori == "1": # jika milih 1
                    kategori = "makanan" # Variabel kategori menyimpan "makanan
                    tahap = 1 #  tahap diubah jadi 1, artinya naik ke tahap berikutnya (menampilkan daftar makanan)
                elif pilih_kategori == "2": # jika milih 2
                    kategori = "minuman" #
                    tahap = 1
                else: #Kalau input-nya bukan “0”, “1”, atau “2”, berarti salah.
                    print("Input tidak valid. Coba lagi.")
                    continue # Membuat program balik ke awal loop untuk minta input ulang.

            # ====== Tahap 1: tampilkan daftar barang admin) ======
            elif tahap == 1:
                print("\033[1;31m\n==========================================\033[0m")
                print(f"\033[1;31m||     MENU {kategori.upper()} VENDING ITB          ||\033[0m") # Menampilkan kategori dalam huruf besar semua
                print("\033[1;31m==========================================\033[0m")

                indeks_barang = [i for i in range(len(barang_array)) if kategori_array[i] == kategori] # Buat daftar berisi indeks (urutan) barang yang kategorinya sesuai dengan yang user pilih.

                if not indeks_barang: # Kalau indeks_barang kosong ([]), artinya belum ada barang dalam kategori tersebut.
                    print("Belum ada barang dalam kategori ini.")
                    tahap = 0
                    continue #  lalu kembali ke tahap 0

                for j, i in enumerate(indeks_barang): # enumerate(indeks_barang), artinya biar menampilkan  nomor urut (j) dan indeks asli (i).
                    nama = barang_array[i].ljust(15) # ljust dan rjust → buat tampilan teks rapi (rata kiri dan kanan).
                    harga = f"Rp{harga_array[i]}".rjust(8)
                    stok = f"stok:{stok_array[i]}".rjust(10)
                    baris = f"{j+1}. {nama} {harga} {stok}"
                    print(f"\033[1;31m|| {baris.ljust(38)}||\033[0m")

                print("\033[1;31m==========================================\033[0m")
                print("\033[1;32mKetik 0 untuk kembali ke pilihan kategori.\033[0m")

                try: # dibungkus try-except agar kalau user mengetik huruf (misal “abc”), program tidak error tapi tampil pesan “Masukkan angka yang valid
                    pilihan = int(input("Masukkan nomor barang yang ingin dibeli: ")) # Program minta user mengetik nomor barang.
                    if pilihan == 0: # Artinya user ingin kembali ke menu kategori.
                        tahap = 0
                        continue
                    pilihan -= 1 # Python menghitung mulai dari 0 (indeks list dimulai dari 0).
                    if 0 <= pilihan < len(indeks_barang): #  Cek apakah nomor yang dimasukkan ada dalam daftar.
                        idx_barang = indeks_barang[pilihan] # Ambil indeks asli barang dari daftar indeks_barang sesuai nomor yang dipilih user
                        if stok_array[idx_barang] == 0: # Kalau stok-nya 0 
                            print("\033[1;31mMaaf, stok barang tersebut habis.\033[0m")
                            continue # pengulangan 
                        else: 
                            tahap = 2
                    else:
                        print("\033[1;31mNomor tidak valid.\033[0m")
                        continue # pengunlangan
                except ValueError: # kalau input huruf
                    print("\033[1;31mMasukkan angka yang valid.\033[0m")
                    continue # pengulangan 

            # ====== Tahap 2: masukkan uang dan jumlah beli ======
            elif tahap == 2: # User sudah memilih barang dari daftar dan sekarang masuk ke tahap transaksi pembelian
                idx = idx_barang # Variabel idx_barang berisi indeks asli barang di list barang_array, dan disimpan ke idx biar lebih singkat
                print(f"\033[1;34m\nAnda memilih {barang_array[idx]} seharga Rp{harga_array[idx]} per item\033[0m")
                print(f"\033[1;34mStok tersedia: {stok_array[idx]}\033[0m")
                print("\033[1;32mKetik 0 untuk kembali ke daftar barang.\033[0m")

                try: # Dibungkus try supaya kalau user salah ketik (misalnya huruf), program tidak error
                    jumlah_beli = int(input("Mau beli berapa? (maksimal 3): "))
                    if jumlah_beli == 0: # Cek kondisi jumlah pembelian
                        tahap = 1 # Kalau user ketik 0, artinya ingin kembali ke daftar barang, jadi tahap = 1
                        continue # pengulangan
                    elif jumlah_beli < 0 or jumlah_beli > 3: # Kalau user isi negatif atau lebih dari 3, tampil pesan “Jumlah tidak valid
                        print("Jumlah tidak valid (1–3 saja).")
                        continue # pengulangan
                    elif jumlah_beli > stok_array[idx]: # Kalau user mau beli lebih banyak dari stok tersedia, muncul pesan “Stok tidak mencukupi
                        print("Stok tidak mencukupi.")
                        continue # pengulangan
                except ValueError: # Kalau user salah input (misalnya huruf), tampil pesan error dan ulang lagi input.
                    print("Masukkan angka yang valid untuk jumlah.")
                    continue # pengulangan

                total_harga = harga_array[idx] * jumlah_beli # Kalikan harga per item dengan jumlah beli, lalu tampilkan total harga
                print(f"\033[1;34mTotal harga: Rp{total_harga}\033[0m")

                try:
                    uang = int(input("Masukkan uang anda (Rp): "))
                    if uang == 0: # Kalau user ketik 0, berarti batal beli → kembali ke daftar barang (tahap 1).
                        tahap = 1 
                        continue 
                except ValueError: # Kalau input-nya bukan angka (misal “seribu”), program tidak error, hanya menampilkan pesan “Masukkan angka yang valid"
                    print("Masukkan angka yang valid untuk uang.")
                    continue

                if uang < total_harga: # Kalau uang yang dimasukkan kurang, program kasih tahu berapa kekurangannya, lalu balik ke daftar barang (tahap 1).
                    print(f"\033[1;31mGagal, uang anda kurang Rp{total_harga - uang}.\033[0m")
                    tahap = 1
                    continue
                else: # Kalau uang cukup
                    kembalian = uang - total_harga # Hitung kembalian
                    stok_array[idx] -= jumlah_beli # Kurangi stok barang sesuai jumlah beli
                    print(f"\033[1;33mAnda membeli {jumlah_beli} {barang_array[idx]}. Kembalian anda: Rp{kembalian}.\033[0m")
                    print(f"\033[1;33mSisa stok {barang_array[idx]}: {stok_array[idx]}\033[0m")

                ulang = input("Apakah ingin membeli lagi? (y/n): ").lower() # Mau beli lagi atau tidak
                if ulang == "y": # Kalau user ketik “y”, balik ke tahap 0 (pilih kategori lagi)
                    tahap = 0
                else: # Kalau ketik “n”, keluar dari mode user, menampilkan pesan terima kasih
                    lanjut_user = False
                    print("\nTerima kasih telah berbelanja di vending machine!\n")
