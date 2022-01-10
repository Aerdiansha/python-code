id = []
nama = []
jabatan =[]
gaji =[]
tunjangan = []

pilihan = 1
while pilihan != 0 :
    print ("1. tampilan data.")
    print ("2. tambah data.")
    print ("3. hapus data.")
    print ("0. exit.")

    pilihan = int(input("masukan pilihan anda : "))
    print('')
    print('')
    print('')
    if pilihan == 1:
        masid = input("masukan id : ")
        id.append({'id' : masid})
        masnama = input("masukan nama : ")
        nama.append({'nama' : masnama})
        masjabatan = input("masukan jabatan :")
        jabatan.append({'jabatan' : masjabatan})
        masgaji = input("masukan gaji :")
        gaji.append({'gaji' : masgaji})
        mastunjangan = input("masukan tunjangan : ")
        tunjangan.append({'asal' : mastunjangan})
        
        
    elif pilihan == 2 :
        penentu = True
        for i in range (len(id)) :
            if penentu :
                print ("id\tnama\tjabatan\tgaji\ttunjangan")
            print (id[i],['id'],'\t',nama[i],['nama'],'\t',jabatan[i],['jabatan'],'\t',gaji[i],['gaji'],'\t',tunjangan[i],['tunjangan'])
            penentu = False
            
    elif pilihan == 3 :
        masnim = input("masukan id : ")
        for i in range (len(id)) :
            if masid == id[i]['id'] :
                print (i)
                del id[i]
                del nama[i]
                del jabatan[i]
                del gaji[i]
                del tunjangan[i]
                break
    print('')
    print('')
    print('')