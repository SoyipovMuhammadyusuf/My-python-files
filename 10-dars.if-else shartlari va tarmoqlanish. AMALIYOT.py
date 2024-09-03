# Sana: 16.03.07.2024
# 10-dars: if-else shartlari va tarmoqlanish
# Muallilf: Muhammadyusuf Soyipov
#                    AMALIYOT

# yangi_cars=["toyato",'mazda','hyundai','gm','kia']

# for cars in yangi_cars:
#    if cars=='gm':
#        print(cars.upper())
#    else:
#            print(cars.title())

# yangi_cars=["toyato",'mazda','hyundai','gm','kia']
# for cars in yangi_cars:
#    if cars!='gm': # gm dan boshqa barchasini barcha harflarini bosh harfga o'zgartiradi
#        print(cars.upper())
#    else:
#            print(cars.title())

# the result
# TOYATO
# MAZDA
# HYUNDAI
# Gm
# KIA

# foydalanuvchi_ismi=input("Ismingizni kiriting \n>>> ")
# if foydalanuvchi_ismi.lower()=="admin":
#    print("Xush kelibsiz.Admin foydalanuvchilar ro'yxatini ko'rishni istaysizmi?")
# else:
#    print("Xush kelibsiz "+foydalanuvchi_ismi)
#    print(f"Xush kelibsiz {foydalanuvchi_ismi} ")

# x=input("1-sonni kiriting\n>>>")
# y=input("2-sonni kiriting\n>>>")
# if x==y:
#  print("Sonlar teng")

# a=int(input("Istalgan sonni kiriting\n... "))
# if a<0:
#    print("Manfiy son")
# else:
#    print("Musbat son")


#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')












