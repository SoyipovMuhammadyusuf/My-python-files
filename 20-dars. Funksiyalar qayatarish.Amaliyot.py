# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:56:26 2024

20-dars. Funksiyalar bilan ishlash Amaliyot

@author: User: Muhammadyusuf Soyipov
"""

def oraliq(min, max,qadam):
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += qadam
    return sonlar


print(oraliq(0, 10,1))
print(oraliq(10, 21,2))
#############################################


def pasport(ism,familiya,t_yili,t_joyi,telefon_raqami):
    info={
        'ism'==ism,
        'familiya'==familiya,
        't_yili'==t_yili,
        't_joyi'==t_joyi,
        "telefon_raqami"==telefon_raqami
        }
    return info

print("Odamlar haqida ma'lumotlar to'playmiz:")
shaxslar=[]
while True:
    print("\nQuyidagi savollarga javob bering:", end=' ')
    ism=input("Shaxsning ismi:")
    familiya=input("Shaxsning familiyasi:")
    t_yili=input("Shaxsning t_yili:")
    t_joyi=input("Shaxsning t_joyi:")
    telefon_raqami=input("Shaxsning telefon_raqami:")
    shaxslar.append(pasport(ism, familiya, t_yili, t_joyi, telefon_raqami))
    savol=input("Yana shaxs qo'shasizmi?(yes/no)>")
    if savol=='no':
        break

print("Siz kiritgan barcha ma'lumotlar shu yerda:")
for shaxs in shaxslar:
    print(f"{ism.title()} {familiya.title()},{t_yili}-yilda {t_joyi.title()}da tavallud topgan.Bog'lanish uchun telefon raqami {telefon_raqami}.")
##############################################################################
def pasport(ism,familiya,t_yili,t_joyi,telefon_raqami=None):
    info={
        'ism':ism,
        'familiya':familiya,
        't_yili':t_yili,
        't_joyi':t_joyi,
        "telefon_raqami":telefon_raqami
        }
    return info

print("Odamlar haqida ma'lumotlar to'playmiz:")
shaxslar=[]
while True:
    print("\nQuyidagi savollarga javob bering:\n")
    ism=input("Shaxsning ismi:")
    familiya=input("Shaxsning familiyasi:")
    t_yili=input("Shaxsning t_yili:")
    t_joyi=input("Shaxsning t_joyi:")
    telefon_raqami=input("Shaxsning telefon_raqami:")
    shaxslar.append(pasport(ism, familiya, t_yili, t_joyi, telefon_raqami))
    savol=input("Yana shaxs qo'shasizmi?(yes/no)>")
    if savol=='no':
        break

print("Siz kiritgan barcha ma'lumotlar shu yerda:")
for shaxs in shaxslar:
    if shaxs["telefon_raqami"]:
        telefon_raqami=shaxs["telefon_raqami"]
    else:
        telefon_raqami="Noma'lum"
    print(
        f"{ism.title()} {familiya.title()},{t_yili}-yilda {t_joyi.title()}da tavallud topgan.Bog'lanish uchun telefon raqami {telefon_raqami}."
        )
#########################################################################
def chiqar(x,y,z):
    print(max(z,y,x))
chiqar(23, 43, 9538)
###################################################################
def tub_sonlar_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar
print(list(tub_sonlar_top(1000, 10000)))
###################################################
def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


print(fibonacci(11))
