# 07-dars: List
# Sana: 08.05.2024  09:13 dan 10:30 gacha 
# Dasturchi: Muhammadyusuf

# IZOH '[]' belgisi o'zgaruvchiga bir nechta element qo'shishda ishlatiladi
# mevalar=["olma",'anjir',"shaftoli","o'rik"] # mevalar ro'yxati (matnlar)
# narxlar=[12000,18000,10900,22000,25000,36000,63.2] # narxlar ro'yxati (sonlar)
# sonlar=['bir','ikki',3,4,5] # sonlar va matnlar arlash ro'yxat
# ismlar=[] # bo'sh ro'yxat

# print("Birinchi meva",mevalar[0])
# print("ikkinchi meva",mevalar[1])

# print("Birinchi meva",mevalar[0].upper())
# print("ikkinchi meva",mevalar[1].title())

# narxlar=[12000,18000,10900,22000]
# print(narxlar[1]+narxlar[3])

# # Elementlarni o'zgartirish

# narxlar=[12000,18000,10900,22000]
# narxlar[0]=13000 # 1-qiymatni 13000 ga o'zgartirdik
# narxlar[2]=11000 # 2-qiymatni 11000 ga o'zgartirdik
# narxlar[3]=narxlar[3]+2000 # 4-qiymatga 2000 ni qo'shdik
# print(narxlar)

# IZOH ".append()" funksiyasi ro'yxat oxirigaelemat qo'shishda foydalaniladi
# mevalar=["olma",'anjir',"shaftoli","o'rik"]
# mevalar.append("tarvuz") # mevalar oxiriga "tarvuz" ni qo'shdik
# print(mevalar)

# cars=[] # bo'sh ro'yxat yaratamiz
# cars.append("Lacetti") # ro'yxatga Lacettini qo'shdik
# cars.append("Nexia 3") # ro'yxatga Nexia 3 ni qo'shdik
# cars.append("Cobalt") # ro'yxatga Cobatni qo'shdik
# print(cars)

# IZOH ".insert" elementni elementlar orasiga qo'shishda ishlatiladi

# cars=['Lacetti', 'Nexia 3', 'Cobalt']
# cars.insert(0,"Malibu") # 1- o'ringa yangi element qo'shamiz
# print(cars)
# cars.insert(-1,"Damas") # oxirgidan 1 ta oldingi o'ringa yangi qiymat qo'shamiz
# print(cars)

# "del" elementlarni o'chirishda ishlatiladi 
# mevalar=["olma",'anjir',"shaftoli","o'rik"]
# del mevalar[1] # 2- o'rindagi "anjirni" o'chirdik
# print(mevalar)

# IZOH "o'zgaruvchi.remove["elementni kiritamiz"]"

# va remove funksiyasi biz kiritgan elementni o'chirib tashlaydi
# mevalar.remove("anjir")
# print(mevalar)

hayvonlar=["it","mushuk","sigir","qo'y","quyon","mushuk"]
hayvonlar.remove("mushuk") # ro'yxatdagi 2-o'rindagi mushukni olib tashlaydi
print(hayvonlar)

# IZOH ".pop(indeks)" 
# ro'yxatning ichidan elementni sug'urib olishda ishlatiladi

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)






























