def tambah(a,b):
    return a+b

def kurang(a,b):
    return a-b

def kali(a,b):
    return a*b

def bagi(a,b):
    if b == 0:
        print("Maaf Tidak Dapat dibagi dengan 0")
    else:
        return a/b


while True:
        print("KALKULATOR PROGRAM\n")
        a =int(input("Masukkan angka pertama = "))
        b =int(input("Masukkan angka kedua = "))
           
        print("Pilih Operator\n" \
            "1.Pertambahan\n" \
            "2.Pengurangan\n" \
            "3.Perkalian\n" \
            "4.Pembagian\n" \
            "5.Keluar\n" )
        
        
        pilih =int(input("Masukkan Pilihan Anda 1,2,3,4,5 ="))
    
        if pilih ==1:
            print("Hasil jumlah dari",a, "+" ,b,"=",tambah(a,b))   
        elif pilih ==2:
            print("Hasil kurang dari",a, "-" ,b,"=",kurang(a,b))
        elif pilih ==3:
            print("Hasil kali dari",a, "*" ,b,"=",kali(a,b))
        elif pilih ==4:
            if b==0:
                print("maaf tidak dapat dibagi dengan 0")
            else:
                print("Hasil bagi dari",a, ":" ,b,"=",bagi(a,b))
        elif pilih ==5:
             break
        else:
            print("Data Anda Tidak Valid")
        break