# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:29:00 2024

22-dars. O'zgaruvchan funksiyalar create

@author: User: Muhammadyusuf
"""


def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi


print(summa(1, 2))
print(summa(1, 2, 3, 4, 5))
print(summa(4, 5, 6, 7))
#################################################
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)


print(summa(2))
print(summa(1, 2, 3, 4, 5))
print(summa(4, 5, 6, 7))
###############################################|
def summa(x, y, *sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return x + y + sum(sonlar)


print(summa(1, 2))
print(summa(1, 2, 3, 4, 5))
print(summa(4, 5, 6, 7))
print(summa(2))
##############################
def avto_info(kompaniya, model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar["kompaniya"] = kompaniya
    malumotlar["model"] = model
    return malumotlar


avto1 = avto_info("GM", "malibu", rang="qora", yil=2018)
avto2 = avto_info("Kia", "K5", rang="qizil", narh=35000, yil=2020, korobka="avtomat")
######################
def avto_info(kompaniya, model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar["kompaniya"] = kompaniya
    malumotlar["model"] = model
    return malumotlar


avto1 = avto_info("GM", "malibu", rang="qora", yil=2018)
avto2 = avto_info("Kia", "K5", rang="qizil", narh=35000, yil=2020, korobka="avtomat")
#################################################
def talaba_info(ism, familiya, **kwargs):
    kwargs["ism"] = ism
    kwargs["familiya"] = familiya
    return kwargs


talaba = talaba_info("olim", "olimov", tyil=1995, fakultet="IT", yonalish="AT")