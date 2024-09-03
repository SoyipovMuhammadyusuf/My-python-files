# Sana: 18.08.2024
# 17-dars WHILe Amaliyot
# Dasturchi: Muhammadyusuf Soyipov

print("Mening yoqtirgan kitoblarim:")
savol="\nO'zingiz yoqtirgan kitoblaringizni kiriting"
savol+="(dasturni to'xtatish uchun (stop) deb yozing)\n>>> "
qiymat=''
#while qiymat!='stop':
#    qiymat=input(savol)
#print("dastur tugadi")

print("Muzeyga kirish chipta narxlari:")
savol=("\nYoshingiz nechada?")
savol+=("(dasturni to'xtatish uchun (exit yoki quiet) deb yozing)\n>>> ")
# ishora=True
while True:
    qiymat=input(savol)
    if str(qiymat)=='exit':
        break
    elif str(qiymat)=='quiet':
        break
    elif int(qiymat)<7:
        print("Siz uchun muzeyga kirish narzi 2000 so'm")
    elif int(qiymat)<=18:
        print("Siz uchun muzeyga kirish narzi 3000 so'm")
    elif int(qiymat)<66:
        print("Siz uchun muzeyga kirish narzi 10000 so'm")
    elif int(qiymat)>65:
        print("Siz uchun muzeyga kirish bepul")
print("Dastur tugadi")

print("Kiritilgan sonning ildizini qaytaruvchi dastur.\n")
savol = "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat=input(savol)
    if qiymat=="exit":
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz=float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
print("Dastur tugadi")
