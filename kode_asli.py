# program nilai
import math

def hitung(a,b,c,d):
    # hitung nilai
    x = a*0.2
    y = b*0.3
    z = c*0.2
    w = d*0.3
    hasil = x+y+z+w
    return hasil

def cek(n):
    if n>=80:
        h="A"
    elif n>=70:
        h="B"
    elif n>=60:
        h="C"
    elif n>=50:
        h="D"
    else:
        h="E"
    return h

def tampil(nm,np,grade):
    print("Nama: "+nm)
    print("Nilai: "+str(np))
    print("Grade: "+grade)
    print("----------")

def proses(data):
    # proses semua data mahasiswa dan tampilkan
    for i in range(len(data)):
        nm = data[i][0]
        a = data[i][1]
        b = data[i][2]
        c = data[i][3]
        d = data[i][4]
        x = a*0.2
        y = b*0.3
        z = c*0.2
        w = d*0.3
        hasil = x+y+z+w
        if hasil>=80:
            h="A"
        elif hasil>=70:
            h="B"
        elif hasil>=60:
            h="C"
        elif hasil>=50:
            h="D"
        else:
            h="E"
        print("Nama: "+nm)
        print("Nilai: "+str(hasil))
        print("Grade: "+h)
        print("----------")

# main
d = [
    ["Robi", 80, 75, 90, 85],
    ["Ganjaro", 60, 55, 70, 65],
    ["Ben", 90, 95, 88, 92],
    ["Deri", 45, 50, 40, 48],
]

print("=== HASIL NILAI MAHASISWA ===")
proses(d)

total=0
for i in range(len(d)):
    a=d[i][1]; b=d[i][2]; c=d[i][3]; e=d[i][4]
    total=total+(a*0.2+b*0.3+c*0.2+e*0.3)
print("Rata-rata kelas: "+str(total/len(d)))