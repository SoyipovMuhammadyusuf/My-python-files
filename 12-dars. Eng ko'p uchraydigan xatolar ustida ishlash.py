# Sana:27.07.2024
# 12-dars.Eng ko'p uchraydigan xatolar ustida ishlash
# Dasturchi: Muhammadyusuf Soyipov


#print("hello world")
#print("Assalomu alaykum")

# Indentation Error joy tashlab ketish xatoligi
print("O'ngacha sanaymiz")
for n in range(10):
    print(n+1)



# Type Error
# False
son=input("Istalgan son kiriting\n>>> ")
print(f"{son} nining kvadrati {son**2} ga teng")

# True
son=int(input("Istalgan son kiriting\n>>> "))
print(f"{son} nining kvadrati {son**2} ga teng")



# NameError Funksiyaning yoki o'zgaruvchilar nomini to'g'ri yozmaslik
# False
prit("Hello world")
mevalar=['olma','uzum','anjir','nok','anor']
for meva in mvalar:
    print(meva)

# True
print("Hello world")
mevalar=['olma','uzum','anjir','nok','anor']
for meva in mevalar:
    print(meva)



# ValueError qiymatni berishda adashishlik
# False
son=int(input("Istalgan son kiriting\n>>> "))
if son>0: # kamchiligu shundaki agar biz 23.5 ga o'xshsh son kiritsak kodimiz ishlamay qoladi
    print("Musbat son")
else:
    print("Manfiy son")

# True
son=float(input("Istalgan son kiriting\n>>> "))
if son>0:
    print("Musbat son")
else:
    print("Manfiy son")
############ OR
son=int(input("Istalgan  BUTUN son kiriting\n>>> "))
if son>0:
    print("Musbat son")
else:
    print("Manfiy son")



# # IndexError
# False
mevalar=['olma','uzum','anjir','nok','anor']
####### Eslatma python dasturida ro'yxatlar bilan ishlashda 1 dan emas balki 0 dan boshlaymiz sanashni
print(mevalar[5]) # royxatdagi 6-chi narsani konsolga chiqarmoqchimiz ammo ro'yxatda 5ta element bor

# True
mevalar=['olma','uzum','anjir','nok','anor']
print(mevalar[4])



# ZeroDivisionError 0 ga bolib bo'lmaslik xatosi
# False
x,y=50,50
z=(250/(x-y))
print(z)

# True
x,y=50,50
if x>y:
    z=(250/(x-y))
    print(z)
else:
    print("0 soniga bo'lib bo'lmaydi")

# Mantiqiy xatolar
# False
radius=5
pi=4.14 # pi aslida 3.14 ga teng
print("aylana yuzi",radius**2*pi)

# True
radius=5
pi=3.14 
aylana_yuzi=pi*radius**2
print(aylana_yuzi)


# Fasle
son=float(input("Istalgan son kiriting\n>>> "))
ildiz=son**1/2 # buning xatoligi 1-sonning birinchi darajasini oladi va uni ikkiga bo'ladi
print(f"{son} sonining ildizi {ildiz} ga teng")

# True
son=float(input("Istalgan son kiriting\n>>> "))
ildiz=son**(1/2)
print(f"{son} sonining ildizi {ildiz} ga teng")
###############################OR
son=float(input("Istalgan son kiriting\n>>> "))
ildiz=son**0.5
print(f"{son} sonining ildizi {ildiz} ga teng")


# False
mevalar=['olma','uzum','anjir','nok','anor']
for meva in mevalar:
    print(meva)
    print("Dastur tugadi")

#True
mevalar=['olma','uzum','anjir','nok','anor']
for meva in mevalar:
    print(meva)
print("Dastur tugadi")


























































