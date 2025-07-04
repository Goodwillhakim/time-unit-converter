print("=" *41)
print("          Konversi Satuan Waktu")
print("=" *41)
print("1.Jam")
print("2.Menit")
print("3.Detik")

Pilihan = input ("Pilih Satuan Awal (1/2/3:) ")
if Pilihan == '1' :
  try :      
    Jam = float(input("Masukan Total Jam: "))
    Menit = Jam * 60
    Detik = Jam * 3600
    print(f"Hasilnya {Jam} jam sama dengan {Menit} menit dan {Detik} detik")
  except ValueError:
        print("Error")
elif Pilihan == '2' :
 try  :
    Menit = float(input("Masukan Total Menit: "))
    Jam = Menit / 60
    Detik = Menit * 60
    print(f"Hasilnya {Menit} menit sama dengan {Jam} jam dan {Detik} detik")
 except ValueError :
     print("Error")   
elif Pilihan == '3' :
 try :
     Detik = float(input("Masukan Total Detik: "))
     Menit = Detik / 60
     Jam = Detik / 3600
     print(f"Hasilnya {Detik} detik sama dengan {Menit} menit dan {Jam} jam")
 except ValueError :
     print("Error")
else :
     print("Masukan Pilihan Yang Benar")