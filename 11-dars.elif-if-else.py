# Sana:17.07.2024
# 11-dars. Bir nechta shartlarni tekshirish
#                 elif-if-else
# Dasturchi: Muhammadyusuf Soyipov

# son=50
# if son<0:
#    print("Manfiy son")
# else:
#    print("Musbat son")

# # # elif operatori if dan 2 va undan ko'p ishlatganimizda kerak
# # # biz elif operatorini istalgancha ishlata olamiz

# yosh=int(input("Yoshingiz nechada?\n>>> "))
# if yosh<=4:
#    print("Siz uchun kirish bepul, marhamat")
# elif yosh <=10:
#   print("Siz uchun kirish narxi 5000 so'm")
# else:
#    print("Siz uchun kirish narxi 10000 so'm")

# yosh=int(input("Yoshingiz nechada?\n>>> "))
# if yosh<=4:
#    print("Siz uchun kirish bepul, marhamat")
# elif yosh <=10:
#   print("Siz uchun kirish narxi 5000 so'm")
# elif yosh<=15:
#    print("Siz uchun kirish narxi 8000 so'm")
# else:
#    print("Siz uchun kirish narxi 10000 so'm")

# yosh=int(input("Yoshingiz nechada?\n>>> "))
# if yosh<=4:
#   narh=0
# elif yosh<=10:
#   narh=5000
# elif yosh<=15:
#    narh=8000
# else:
#    narh=10000
# print(f"Siz uchun kirish narxi {narh} so'm")

# # # or funksiyasi esa if dan ko'proq narsani bajarishda ishlatamiz
# # # huddi ifdan 2-marotaba ishlatayotganday
# # # or bu fuksiya bitta variant tog'ri bo'lganda ham ishlaydi

# kun=input("Bugun haftaning qaysi kuni?\n>>> ")
# if kun.lower()=="shanba" or kun.lower()=="yakshanba":
#    print("Bugun dam olish kuni")
# else:
#    print("Bugun ish kuni")
    
# kun=input("Bugun haftaning qaysi kuni?\n>>> ")
# harorat=float(input("Bugun havo harorati qanday?\n>>> "))

# if kun.lower()=="yakshanba" and harorat>=30:
#    print("Qani cho'milgani ketdik!")
# elif kun.lower()=="yakshanba" and harorat<30:
#    print("Bugun uyda dam olamiz")

# kun=input("Bugun haftaning qaysi kuni?\n>>> ")
# harorat=float(input("Bugun havo harorati qanday?\n>>> "))

# # # and 2 ta so'rovni birlashtirishda ishlatiladi
# # # and ning or funksiysidan farqi 
# # # and faqat ikkala so'rov ham true qiymat qaytarganda ishlaydi

# if kun.lower()=="yakshanba" and harorat>=30:
#    print("Qani cho'milgani ketdik!")
# elif kun.lower()=="yakshanba" and harorat<30:
#    print("Bugun uyda dam olamiz")
    
# kun=input("Bugun haftaning qaysi kuni?\n>>> ")
# harorat=float(input("Bugun havo harorati qanday?\n>>> "))
# if (kun.lower()=="yakshanba" or kun.lower()=="shanba") and harorat>=30:
#    print("Qani cho'milgani ketdik!")
# elif (kun.lower()=="yakshanba" or kun.lower()=="shanba") and harorat<30:
#    print("Bugun uyda dam olamiz")

# narh=15000 # mijoz 15000 so'mlik taom oldi
# choy=True # mijoz choy oldi
# salat=False # mijoz salat olmadi

# if choy and salat: # agar mijoz choy va salt olgan bo'lsa
#   narh=narh+10000
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#   narh=narh+5000
# print(f"Jami harid {narh} so'm")

# false o'rniga 0 dan
# true o'rniga 1 dan foydalana olamiz

# narh=15000
# non=1
# choy=1
# salat=0
# kompot=1
# choy_chaqa=0

# Quyidagi har bir shart tekshiladi va ular bir biriga bog'liq emas

# if non:
#    print("Mijoz non oldi")
#    narh=narh+2500

#if choy:
#    print("Mijoz choy oldi")
#    narh=narh+3000

#if salat:
#    print("Mijoz salat oldi")
#    narh=narh+4000

# if kompot:
#    print("Mijoz kompot oldi")
#    narh=narh+7000

# if choy_chaqa:
#    print("Mijoz choy chaqa berdi")
#    narh=narh+1000
# print(f"Mijoz {narh} so'mlik harid qildi")

# narh=15000
# non=1
# choy=1
# salat=0
# kompot=1
# choy_chaqa=0

# Quyidagi har bir shart tekshiladi va ular bir biriga bog'liq emas

# if non:
#    print("Mijoz non oldi")
#    narh=narh+2500
# else:
#    print('Mijoz non olmadi')

# if choy:
#    print("Mijoz choy oldi")
#    narh=narh+3000
# else:
#    print("Mijoz choy olmadi")

# if salat:
#    print("Mijoz salat oldi")
#    narh=narh+4000
# else:
#    print("Mijoz salat olmadi")

# if kompot:
#    print("Mijoz kompot oldi")
#    narh=narh+7000
# else:
#    print("Mijoz kompot olmadi")

# if choy_chaqa:
#    print("Mijoz choy chaqa berdi")
#    narh=narh+1000
# else:
#    print("Mijoz choy chaqa bermadi")

# print(f"Mijoz {narh} so'mlik harid qildi")

# menu=["osh","qozonkabob","somsa","manti"]
# menu.append("norin")
# menu.append("shashlik")

# # # in operatori bizga menuda borligida
# # # not in esa yo'q bo'ganda qo'l keladi

# ovqat=input("Qanday ovqat yeysiz?\n>>> ")
# if ovqat.lower() in menu:
#    print("Buyurtmangiz qabul qilindi. Iltimos biroz kutib turing ")
# else:
#    print("Kecherasiz ,ammo, bizda bunday taom yo'q")

# ovqat=input("Qanday ovqat yeysiz?\n>>> ")
# if ovqat.lower() not in menu:
#    print("Kecherasiz ,ammo, bizda bunday taom yo'q")
# else:
#    print("Buyurtmangiz qabul qilindi. Iltimos biroz kutib turing ")

# menu=['osh', 'qozonkabob', 'somsa', 'manti', 'norin', 'shashlik']
# buyurtmalar=["osh","norin","somsa","choy","non"]

# for taomlar in buyurtmalar:
#    if taomlar in menu:
#        print(f"Menuda {taomlar} bor")
#    else:
#        print(f"Menuda {taomlar} yo'q")

# buyurtmalar=["osh","norin","somsa","choy","non"]
# if buyurtmalar:
#    print(f"ro'yxat {len(buyurtmalar)} taom bor")
# else:
#    print("ro'yxat bo'm-bo'sh")
        
menu=['osh', 'qozonkabob', 'somsa', 'manti', 'norin', 'shashlik']
buyurtmalar=["osh","norin","somsa","choy","non"]
if buyurtmalar: # agar ro'yxatda taomlar bo'lsa true qiymat qaytaradi
    for taomlar in buyurtmalar:
        if taomlar in buyurtmalar:
            print(f"Menuda {taomlar} bor")
        else:
            print(f"Menuda {taomlar} yo'q")
else:
    print("Buyurtmangiz bo'm bo'sh")





































