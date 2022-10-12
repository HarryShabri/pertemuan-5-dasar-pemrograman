print('''
   GEROBAK FRIED CHICKEN
----------------------------------------
|| Kode ||  Jenis potong    ||  Harga ||
---------------------------------------- 
||   1  ||   Dada           || Rp2500 ||
||   2  ||   Paha           || Rp2000 ||
||   3  ||   Sayap          || Rp1500 ||
----------------------------------------
''')
nota =[]
bayar_pajak = []
jh = []
total_bayar = []
harga_satuan = int()
jumlah_harga = int()
banyak_pembelian = int(input("Banyak jenis :"))
for i in range(banyak_pembelian):
    if banyak_pembelian == 0:
        print("Menu tidak tersedia")
        break
    elif banyak_pembelian >3:
        print("Menu tidak tersedia")
        break
    pembelian = print("jenis ke - "+str(i+1))
    jenis_potong = int(input("Kode potong[1,2,3] : "))
    if jenis_potong == 1:
        merk = ("Dada")
        harga_satuan = 2500
    elif jenis_potong == 2:
        merk = ("Paha")
        harga_satuan = 2000
    elif jenis_potong == 3:
        merk = ("Sayap")
        harga_satuan = 1500   
    else:
        print("jenis potong tidak tersedia")
    banyak_beli = int(input("Banyak potong : "))
    jumlah_harga = harga_satuan*banyak_beli
    pajak = 0.1*jumlah_harga
    data = ("%i       %s          Rp%i            %i              Rp%i"%(jenis_potong,merk,harga_satuan,banyak_beli,jumlah_harga))
    nota.append(data)
    jh.append(jumlah_harga)
    bayar_pajak.append(pajak)
    total_bayar.append(jumlah_harga+pajak)
if banyak_pembelian ==1:
    print('''
GEROBAK FRIED CHICKEN
-----------------------------------------------------------------
No | Jenis potong |  harga satuan  | banyak beli | jumlah harga |
-----------------------------------------------------------------
''')
    print(nota[0])
    jb = jh[0]
    bayar_pajak = bayar_pajak[0]
    total_bayar = total_bayar[0]
    print('''    
-----------------------------------------------------------------
''')
elif banyak_pembelian == 2:
    print('''
GEROBAK FRIED CHICKEN
-----------------------------------------------------------------
No | Jenis potong |  harga satuan  | banyak beli | jumlah harga |
-----------------------------------------------------------------
''')
    print(nota[0])
    print(nota[1])
    jb = jh[0]+jh[1]
    bayar_pajak = bayar_pajak[0]+bayar_pajak[1]
    total_bayar = total_bayar[0]+total_bayar[1]
    print('''
-----------------------------------------------------------------
''')
elif banyak_pembelian == 3:
    print('''
GEROBAK FRIED CHICKEN
-----------------------------------------------------------------
No | Jenis potong |  harga satuan  | banyak beli | jumlah harga |
-----------------------------------------------------------------
''')
    print(nota[0])
    print(nota[1])
    print(nota[2])
    jb = jh[0]+jh[1]+jh[2]
    bayar_pajak = bayar_pajak[0]+bayar_pajak[1]+bayar_pajak[2]
    total_bayar= total_bayar[0]+total_bayar[1]+total_bayar[2]
    print('''
-----------------------------------------------------------------
''')
else:
    print("Nota tidak akan tampii")
print("                            Jumlah Bayar : Rp", jb)
print('''                            Pajak        : Rp''',bayar_pajak)
print('''                            Total bayar  : Rp''',total_bayar)