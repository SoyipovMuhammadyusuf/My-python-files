"""
06/12/2020

Dasturlash asoslari

#16-dars: NESTING

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

buxoriy = {
    "ism": "Abu Abdulloh Muhammad ibn Ismoil",
    "tyil": 810,
    "vyil": 870,
    "tjoy": "Buxoro",
}

qodiriy = {"ism": "Abdulla Qodiriy", "tyil": 1894, "vyil": 1938, "tjoy": "Toshkent"}

vohidov = {"ism": "Erkin Vohidov", "tyil": 1936, "vyil": 2016, "tjoy": "Farg'ona"}

navoiy = {"ism": "Alisher Navoiy", "tyil": 1441, "vyil": 1501, "tjoy": "Xirot"}

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs["ism"]
    tyil = shaxs["tyil"]
    vyil = shaxs["vyil"]
    tjoy = shaxs["tjoy"]
    print(
        f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. " f"{vyil-tyil} yil umr ko'rgan."
    )



buxoriy = {
    "ism": "Abu Abdulloh Muhammad ibn Ismoil",
    "tyil": 810,
    "vyil": 870,
    "tjoy": "Buxoro",
    "asarlar": [
        "Al-jome’ as-sahih",
        "Al-adab al-mufrad",
        "At-tarix al-kabir",
        "At-tarix as-sag‘ir",
    ],
}

qodiriy = {
    "ism": "Abdulla Qodiriy",
    "tyil": 1894,
    "vyil": 1938,
    "tjoy": "Toshkent",
    "asarlar": ["O'tkan kunlar", "Mehrobdan Chayon", "Obid ketmon"],
}

vohidov = {
    "ism": "Erkin Vohidov",
    "tyil": 1936,
    "vyil": 2016,
    "tjoy": "Farg'ona",
    "asarlar": ["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"],
}

navoiy = {
    "ism": "Alisher Navoiy",
    "tyil": 1441,
    "vyil": 1501,
    "tjoy": "Xirot",
    "asarlar": ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", "Munojot"],
}

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs["ism"]
    asarlar = shaxs["asarlar"]
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)
        
        

kinolar = {
    "ali": ["Terminator", "Rambo", "Titanic"],
    "vali": ["Tenet", "Inception", "Interstellar"],
    "hasan": ["Abdullajon", "Bomba", "Shaytanat"],
    "husan": ["Mahallada duv-duv gap", "John Wick"],
}


for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)



davlatlar = {
    "o'zbekiston": {
        "poytaxt": "toshkent",
        "maydon": 448978,
        "aholi": 33_000_000,
        "pul birligi": "so'm",
    },
    "rossiya": {
        "poytaxt": "moskva",
        "maydon": 17_098_246,
        "aholi": 144_000_000,
        "pul birligi": "rubl",
    },
    "aqsh": {
        "poytaxt": "vashington",
        "maydon": 9_631_418,
        "aholi": 327_000_000,
        "pul birligi": "dollar",
    },
    "malayziya": {
        "poytaxt": "kuala-lumpur",
        "maydon": 329750,
        "aholi": 25_000_000,
        "pul birligi": "rinngit",
    },
}

for davlat, info in davlatlar.items():
    if davlat.lower() == "aqsh":
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(
        f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
        f"\nHududi: {info['maydon']} kv.km"
        f"\nAholisi: {info['aholi']}"
        f"\nPul birligi: {info['pul birligi']}"
    )
    
    
    

davlatlar = {
    "o'zbekiston": {
        "poytaxt": "toshkent",
        "maydon": 448978,
        "aholi": 33_000_000,
        "pul birligi": "so'm",
    },
    "rossiya": {
        "poytaxt": "moskva",
        "maydon": 17_098_246,
        "aholi": 144_000_000,
        "pul birligi": "rubl",
    },
    "aqsh": {
        "poytaxt": "vashington",
        "maydon": 9_631_418,
        "aholi": 327_000_000,
        "pul birligi": "dollar",
    },
    "malayziya": {
        "poytaxt": "kuala-lumpur",
        "maydon": 329750,
        "aholi": 25_000_000,
        "pul birligi": "rinngit",
    },
}

davlat = input("Davlat nomini kiriting: ").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(
        f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
        f"\nHududi: {info['maydon']} kv.km"
        f"\nAholisi: {info['aholi']}"
        f"\nPul birligi: {info['pul birligi']}"
    )
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")