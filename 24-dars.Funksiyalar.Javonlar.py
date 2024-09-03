# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:25:28 2024

24-dars.Funksiyalar.Javoblar

@author: User: Muhammadyusuf Soyipov

"""
f1 = lambda x: x * 10
print(f1(10))
#################################################
f2 = lambda x, y: x * y
print(f2(5, 4))
############################
from random import sample
from math import sqrt

x = list(range(0, 1001))
y = sample(x, k=10)
print(y)

ildizlar = list(map(lambda n: sqrt(n), y))
print(ildizlar)

toq_sonlar = list(filter(lambda n: n % 2, y))
print(toq_sonlar)
##################################################
def tubmi(x):
    if x % 2 == 0 or x < 2:
        return False  # Son juft yoki 2 dan kichik bo'lsa
    if x == 2 or x == 3:
        return True  # Son 2 yoki 3 bo'lsa
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True


tub_sonlar = list(filter(tubmi, range(1000)))
print(tub_sonlar)
