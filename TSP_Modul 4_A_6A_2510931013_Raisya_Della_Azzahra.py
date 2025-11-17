nama = ["One Ok Rock", "Stray Kids", "Feast", "One Direction (Reborn)", "Kendrick Lamar"]
agency = ["United Talent Agency (UTA)", "JYP Entertainment", "Rusa Record", "Syco Music", "Wasserman Music" ]
asal_negara = ["Jepang", "Korea Selatan", "Indonesia", "Inggris", "USA"]
fee_biaya_tampil = ["150000", "400000", "10000", "1500000 ", "750000 "]
hit_single =  ["Stand Out Fit In", "Maniac ", "Peradaban", "What Make You Beautiful ", "Humble "]
durasi_kontrak = [" 14 ", " 15", " 16 ", " 15 ", " 14 "]

pilihan = 0

while pilihan != 9:
     print("\n=== Daftar Awal Band ===")
     print("1. Menampilkan daftar artis & band awal. ")
     print("2. Menambahkan artis atau band baru ke daftar.")
     print("3. Menghapus artis atau band dari daftar.")
     print("4. Mengubah Fee (Biaya Tampil) atau durasi kontrak artis tertentu")
     print("5. Menghitung total estimasi biaya kontrak seluruh artis")
     print("6. Menghitung rata-rata Fee (Biaya Tampil) dari seluruh artis.")
     print("7. Menghitung pendapatan bersih setelah pajak")
     print("8. Menampilkan daftar artis & band setelah dilakukan perubahan")

     pilihan = int(input("\nPilih Menu (1-8) = "))

     if pilihan == 1:
          print("\n=== Menampilkan Daftar Awal Band ===")
          for i in range(len(nama)):
            print((f"{i+1}. {nama[i]} | {agency [i]} | {asal_negara[i]} | Fee : ${fee_biaya_tampil[i]} | Hit Single : {hit_single[i]} | Durasi:  {durasi_kontrak[i]} hari | "))
    
     elif pilihan == 2:
          print("\n=== Menambahkan artis atau band baru ke daftar ===")
          nama.append(input("nama = "))
          agency.append(input("agency = "))
          asal_negara.append(input("asal_negara = "))
          fee_biaya_tampil.append(input("fee_biaya_tampil = "))
          hit_single.append(input("hit_single = "))
          durasi_kontrak.append(input("durasi_kontrak = "))
          print("Artis atau Band baru berhasil ditambahkan!")
      
     elif pilihan == 3:
          print("\n=== Menghapus artis atau Band dari daftar ===")
          cari = input("Masukkan artis atau Band yang ingin dihapus = ")
          if cari in nama:
           index = nama.index(cari)
           del nama[index]              
           del agency[index]            
           del asal_negara[index]      
           del fee_biaya_tampil[index]  
           del hit_single[index]       
           del durasi_kontrak[index]    
           print("Artis atau Band berhasil dihapus!")

     elif pilihan == 4:
           print("\n=== Mengubah Fee atau Durasi Kontrak ===")
           cari = input("Masukkan nama artis atau band yang ingin diubah = ")
           if cari in nama:
            index = nama.index(cari)
            print(f"Data ditemukan: {nama[index]}")
            print("1. Ubah Fee (Biaya Tampil)")
            print("2. Ubah Durasi Kontrak")
            ubah = int(input("Pilih menu (1/2): "))
            if ubah == 1:
                fee_baru = (input("Masukkan Fee baru = "))
                fee_biaya_tampil[index] = fee_baru
                print("Fee berhasil diubah!")
            elif ubah == 2:
                durasi_baru = int(input("Masukkan Durasi Kontrak baru (hari) = "))
                durasi_kontrak[index] = durasi_baru
                print("Durasi kontrak berhasil diubah!")
            else:
                print("Artis atau band tidak ditemukan!")

     elif pilihan == 5:
         print("\n=== Menghitung total estimasi biaya kontrak seluruh artis ===")
         estimasi_biaya = [int(fee_biaya_tampil[i]) * int(durasi_kontrak[i]) for i in range(len(nama))]
         total = sum(estimasi_biaya)
         print(f"\nTotal estimasi biaya kontrak seluruh artis = ${total:,}")  

     elif pilihan == 6:
        print("\n=== Menghitung rata-rata Fee (Biaya Tampil) dari seluruh artis ===")
        total_int = [int(fee.strip()) for fee in fee_biaya_tampil] 
        rata_fee = sum(total_int) / len(total_int)
        print(f"\nRata-rata Fee (Biaya Tampil) dari seluruh artis = ${rata_fee:.2f}")

     elif pilihan == 7:
        print("\n=== Menghitung pendapatan bersih setelah pajak ===")
        total_bersih = 0
        if not nama:  
            print("\nTidak ada artis untuk dihitung!")
        else:
            for i in range(len(nama)):
                fee = int(fee_biaya_tampil[i])
                durasi = int(durasi_kontrak[i])
                fee_total = fee * durasi  
                if asal_negara[i].lower() == "indonesia":
                    pajak = 0.08
                else:
                    pajak = 0.18
                bersih = fee_total - (fee_total * pajak)
                total_bersih += bersih
                print(f"\n{nama[i]} - Fee Total: ${fee_total:,} | Pendapatan Bersih: ${bersih:.2f}")
            print(f"\nTotal pendapatan bersih setelah pajak = ${total_bersih:.2f}")

     elif pilihan == 8:
          print("\n=== Daftar Artis & Band Setelah Perubahan ===")
          for i in range(len(nama)):
            print(f"{i+1}. {nama[i]} | {agency[i]} | {asal_negara[i]} | Fee: ${fee_biaya_tampil[i]} | Hit Single: {hit_single[i]} | Durasi: {durasi_kontrak[i]} hari")

     elif pilihan == 9:
          print("\nProgram selesai. Terima kasih.")
          break

     else:
          print("Pilihan tidak valid, silakan coba lagi.")

              
                   
     
           