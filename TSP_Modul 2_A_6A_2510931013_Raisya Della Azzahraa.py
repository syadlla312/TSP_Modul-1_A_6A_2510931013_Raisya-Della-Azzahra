Nama = input("masukkan nama = ")
Nim = input("masukkan nim = ")
Kelompok = input("masukkan kelompok = ")
Asisten_Pembimbing = input("masukkan asisten pembimbing = ")

nim = int(input ("masukkkan 4 digit terakhir nim = "))
ABC = int(input ("3 digit nim sebelum akhir = "))
D = int(input ("1 digit terakhir nim = "))

Silver = 1-4
Gold = 5-7
Platinum = 8-9
Non_Member = 0

if 1 <= D <= 4 :
    membership = "Silver"
    diskon = 5/100
elif 5 <=  D <= 7 :
   membership = "Gold"
   diskon =  10/100
elif 8 <= D <= 9 :
    membership = "Platinum"
    diskon = 15/100
else :
    membership = "Non-Member"
    diskon = 0/100

print(" ")
print("pilih metode pembayaran")
print("1. Tunai")
print("2. QRIS")
print("3. Debit")
pilihan = int(input("masukkan pilihan (1/2/3) = "))

if pilihan == 1 :
    metode = "Tunai"
    biaya_tambahan = 0
elif pilihan == 2 :
    metode = "QRIS"
    biaya_tambahan = 2500
elif pilihan == 3 :
    metode = "Debit"
    biaya_tambahan = 5000
else :
    metode = "Tidak valid"
    biaya_tambahan = 0

total_belanja = ABC * 1000
besar_diskon = total_belanja * diskon
setelah_diskon =total_belanja - besar_diskon
total_akhir = setelah_diskon + biaya_tambahan

print(" ")
print("== Struk Pembayaran ==")
print("total belanja = Rp", total_belanja)
print("membership = ", membership)
print("diskon = ", besar_diskon )
print("setelah diskon = ",setelah_diskon)
print("metode pembayaran = ", metode)
print("biaya tambahan = ", biaya_tambahan)
print("total yang dibayar = ", total_akhir)







