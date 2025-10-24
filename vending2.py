from data import barang_array, harga_array, stok_array, kategori_array

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

    if pilihan_login == "1":
        role = "user"
    elif pilihan_login == "2":
        role = "admin"
    elif pilihan_login == "3":
        print("Terima kasih telah menggunakan vending machine!")
        program_jalan = False
        continue
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
        continue

    if role == "admin":
        pwd = input("Masukkan password admin: ")
        if pwd != "itb123":
            print("Password salah. Kembali ke menu login.\n")
            continue

    if role == "admin":
        lanjut_admin = True
        while lanjut_admin:
            print("\033[1;31m=======================================================\033[0m")
            print("\033[1;31m||              MENU ADMIN VENDING ITB               ||\033[0m")
            print("\033[1;31m=======================================================\033[0m")
            for i, barang in enumerate(barang_array):
                nama = barang.ljust(15)
                harga = f"Rp{harga_array[i]}".rjust(8)
                stok = f"stok:{stok_array[i]}".rjust(10)
                kategori = f"({kategori_array[i]})".rjust(11)
                baris = f"{i+1}. {nama} {harga} {stok} {kategori}"
                print(f"\033[1;31m|| {baris.ljust(38)}||\033[0m")

            print("\033[1;31m==========================================\033[0m")
            print("1. Tambah stok barang")
            print("2. Ubah harga barang")
            print("3. Tambah barang baru")
            print("4. Logout ke menu login")

            pilihan = input("Pilih menu (1-4): ")

            if pilihan == "1":
                inp = input("Masukkan nomor barang: ")
                if not inp.isdigit():
                    print("Input harus berupa angka!")
                    continue
                idx = int(inp) - 1
                if 0 <= idx < len(barang_array):
                    tambah_inp = input("Tambah stok sebanyak: ")
                    if not tambah_inp.isdigit():
                        print("Input harus berupa angka!")
                        continue
                    stok_array[idx] += int(tambah_inp)
                    print(f"Stok {barang_array[idx]} sekarang {stok_array[idx]}")
                else:
                    print("Nomor tidak valid.")

            elif pilihan == "2":
                inp = input("Masukkan nomor barang: ")
                if not inp.isdigit():
                    print("Input harus berupa angka!")
                    continue
                idx = int(inp) - 1
                if 0 <= idx < len(barang_array):
                    harga_inp = input("Masukkan harga baru: ")
                    if not harga_inp.isdigit():
                        print("Input harus berupa angka!")
                        continue
                    harga_array[idx] = int(harga_inp)
                    print(f"Harga {barang_array[idx]} sekarang Rp{harga_array[idx]}")
                else:
                    print("Nomor tidak valid.")

            elif pilihan == "3":
                nama_baru = input("Masukkan nama barang baru: ")
                harga_inp = input("Masukkan harga barang: ")
                stok_inp = input("Masukkan stok barang: ")
                if not (harga_inp.isdigit() and stok_inp.isdigit()):
                    print("Harga dan stok harus berupa angka!")
                    continue

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

                barang_array.append(nama_baru)
                harga_array.append(int(harga_inp))
                stok_array.append(int(stok_inp))
                kategori_array.append(kategori_baru)

                print(f"Barang '{nama_baru}' berhasil ditambahkan ke kategori '{kategori_baru}'!")

            elif pilihan == "4":
                lanjut_admin = False
                print("\nLogout berhasil. Kembali ke menu login.")
            else:
                print("Menu tidak valid.")

            if lanjut_admin:
                ulang = input("Apakah ingin melakukan aksi lain (y/n)? ").lower()
                if ulang != "y":
                    lanjut_admin = False

    elif role == "user":
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

                pilih_kategori = input("Masukkan pilihan: ").lower()
                if pilih_kategori == "0":
                    print("Kembali ke menu utama...\n")
                    lanjut_user = False
                    continue
                elif pilih_kategori == "1":
                    kategori = "makanan"
                    tahap = 1
                elif pilih_kategori == "2":
                    kategori = "minuman"
                    tahap = 1
                else:
                    print("Input tidak valid. Coba lagi.")
                    continue

            elif tahap == 1:
                print("\033[1;31m\n==========================================\033[0m")
                print(f"\033[1;31m||     MENU {kategori.upper()} VENDING ITB          ||\033[0m")
                print("\033[1;31m==========================================\033[0m")

                indeks_barang = [i for i in range(len(barang_array)) if kategori_array[i] == kategori]

                if not indeks_barang:
                    print("Belum ada barang dalam kategori ini.")
                    tahap = 0
                    continue

                for j, i in enumerate(indeks_barang):
                    nama = barang_array[i].ljust(15)
                    harga = f"Rp{harga_array[i]}".rjust(8)
                    stok = f"stok:{stok_array[i]}".rjust(10)
                    baris = f"{j+1}. {nama} {harga} {stok}"
                    print(f"\033[1;31m|| {baris.ljust(38)}||\033[0m")

                print("\033[1;31m==========================================\033[0m")
                print("\033[1;32mKetik 0 untuk kembali ke pilihan kategori.\033[0m")

                inp = input("Masukkan nomor barang yang ingin dibeli: ")
                if not inp.isdigit():
                    print("\033[1;31mMasukkan angka yang valid.\033[0m")
                    continue
                pilihan = int(inp)
                if pilihan == 0:
                    tahap = 0
                    continue
                pilihan -= 1
                if 0 <= pilihan < len(indeks_barang):
                    idx_barang = indeks_barang[pilihan]
                    if stok_array[idx_barang] == 0:
                        print("\033[1;31mMaaf, stok barang tersebut habis.\033[0m")
                        continue
                    else:
                        tahap = 2
                else:
                    print("\033[1;31mNomor tidak valid.\033[0m")
                    continue

            elif tahap == 2:
                idx = idx_barang
                print(f"\033[1;34m\nAnda memilih {barang_array[idx]} seharga Rp{harga_array[idx]} per item\033[0m")
                print(f"\033[1;34mStok tersedia: {stok_array[idx]}\033[0m")
                print("\033[1;32mKetik 0 untuk kembali ke daftar barang.\033[0m")

                jumlah_inp = input("Mau beli berapa? (maksimal 3): ")
                if not jumlah_inp.isdigit():
                    print("Masukkan angka yang valid untuk jumlah.")
                    continue
                jumlah_beli = int(jumlah_inp)
                if jumlah_beli == 0:
                    tahap = 1
                    continue
                elif jumlah_beli < 0 or jumlah_beli > 3:
                    print("Jumlah tidak valid (1–3 saja).")
                    continue
                elif jumlah_beli > stok_array[idx]:
                    print("Stok tidak mencukupi.")
                    continue

                total_harga = harga_array[idx] * jumlah_beli
                print(f"\033[1;34mTotal harga: Rp{total_harga}\033[0m")

                uang_inp = input("Masukkan uang anda (Rp): ")
                if not uang_inp.isdigit():
                    print("Masukkan angka yang valid untuk uang.")
                    continue
                uang = int(uang_inp)
                if uang == 0:
                    tahap = 1
                    continue

                if uang < total_harga:
                    print(f"\033[1;31mGagal, uang anda kurang Rp{total_harga - uang}.\033[0m")
                    tahap = 1
                    continue
                else:
                    kembalian = uang - total_harga
                    stok_array[idx] -= jumlah_beli
                    print(f"\033[1;33mAnda membeli {jumlah_beli} {barang_array[idx]}. Kembalian anda: Rp{kembalian}.\033[0m")
                    print(f"\033[1;33mSisa stok {barang_array[idx]}: {stok_array[idx]}\033[0m")

                ulang = input("Apakah ingin membeli lagi? (y/n): ").lower()
                if ulang == "y":
                    tahap = 0
                else:
                    lanjut_user = False
                    print("\nTerima kasih telah berbelanja di vending machine!\n")
