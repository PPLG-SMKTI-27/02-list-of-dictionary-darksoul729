from tabulate import tabulate

item1 = {"nama" : "router huawei", "stok" : 10 , "harga" : 1000}
item2 = {"nama" : "orbit telkomsel", "stok" : 9 , "harga" : 90000}
item3 = {"nama" : "simcard xl", "stok" : 3 , "harga" : 25000}
item4 = {"nama" : "adapter usb to type c", "stok" : 5 , "harga" : 5000}
item5 = {"nama" : "airpods", "stok" : 7 , "harga" : 278000}

items = [item1,item2,item3,item4,item5]

#fungsi read menggunakan for
for i in range(len(items)):
    print("Barang ke-",1+i,":", items[i]["nama"] , "\nstok : ", items[i]["stok"], '\n', "harga : ", items[i]["harga"], "\n")

#fungsi create 

nama = str(input("Masukkan Nama Barang : "))
stok = int(input("Masukkan Jumlah Barang : "))
harga = int(input("Masukkan Harga Barang : "))
barang_baru = {"nama" : nama, "stok" : stok , "harga" : harga}
items.append(barang_baru)
print(tabulate(items, headers="firstrow", tablefmt="grid"))



