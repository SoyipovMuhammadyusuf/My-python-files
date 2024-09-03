# Sana: 31.07.2024
# 14-dars.Lug'at ichidagielementlar bilan ishlash
# Dasturchi: Muhammadyusuf Soyipov

##################AMALIYOT

phyton_izohli_dictionary={
    "upper()":"gapdagi barcha harflarni bosh harfga o'tkazadi",
    "(f"")":"o'zgaruvchilarni bir-biriga qo'shishda ishlatiladi",
    ".title()":"barcha so'zlarning 1- harfini bosh harfga o'tkazadi",
    ".lstrip()":"so'zning chap chekkasidagi bo'shliqni olib tashlaydi",
    "int()":"sonlar bilan ishlashda qo'l keladi va matnli malu'motlarni raqamlisiga o'tkazadi",
    "str()":"ma'lumotlarni yozuvlisiga o'tkazadi",
    "float()":"raqamlarni 10 lik sanoq sistemasiga o'tkazadi",
    "len()":"jadvalda qancha so'z borligini chiqarib beradi",
    "sorted()":"jadvalarni saralashda, tartibga silishda ishlatiladi",
    ".append()":"jadvallarga element qo'shishda ishlatiladi"
    }

for izoh in sorted(phyton_izohli_dictionary.values()):
    print(izoh)
    a=sorted(phyton_izohli_dictionary.values())
    print(f"{a}\n")
# ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
for key,value in sorted(phyton_izohli_dictionary.items()):
    print(f"{key.title()}-{value}")

sports={
       "futbol":"top",
       "tennis":"sharik",
       "golf":"top",
       "yugurish":"oyoq",
       "sakrash":"oyoq",
       "hisoblash":"aql",
       "aql":"miya"
       }

for sport,sportt in sorted(sports.items()):
    print(f"{sport}-{sportt}.\n")



sports={
       "futbol":"top",
       "tennis":"sharik",
       "golf":"top",
       "yugurish":"oyoq",
       "sakrash":"oyoq",
       "hisoblash":"aql",
       "aql":"miya"
       }

# s_tur=input("Istalgan sport turining nomini kiriting\n>>> ")
#for sport in sports:
#    if s_tur in sport:
#        print(f"{sports[s_tur]}")
#        #orrrrrrrrrrrrrrrrrrrrrr
#        print(f"{s_tur} o'ynash uchun {sports[s_tur]} kerak.")
#else:
#    print("Bizda siz so'ragan sport o'yini haqida hech qanday ma'lumot yo'q")
#ORRRRRRRRRRRRRRRRRRRRRRRRRRR
print('Dunyodagi sport turlari:')
for sport in sorted(sports):
    print(sport.upper())

print('\nDunyodagi sport turlari uchun zarur bo\'ladigan jihozlar ')
for jihozlar in sorted(sports.values()):
    print(jihozlar.title())

item=input("Qaysi sportni qanday jihoz bilan o'ynash mumkin ekanligini bilmoqchimisiz\n>>> ").lower()
game=sports.get(item)
if game==None:
    print("Bizda {item} orqali o'ynaladigan o'yinlar haqaida hech qanday mal'umot yo'q")
else:
    print(f"{item.upper()} ni siz {game} orqali o'ynay olasiz")



ovqatlar={
    "osh":30000,
    "mastava":25000,
    "sho'rva":20000,
    "manti":10000,
    "somsa":20000,
    "shashlik":40000,
    "qozonkabob":50000,
    'choy':15000,
    'sharbat':35000,
    'salat':45000,
    }

savat=[]
for n in range(1):
    savat.append(input(f"{n+1}-buyurtmangizni kiriting:\n>>> "))

for ovqat in ovqatlar:
    if ovqat in savat:
        print(f"{ovqat}ning narxi {ovqatlar[ovqat]}")

for sav in savat:
    if sav not in ovqatlar:
        print("Bizda bunday taom yo'q.")
#ORRRRRRRRRRRRRRRRRRR
ovqatlar={
    "osh":30000,
    "mastava":25000,
    "sho'rva":20000,
    "manti":10000,
    "somsa":20000,
    "shashlik":40000,
    "qozonkabob":50000,
    'choy':15000,
    'sharbat':35000,
    'salat':45000,
    }

print("3 ta taom buyurtma bering\n>>> ")
buyurtmalar=[]
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-buyurtmangizni bering>>> ").lower())

for buyurtma in buyurtmalar:
    if buyurtma in ovqatlar:
        print(f"{buyurtma.title()}-{ovqatlar[buyurtma]} so'm")
    else:
        print(f"Bizda {buyurtma.title()} yo'q")



ranglar={'sariq','oq','qora'}
ranglar.add('qizil')
ranglar.update(["yashil","pushti"])
print(f"{ranglar}")



set1={10,20,30,40,50}
set2={30,40,50,60,70}
a=set1|set2
a=sorted(a)
print(a)
# ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
print(sorted(set1.union(set2)))
a=sorted(set1.union(set2))
print(a)

# Umumiy elementlar
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1 & set2
print(set3)

# To'plamlar orasida farq
print(set1.difference(set2))
print(set2.difference(set1))

# Simmetrik farq
print(set1.symmetric_difference(set2))

b=['choy','non','kartoshka','tuxum','sut']
m=['non','sut','tuxum','olma','un','tuz']
b=set(b)
m=set(m)
c=b.intersection(m)
d=(b-m)
print(d)
m=m|d
print(m)







































