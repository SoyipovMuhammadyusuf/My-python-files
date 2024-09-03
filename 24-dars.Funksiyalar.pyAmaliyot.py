# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:25:28 2024

24-dars.Funksiyalar. Amaliyot

@author: User: Muhammadyusuf Soyipov

"""
son=lambda x:x*10
print(son(4))
#orrrrrrrrrrrrrr
def f1(n):
    return lambda x:x*n
nx10=f1(10)
print(nx10(7))
#orrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
def k(*nn): # Istalgancha aon kiritish mumkin
    for n in nn:
        print(n*10)
k(2,7)
######################################
a_b=lambda a,b:a+b
#print(a_b(2,3))
########################################
import random as r
#x=list(r.sample(range(1000), 10))
#print(x)
#y=list(map(lambda n:n**2, x))
#print(sorted(y))
####################################################
c=list(range(1001))
e=r.sample(c, 10)
print(e)
d=list(filter(lambda x:x%2, e))
print(d)
#ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
def toqs(x):
    if x<=10:
        print(f"Uzr,{x} soni 10 dan kichik.Shuning uchun bu funksiya ishlamaydi.Iltimos 10 dan katta son kiritib qayta urunib ko'ring")
    else:
        y=list(r.sample(range(x),10))
        z=list(sorted(filter(lambda n:n%2, y)))
        print(z)
toqs(100)
#########################################
def tubmi(x):
    if x==1 or x==2 or x==3:
        return True
    if x%2==0:
        return False
    for n in range(3,x):
        if x%n==0:
            return False
    return True

while True:
    a=int(input("Istalgan son kiriting.Biz sizga bu son tub yoki yo'qligini tekshirib beramiz: "))
    print(tubmi(a))
    javob=input("Davom etasizmi (yes/no):")
    if javob!="no":
        continue
    else:
        break
#################################################################
def tubmi(x=1001):
    if x==1 or x==2 or x==3:
        return True
    if x%2==0:
        return False
    for n in range(3,x):
        if x%n==0:
            return False
    return True
tubsonlar=list(sorted(filter(tubmi, range(1001))))
print(tubsonlar)