Nama = (str(input("Masukkan Nama = ")))
Nim = (str(input("Masukkan Nim = ")))
Kelompok = (str(input("Masukkan Kelompok = ")))
Asisten_Pembimbing = (str(input("Masukkan Asisten Pembimbing = ")))

#pemakaian kWh dibulan 1 & 2
AB = int(input("masukkan nilai AB = "))
CD = int(input("masukkan nilai CD = "))

#data yang diketahui
biaya_energi1 = 1500
biaya_energi2 = 1500
biaya_beban1 = 20000
biaya_beban2 = 20000

#rumus mencari 
total_pemakaian = AB + CD
biaya_energi1 = 1500 * AB
biaya_energi2 = 1500 * CD
total_biaya_energi = biaya_energi1 + biaya_energi2
biaya_pajak1 = biaya_energi1 * 5/100 
biaya_pajak2 = biaya_energi2 * 5/100
total_biaya_pajak = biaya_pajak1 + biaya_pajak2
total_biaya_beban = biaya_beban1 + biaya_beban2
total_biaya_administrasi = 2/100 * total_biaya_energi + total_biaya_pajak + total_biaya_beban
total_tagihan = total_biaya_energi + total_biaya_pajak + total_biaya_beban + total_biaya_administrasi

#output yang akan dihasilkan
print(f"total pemakaian kWh adalah = {total_pemakaian}")
print(f"biaya energi pada masing masing bulan adalah = {biaya_energi1} dan {biaya_energi2}")
print(f"biaya energi 2 bulan tanpa pajak dan administrasi = {total_biaya_energi}")
print(f"biaya pajak 2 bulan = {biaya_pajak1} dan {biaya_pajak2}")
print(f"biaya beban 2 bulan = {total_biaya_beban}")
print(f"biaya administrasi ke2 bulan = {total_biaya_administrasi}")
print(f"total biaya tagihan kedua bulan {total_tagihan}")


