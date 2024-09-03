# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 05:29:57 2024
18-dars.While Amaliyot
@author: User: Muhamamdyusuf Soyipov
"""

print("Sizning buyurtmalaringizni jadval sifatida chiqaramiz:")
buyurtmalar=[]
n=1
while True:
    savol=f"{n}-buyurtmangizni bering:>>> "
    buyurtma=input(savol)
    buyurtmalar.append(buyurtma)
    takrorlash=input("Yana buyurtma bermoqchimisiz (ha/yo'q)")
    n+=1
    if takrorlash!="ha":
        break
print("Sizning buyurtmalaringiz ro'yxati:")
for buyurtma in buyurtmalar:
    print(f"{buyurtma.title()}")
#orrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
print("Sizning buyurtmalaringizni jadval sifatida chiqaramiz:")
buyurtmalar=[]
n=1
while True:
    savol=f"{n}-buyurtmangizni bering:>>> "
    buyurtma=input(savol)
    buyurtmalar.append(buyurtma)
    takrorlash=input("Yana buyurtma bermoqchimisiz (ha/yo'q)")
    n+=1
    if takrorlash=="yo'q":
        break

print("Sizning buyurtmalaringiz ro'yxati:")
for buyurtma in buyurtmalar:
    print(f"{buyurtma.title()}")
#ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
buyurtmalar = ["olma", "anjir", "uzum", "qovun"]
mahsulotlar = {"olma": 20000, "shaftoli": 25000, "tarvuz": 18000, "uzum": 22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")