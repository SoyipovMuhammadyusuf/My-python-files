# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:29:00 2024

22-dars. O'zgaruvchan funksiyalar create.javoblar

@author: User: Muhammadyusuf
"""
def multiply(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma


print(multiply(4, 5, 6))
##############

def talaba_info(ism, familiya, **kwargs):
    kwargs["ism"] = ism
    kwargs["familiya"] = familiya
    return kwargs


talaba = talaba_info("olim", "olimov", tyil=1995, fakultet="IT", yonalish="AT")
