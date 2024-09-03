# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 06:00:29 2024

19-dars.Funcyion (Funksiyalar)

@author: User: Muhammadyusuf Soyipov
"""


def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")


salom_ber()



def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib,
    unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")


salom_ber("hasan")
salom_ber("olim")





def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(
        f"Foydalanuvchi ismi: {ism.title()}\n"
        f"Foydalanuvchi familiyasi: {familiya.title()}"
    )


# toliq_ism('olim','hakimov')
# toliq_ism('hakimov','olim')


def yosh_hisoblaa(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")


# yosh_hisobla('olim',1997)
# yosh_hisobla(1997,'olim')

# yosh_hisobla(ism='olim', t_yil=1997)
toliq_ism(familiya="hakimov", ism="olim")



def yosh_hisobla(tugilgan_yil, joriy_yil):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")


yosh_hisobla(1995,2020)
yosh_hisobla(1993)

# tyil = input("Tug'ilgan yilingizni kiriting: ")
# yosh_hisobla(tyil)



# Funksiyalar haqida ma'lumot olish .__doc__
print(salom_ber.__doc__)
