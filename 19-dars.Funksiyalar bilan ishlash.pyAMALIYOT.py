# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:20:11 2024

19-dars. Amaliyot

@author: User: Muhammadyusuf Soyipov

"""

def yosh_hisobla(t_yil,joriy_yil=2024):
    """Foydalanuvchining yoshini hisoblaymiz"""
    print(f"Siz {joriy_yil-t_yil} yoshdasiz")

t_yil=int(input("Tug'ilgan tilingizni kiriting: "))
yosh_hisobla(t_yil)



def yosh_hisobla(t_yil,joriy_yil):
    print(f"Siz {joriy_yil-t_yil} yoshdasiz")

yosh_hisobla(1993,2024)



def salom_ber():
    print("Assalomu alaykum")


salom_ber()



def toliq_ism(ism,familiya):
    print(f"Foydalanuvchining ismi: {ism.title()}",
          f"Foydalanuvchining familiyasi: {familiya.title()}")

toliq_ism(familiya='soyipov',ism='muhammadyusuf')


##########################################
##########################################
#################AMALIYOT#########################
##########################################
##########################################
def toliq_ism(ism,familiya,t_yil,joriy_yil=2024):
    t_yil=int(t_yil)
    print(f"Foydalanuvchining ismi: {ism.title()}",
          f"Foydalanuvchining familiyasi: {familiya.title()}",
          f"Foydalanuvchining yoshi: {joriy_yil-t_yil}")

ism=input("Ismingiz nima? ")
familiya=input("Familiyangiz nima? ")
t_yil=int(input("Nechanchi yilda tug'ilgansiz? "))
toliq_ism(ism, familiya, t_yil,)
toliq_ism('muhammadyusuf', "soyipov", 2009)
################################################################



def kv_kub(son):
    print(f"Sonning kvadrati {son**2} \nVa\nSonning kubi {son**3} ga teng")

son=int(input("Istalgan butun son kiriting>>>"))
kv_kub(son)
kv_kub(32)
################################################################



def taqqosla(x,y):
    if x>y:
        print(f"{x}>{y}")
        print("x katta y dan")
    elif x<y:
        print(f"{x}<{y}")
        print("x kichik y dan")
    else:
        print(f"{x}={y}")
        print("Sonlar teng")

x=int(input("1-butun son kiriting>>>"))
y=int(input("2-butun son kiriting>>>"))
taqqosla(x, y)
taqqosla(536, 7523)
############################################################


def aniqla(son):
    if son%2==0:
        print("Bu juft son.")
    else:
        print("Bu toq son, iltimos juft son kiriting.")
son=int(input("istalgan son kiriting>>>"))
aniqla(son)
#aniqla(4)


def darajaga_kotar(x,y=2):
    print(f"x ning y-darajasi {x**y} ga teng.")

darajaga_kotar(3, 4)
darajaga_kotar(4)


def BA(son):
    for n in range(2,11):
        if son%n==0:
            print(f"{n}", end=' , ')
BA(100)



