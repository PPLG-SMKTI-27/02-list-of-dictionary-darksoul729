student1 = {'nama' : 'ahmad', 'asal' : 'samarinda', 'nilai' : 90} 
student2 = {'nama' : 'bambang', 'asal' : 'sebulu' , 'nilai' : 75} 
student3 = {'nama' : 'cecep', 'asal' : 'cimahi' , 'nilai' : 66}


students = [student1,student2,student3]
#print(students)

sum = 0
for i in range(len(students)):
    print("Siswa ke-",i,":", students[i]["nama"] , "\n", "\nasal : ", students[i]["asal"], '\n')
    sum = sum + students[i]["nilai"]
print("==== total nilai ketiga siswa adalah", sum, '\n')

#rata rata
ratarata = sum / len(students)
print('==== nilai rata rata siswa adalah', ratarata, "\n")


#CRUD-Create
print("===================================================")
nama = str(input("Masukkan Nama : "))
asal = str(input("Masukkan Asal : "))
nilai = int(input("Masukkan Nilai : "))
student4 = {"nama": nama, "asal": asal, "nilai": nilai}
print()
print("Hasil Create")
students.append(student4)
print(students, "\n")

#CRUD-Read
print("Hasil Read")
print("No\tNama\t\tAsal\t\tNilai")
for i in range(len(students)):
    print(i+1, "     ", students[i]["nama"], "      ", students[i]["asal"], "\t\t", students[i]["nilai"])

print()

print("Nama\tAsal\tNilai")
for s in students :
    print(s["nama"], "\t", s["asal"], "\t", s["nilai"])

