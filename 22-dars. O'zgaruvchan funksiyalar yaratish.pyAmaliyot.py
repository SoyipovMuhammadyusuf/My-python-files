# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:29:00 2024

22-dars. O'zgaruvchan funksiyalar create Amaliyot

@author: User: Muhammadyusuf
"""
def kopaytir(*sonlar):
    kopaytma=1
    for son in sonlar:
        kopaytma*=son
    return kopaytma
print(kopaytir(2,4,4))
########################################
def malumot(ism,familiya,**malumotlar):
    malumotlar['ism']=ism
    malumotlar["familiya"]=familiya
    print(malumotlar)
    return malumotlar

n=malumot("muhammadyusuf", "soyipov", tyili=2009)
print(n)

