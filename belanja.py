totalBelanja = int(input("Total belanja: Rp."))
# jumlah yang harus dibayar adalah berapa total belanjanya
# tapi kalau dapat diskon berkurang
bayar = totalBelanja

# jika dia belanja diatas 100rb maka berikan bonus dan diskon
if totalBelanja > 100000:
    print("kamu mendapatkan bonus minuman dingin\ndan diskon 5%")

    # hitung diskonnya
    diskon = totalBelanja * 5/100 # 5%
    bayar = totalBelanja - diskon

# cetak struk
print("total yang harus dibayar: Rp." , bayar)
print("Terima kasih sudah berbelanja!")
print("Datang kembali!")