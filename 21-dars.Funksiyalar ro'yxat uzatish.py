# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:47:51 2024

21-dars. Funksiyalar ro'yxat uzatish

@author: User: Muhammadyusuf Soyipov
"""

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar


talabalar = ["ali", "vali", "hasan", "husan"]
baholar = bahola(talabalar)
print(baholar)
print(talabalar)
############################################################
talabalar = ["ali", "vali", "hasan", "husan"]


def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar


baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)