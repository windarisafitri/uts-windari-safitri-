buku = [
 "{0.jago programen, harga : 30000}",
 "{1. jago python, harga :20000}", 
 "{2. jago OOP, harga : 250000}", 
 "{3. Desaign Website, harga : 40000}", 
 "{4. jago JavaScrep, Harga : 35000}"]
a=int(input("pililah, jika beli tekan 1, dan jika ke admin tekan 2 :"))
if a == 1:
    print("selamat datang pada aplikasi penjualan buku pada toko kami")
    print("----------------------------------------------------------")
    b = input("apakah anda mau membeli buku, jika  ya / tidak ? :")
    if b in ["ya", "YA", "Ya"]:
        print("berikut kami tampilkan judul judul buku sebagai berikut :")
        print("========================================================")
        for x in buku:
            print(x)
        pilih = int(input("masukan nomor buku di atas :"))
        if pilih == 0:
            harga = 30000
            print("buku yang anda beli : \n",buku[0])
            print("====================================================")
            tanya =str(input("apakah masih beli buku, jika masi masukan n0mor buku, jika tidak, tuliskan tidak :"))
            if tanya == "1":
                harga = 50000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[0],buku[1])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "2":
                harga = 50000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[0],buku[2])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif  tanya == "3":
                harga = 70000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[0],buku[3])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "4":
                harga = 65000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[0],buku[4])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "5":
                harga = 45000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[0],buku[5])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 30000
                jum = 1
                print("============================================")
                print("buku yang anda beli :",buku[0])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)  
        elif pilih == 1:
            harga = 20000
            print("buku yang anda beli : \n",buku[1])
            print("====================================================")
            tanya =str(input("apakah masih beli buku, jika masih masukan nomor buku, jika tidak, tuliskan tidak :"))
            if tanya == "2":
                harga = 45000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[1],buku[2])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "3":
                harga = 60000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[1],buku[3])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif  tanya == "4":
                harga = 55000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[1],buku[4])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "5":
                harga = 35000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[1],buku[5])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "0":
                harga = 50000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[1],buku[0])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 20000
                jum = 1
                print("============================================")
                print("buku yang anda beli :",buku[1])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
        elif pilih == 2:
            harga = 25000
            print("buku yang anda beli : \n",buku[2])
            print("====================================================")
            tanya =str(input("apakah masih beli buku, jika masih masukan n0mor buku, jika tidak, tuliskan tidak :"))
            if tanya == "3":
                harga = 65000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli ::",buku[2],buku[3])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "4":
                harga = 60000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[2],buku[4])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif  tanya == "5":
                harga = 40000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[2],buku[5])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "0":
                harga = 55000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[2],buku[0])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "1":
                harga = 45000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[2],buku[1])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 25000
                jum = 1
                print("============================================")
                print("buku yang anda beli :",buku[2])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
        elif pilih == 3:
            harga = 40000
            print("buku yang anda beli : \n",buku[3])
            print("====================================================")
            tanya =str(input("apakah masih beli buku, jika masih masukan n0mor buku, jika tidak, tuliskan tidak :"))
            if tanya == "4":
                harga = 35000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[3],buku[4])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "5":
                harga = 55000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[3],buku[5])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif  tanya == "0":
                harga = 60000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[3],buku[0])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "1":
                harga = 60000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[3],buku[1])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "2":
                harga = 65000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[3],buku[2])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 40000
                jum = 1
                print("============================================")
                print("buku yang anda beli :",buku[3])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
        elif pilih == 4:
            harga = 35000
            print("buku yang anda beli : \n",buku[4])
            print("====================================================")
            tanya =str(input("apakah masih beli buku, jika masih masukan nomor buku, jika tidan, tuliskan tidak :"))
            if tanya == "5":
                harga = 50000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[4],buku[5])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "0":
                harga = 65000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[4],buku[0])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif  tanya == "1":
                harga = 55000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[4],buku[1])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "2":
                harga = 55000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[4],buku[2])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "3":
                harga = 75000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[4],buku[3])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 35000
                jum = 1
                print("============================================")
                print("buku yang anda beli :",buku[4])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
        elif pilih == 5:
            harga = 15000
            print("buku yang anda beli : \n",buku[5])
            print("====================================================")
            tanya =str(input("apakah masih beli buku, jika masih masukan nomor buku, jika tidan, tuliskan tidak :"))
            if tanya == "0":
                harga = 45000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[5],buku[0])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "1":
                harga = 45000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[5],buku[1])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif  tanya == "2":
                harga = 40000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[5],buku[2])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "3":
                harga = 55000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[5],buku[3])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "4":
                harga = 50000
                jum = 2
                print("============================================")
                print("di batasi pembelian buku maxsimal dua buku ")
                print("buku yang anda beli :",buku[5],buku[4])
                print("============================================")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 15000
                jum = 1
                print("============================================")
                print("buku yang anda beli :",buku[5])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            else:
                print("nomor yang anda masukan salah")
        else:
            print("angka yang anda masukan tidak tercantum dalah nomor buku")
            print("silahkan mulai kembali!")
elif a == 2:
    print("selamat datang admin pada aplikasi penjualan buku  pada Toko sejahtra")
    print("--------------------------------------------------------------------")
    print("stok buku")
    print(buku)
    print("===================================================================")
    print("jikan menambah tekan 1, dan jika menghapus tekan 2")
    pilih = int(input("masukan pilihan :"))
    if pilih == 1:
        print("anda menambahkan stok buku, dengan format ikuti di bawah ini")
        print("{nomor selanjutnya. nama buku, harga : diisi}")
        stok = str(input("masukan stok : "))
        buku.append(stok)
        print(buku)
    elif pilih == 2:
        print("anda ingin menghapus stok yang telah habis ? ")
        print("pililah nomor buku yang ingin anda hapus")
        stok = int(input ("masukan nomor :"))
        del buku[stok]
        print(buku)