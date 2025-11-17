pin_transaksi = "1013"
salah = 0
percobaan = 3
while salah < percobaan :
    pin = input("masukkan pin anda = ")
    if pin == pin_transaksi:
        while True:
             print("=== daftar film ===")
             print("1.AAOU = Rp75000")
             print("2.IM = Rp80000 ")
             print("3.AIW = Rp85000")
             print("4.AE = Rp90000")
             pilih = input("pilihan anda 1/2/3/4 = ")
             if pilih == "1":
                harga = 75000 
                film = "AAOU"
             elif pilih == "2":
                  harga = 80000 
                  film = "IM"
             elif pilih == "3":
                  harga = 85000 
                  film = "AIW"
             elif pilih == "4":
                  harga = 90000 
                  film = "AE"
             else :
                  print("pilihan tak tersedia! pilih 1-4.") 
                  continue

             jumlah_tiket = int(input("masukkan jumlah tiket anda = "))
             total_transaksi = jumlah_tiket * harga
             print(f"film = {film}")
             print(f"jumlah tiket = {jumlah_tiket}")
             print(f"total transaksi anda = Rp{total_transaksi}")

             ulang = input("ingin memesan lagi? (ya/tidak): ").lower()
             if ulang != "ya":
                print("terima kasih telah memesan!")
                print("selamat menonton!")
                break 
        break 
    else:
     salah += 1
     print(f"pin salah! kesempatan tersisa = {percobaan - salah}")

if salah == percobaan:
   print("kesempatan anda habis.")
    

    


