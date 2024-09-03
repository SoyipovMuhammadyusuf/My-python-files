# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:04:14 2024

Mening Matematika uchun yaratgan funksiyalarim.

@author: User: Muhammadyusuf Soyipov

"""

def tubmi(x):
    """Bu funksiya sizga siz kiritgan son,
    tub yoki tub emasligini tekshirib beradi"""
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
####################################################################
def tubmi(x):
    
    if x==1 or x==2 or x==3:
        return True
    if x%2==0:
        return False
    for n in range(3,x):
        if x%n==0:
            return False
    return True
x=int(input("Bu funksiya sizga siz kiritgan songacha bo'lgan barcha tub sonlarning ro'yxatini chiqarib beradi:\nIstalgan son kiriting:"))
tubsonlar=list(sorted(filter(tubmi, range(x))))
print(tubsonlar)
######################################################################
