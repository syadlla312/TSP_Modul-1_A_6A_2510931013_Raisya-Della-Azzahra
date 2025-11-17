class KontakLSIK:
    def __init__(self, kode = " ", nama_kontak = " ", no_telp = " ", email = " "):
        self.kode = kode
        self.nama_kontak = nama_kontak
        self.no_telp = no_telp
        self.email = email

    def tampilkan_data(self):
        print(f"KontakLsik = {self.kode},{self.nama_kontak}, {self.no_telp}, {self.email}")

    def inisialisasi(self):
        self.daftar_kontak = [ ]

    def tambah_data_awal(self):
        self.daftar_kontak = [
            KontakLSIK("C01", "Ahmad Dahlan", "081234567890", "Ahmad@mail.com"),
            KontakLSIK("C02", "Susi Susanti", "081298765432", "Susi@mail.com"),
            KontakLSIK("C03", "Dewi Kartika", "082143658709", "Dewi@mail.com"),
            KontakLSIK("C04", "Arya Putra", "082189674523", "Arya@mail.com")
        ]

    def buat_kode_baru(self):
        return "C" + str(len(self.daftar_kontak) + 1)

    def tambah_kontak(self):
        print("=== Menambah Kontak Baru ===")
        nama_baru= input("Nama Kontak = ")
        notelp_baru = input("No Telp = ")
        mail_baru = input("Email = ")
        kode_baru = self.buat_kode_baru()
        baru = KontakLSIK(kode_baru,nama_baru, notelp_baru, mail_baru)
        self.daftar_kontak = self.daftar_kontak + [baru] 
        print(f"Kontak baru ditambahkan: {kode_baru}")

    def hapus_kontak(self):
        print("=== Menghapus Kontak ===")
        kode_hapus = input("Kontak yang ingin dihapus berdasarkan kode = ").upper()
        baru_daftar = []
        terhapus = False
        for k in self.daftar_kontak:
            if k.kode != kode_hapus:
                baru_daftar.append(k)
            else:
                terhapus = True
        self.daftar_kontak = baru_daftar
        if terhapus:
            print(f"Kontak {kode_hapus} berhasil dihapus")
        else:
            print("Kode tidak ditemukan")

    def tampilkan_semua(self):
        print("\nDaftar Kontak saat ini :")
        for k in self.daftar_kontak:
            k.tampilkan_data()

    def cari_nama(self):
        print("=== Mencari Kontak Berdasarkan Nama ===")
        cari = input("Masukkan nama yang dicari = ").lower()
        hasil = [k for k in self.daftar_kontak if cari in k.nama_kontak.lower()]
        if hasil:
            for k in hasil:
                k.tampilkan_data()
        else:
            print("Nama Tidak Ada")

kontak = KontakLSIK()
kontak.inisialisasi()
kontak.tambah_data_awal()

while True:
    print("\n=== Pilihan Untuk Pengelolaan ===")
    print("1. Menampilkan daftar kontak saat ini")
    print("2. Menambah kontak baru (kode berurut otomatis)")
    print("3. Menghapus kontak berdasarkan kode ")
    print("4. Menampilkan daftar kontak setelah perubahan")
    print("5. Mencari kontak berdasarkan nama")
    print("6. Keluar.")

    pilihan = input("pilih menu (1-6) = ")

    if pilihan == "1":
        kontak.tampilkan_semua()
    elif pilihan == "2":
        kontak.tambah_kontak()
    elif pilihan == "3":
        kontak.hapus_kontak()
    elif pilihan == "4":
        kontak.tampilkan_semua()
    elif pilihan == "5":
        kontak.cari_nama()
    elif pilihan == "6":
        print("Program Selesai.")
        break

    else:
        print("Pilihan tidak valid! pilihan hanya 1-6.")