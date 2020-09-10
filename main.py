import os, platform
from customer import Customer
from time import sleep # modul sleep digunakan untuk membuat delay

def judul():
  print("🏦 Selamat Datang di ATM Progate 🏦\n")

# hapus history
def hapus_history():
  # jika OS UNIX atau GNU/Linux atau MacOS, perinah hapus layarnya pake 'clear'
  if platform.system() == 'Darwin' or platform.system() == 'Linux':
    os.system('clear')
  # kalau engga mereka, ya windows, cls :D
  else:
    os.system('cls')

# garis
def garis():
  print("\n==============================\n")

# loading. menerima satu param
def loading(teks):
  print("\n⏳ "+teks+"\n")
  sleep(3) # membuat delay 3 detik

# instance object
atm = Customer()

while True:
  hapus_history()
  judul()
  # 'percobaan' jika salah input PIN
  percobaan = 0
  pin = int(input('Masukkan nomor PIN: '))
  while(pin != int(atm.cek_pin()) and percobaan < 3):
    print("PIN Anda salah!")
    pin = int(input('Masukkan PIN lagi: '))
    percobaan += 1

    # karena percobaan dimulai dai 0 maka sampai 2 (total 3 kali)
    if percobaan == 2:
      print("ERROR")
      print("Anda telah memasukkan PIN salah sebanyak 3 kali")
      exit()

  hapus_history()
  while True:
    judul()
    print("1 Cek Saldo")
    print("2 Debet")
    print("3 Stor Tunai")
    print("4 Ubah PIN")
    print("5 Selesai")

    pilih = input("Pilih menu nomor 1/2/3/4/5: ")

    if pilih == '1':
      hapus_history()
      print("Saldo Anda:",atm.cek_balance())
      garis()
      
    elif pilih == '2':
      hapus_history()
      print("Ambil uang")
      nominal = float(input("Masukkan nominal Rp"))
      confirm = input('Anda akan melakukan debet Rp'+str(nominal)+' (y/t) ')
      if confirm.lower() == 'y':
        if nominal < atm.cek_balance():
          saldo = atm.debet(nominal)
          loading("Tunggu sebentar...")
          print("Silakan ambil uang Anda")
          garis()
        else:
          loading("Tunggu sebentar...")
          print("😔 Maaf saldo Anda tidak mencukupi")
          print("Saldo Anda saat ini Rp"+str(atm.cek_balance()))
          print("Silakan lakukan penambahan saldo minimal 💰")
          garis()
      else:
        break

    elif pilih == '3':
      hapus_history()
      print("Stor Tunai")
      nominal = float(input("Masukkan nominal Rp"))
      confirm = input('Lanjutkan stor tunai Rp'+str(nominal)+' (y/t) ')
      if confirm.lower() == 'y':
        saldo = atm.stor_tunai(nominal)
        loading("Tunggu sebentar...")
        print("Anda berhasil melakukan Stor Tunai sebanyak Rp",nominal)
      else:
        print("\n⚠️  Anda membatalkan proses Stor Tunai")
        print("💵 Silakan ambil kembali uang Anda")
      garis()

    elif pilih == '4':
      hapus_history()
      print("Ubah PIN")
      # masukkan dulu current PIN (pin saat ini)
      cur_pin = int(input("Masukkan PIN Anda saat ini: "))
      while cur_pin != atm.cek_pin(): # selama PIN yang dimasukkan tidak sama maka akan terus ngulang
        print("🙅🏻‍♂️ PIN Anda salah")
        cur_pin = int(input("Silakan masukkan kembali PIN Anda: "))
      # buat PIN baru
      print("\n🔢 Membuat PIN Baru 🔢")
      new_pin     = int(input("Masukkan PIN baru  : "))
      confirm_pin = int(input("Konfirmasi PIN baru: "))
      while new_pin != confirm_pin:   # konfirmasi PIN harus sama dengan PIN baru (new_pin == confirm_pin)
        print("Konfirmasi PIN salah")
        confirm_pin = int(input("Masukkan kembali Konfirmasi PIN baru: "))
        
      # jika PIN baru berhasil dikonfirmasi, maka simpan
      if new_pin == confirm_pin:
        confirm = input('Apakah Anda yakin ingin mengubah PIN dengan yang baru? (y/t) ')
        if confirm.lower() == 'y':
          loading("💾 Sedang menyimpan PIN baru...")
          atm.pin = new_pin # simpan PIN baru ke instance var di kelas ATMCard
          print("✅ PIN baru telah disimpan.")
          loading("Tunggu sebentar Anda akan diminta masuk kembali...")
          sleep(3)
          break
        else:
          print("\n⚠️  Proses perubahan PIN dibatalkan...")
          sleep(3)
      garis()
      hapus_history()

    elif pilih == '5':
      print("Selesai.")
      exit()

    else:
      hapus_history()
      print("Tidak ada menu nomor",pilih)
      garis()
  
  