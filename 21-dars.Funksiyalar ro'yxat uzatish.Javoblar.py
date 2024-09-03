# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:47:51 2024

21-dars. Funksiyalar ro'yxat uzatish.JAVOBLAR

@author: User: Muhammadyusuf Soyipov
"""

def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()


ismlar = ["ali", "vali", "hasan", "husan"]
katta_harf(ismlar)
print(ismlar)
########################################################
def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
    return matnlar


ismlar = ["ali", "vali", "hasan", "husan"]
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)
#############################################################
talabalar = ["ali", "vali", "hasan", "husan"]


def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar


baholar = bahola(talabalar)
print(baholar)
print(talabalar)