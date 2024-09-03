# Sana: 11.08.2024
# 16-dars:     Amaliyot
# Dasturchi: Muhammadyusuf Soyipov


friends={
    'sardor':{
        "familiya":"qodirjonov",
        "kasb":["student",'sartarosh'],
        'tyil':2009,
        'goal':"being richman"
        },
    'husniddin':{
        "familiya":"qosimjonov",
        'kasb':"student",
        'tyil':2009,
        "goal":"doing a busines"
        },
    "hojiahror":{
        "familiya":"rasuljonov",
        "kasb":"fighter",
        'tyil':2009,
        "goal":"being the strongest"
        }
    }
for friend,info in friends.items():
    print(f"\n{friend.title()} {info['familiya'].title()},\n"
          f"{info['tyil']}-yilda tug'ilgan.\n"
          f"Hayotdagi maqsadi {info['goal']},\n"
          f"Hozirda qiladigan ishi:")
    print(f"{info['kasb']}")



taomlar={
      'onam':["sho'rva",'mastava','somsa'],
      'dadam':['osh','manti','somsa'],
      'ukam':['chips','makaron','pecheniy']
      }

for ism,taom in taomlar.items():
    print(f"\n{ism.title()}ning sevimli taomlari:")
    for taomm in taom:
        print(taomm.upper())



davlatlar={
    "o'zbekiston":{
        "poytaxti":"toshkent",
        "aholisi":37000000
        },
    "rossiya":{
        'poytaxti':"moskva",
        'aholisi':144000000
        }
    }

for davlat,info in davlatlar.items():
    davlat=davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxti'].title()} va\n"
          f"{davlat}ning aholisining soni {info['aholisi']} ga teng")



davlatlar={
    "o'zbekiston":{
        "poytaxti":"toshkent",
        "aholisi":37000000
        },
    "rossiya":{
        'poytaxti':"moskva",
        'aholisi':144000000
        }
    }

davlat=input("Birir-bir davlat nomini kiriting u haqida bilish uchun\n>>>").lower()
if davlat in davlatlar:
    info=davlatlar[davlat]
    print(f"\n{davlat .capitalize()} haqida:\n"
          f"Poytaxti:{info['poytaxti'].title()}\n"
          f"Aholisi:{info['aholisi']}")
else:
    print(f"Bizda {davlat.capitalize()} haqida hech qanday ma'lumot yo'q.")
