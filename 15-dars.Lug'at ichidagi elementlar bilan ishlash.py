# Sana: 31.07.2024
# 14-dars.Lug'at ichidagielementlar bilan ishlash
# Dasturchi: Muhammadyusuf Soyipov




talaba={"ism familiya":"murod olimov",
        "yosh":20,
        "t_yil":2004,
        }

# items() metodi bizga lug'atlar ichidagi barcha elementlar bilan ishlashga yordam beradi

#print(talaba.items())

#for key, value in talaba.items():
#    print(f"Key:{key}")
#    print(f"Value:{value} \n")

en_uz={
       "run":"yugurmoq",
       "jump":"sakramoq",
       "drink":"ichmoq",
       "sleep":"uhlamoq",
       "kill":"o'ldirmoq",
       "save":"saqlamoq",
       }

for english,uzbek in en_uz.items():
    print(f"All the words our dictionary has is in here: \n>>> ({english})")
    print(f"Bizning lugatimizdagi barcha so'zlar shu yerda:\n>>> ({uzbek}) \n")
#############################ORRRRRRRRRRRRRRRRRRRRRRRRRRRR
for english,uzbek in en_uz.items(): 
    print(f"{english}-{uzbek} \n")



telefonlar={
    'ali':"iphone x",
    'anvar':'poco f5',
    "husniddin":"infinix",
    'sardor':'galaxy A6',
    'orif':"nokia"
    }

for person,phone in telefonlar.items():
    print(f"{person.title()}ning telefonining rusumi <<{phone}>>. \n")



# keys()
mahsulotlar={
    "olma":10000,
    "anor":15000,
    "anjir":20000,
    "behi":25000,
    "shaftoli":30000,
    }

print("Do'konimizdagi mahsulotlar:")
for mahsulot in mahsulotlar.keys():
    print(f"{mahsulot.title()} \n")
#ORRRRRRRRRRRRRRRRRRRRRRRRRRRR
print("Do'konimizdagi mahsulotlar:")
for mahsulot in mahsulotlar:
    print(mahsulot.title())



mahsulotlar={
    "olma":10000,
    "anor":15000,
    "anjir":20000,
    "behi":25000,
    "shaftoli":30000,
    }

jami=[]
bozorlik=["olma",'anor','anjir','non']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        jami.append(mahsulotlar[mahsulot])
        print(f"Jami {sum(jami)} so'm")
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling.")
# ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
mahsulotlar={
    "olma":10000,
    "anor":15000,
    "anjir":20000,
    "behi":25000,
    "shaftoli":30000,
    }

bozorlik=["olma",'anor','anjir','non']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling.")



# # values
telefonlar={
    'ali':"iphone x",
    'anvar':'poco f5',
    "husniddin":"infinix",
    'sardor':'galaxy A6',
    'orif':"nokia",
    'men':"iphone x",
    "u":"nokia"
    }

print(telefonlar.values())

print("Mening do'stlarim ishlatadigan telefon turlari:")
for tel in telefonlar.values():
    print(tel)

#### set() ro'yxatdagi barcha bir xil elementlardan faqat bittasini qoldirishda ishlatiladi
print("Mening do'stlarim ishlatadigan telefon turlari:")
for tel in set(telefonlar.values()):
    print(tel)

toys={'bear','car','dog','cat','bear','car','cat'}
print(toys)

print(set(toys))







































