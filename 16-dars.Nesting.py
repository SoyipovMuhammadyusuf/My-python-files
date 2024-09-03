# Sana 07.08.2024
# 16-dars:     Nesting
# Dasturchi: Muhammadyusuf Soyipov

# Lug'atlar ro'yxati

car0={
      'model':"lacetti",
      "rang":"oq",
      "yili":2020,
      "narh":15000,
      "km":500000,
      "karobka":"avtomat",
      }

car1={
      "model":"nexia",
      "rang":"qora",
      "yili":2022,
      "narh":20000,
      "km":400000,
      "karobka":"avtomat"
      }

car2={
      "model":"gentra",
      "rang":"qizil",
      "yili":2023,
      "narh":18000,
      "km":300000,
      "karobka":"meaxanika"
      }



car=car0
print(f"{car['model'].title()}, "
      f"{car['rang']}, "
      f"{car['narh']}, "
      f"{car['yili']} ")

car=car1
print(f"{car['model'].title()}, "
      f"{car['rang']}, "
      f"{car['narh']}, "
      f"{car['yili']} ")

car=car2
print(f"{car['model'].title()}, "
      f"{car['rang']}, "
      f"{car['narh']}, "
      f"{car['yili']} ")
#ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
cars=[car0,car1,car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']}, "
          f"{car['narh']}$, "
          f"{car['yili']},")

print(cars[0]['model'])

print(f"{cars[2]['rang'].title()} "
      f"{cars[2]['model']}")



# Lug'atlarni oson yaratish
malibus=[]
for n in range(10):
    newcar={
        'model':"malibu",
        "rang":None, # rang noaniq
        "yil":2024,
        'narh':None,
        "km":0,
        "karobka":"avtomat"
        }
    malibus.append(newcar)

for malibu in malibus:
    print(malibu)

# 1-uchta alibuning rangini qizil qilamiz
for malibu in malibus[:3]:
    malibu['rang']='qizil'

for malibu in malibus:
    print(malibu)

for malibu in malibus[3:6]:
    malibu['rang']='qora'

for malibu in malibus:
    print(malibu)

for malibu in malibus[6:]:
    malibu['rang']='oq'
    malibu['karobka']='mexanika'

for malibu in malibus:
    print(malibu)

for malibu in malibus:
    if malibu['karobka']=='avtomat':
        malibu['narh']=40000
    else:
        malibu['narh']=35000

    print(malibu)



# LUG'AT ICHIDA RO'YXAT
dasturchilar={
    'ali':['python','c++'],
    "vali":["html",'css','js'],
    'hasan':["php",'sql'],
    "husan":["pyton","php"],
    'maryam':["c++",'c#']
    }

for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())

for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(f"{til.upper()} ", end='')




# Nesting
hamkasblar={
    'ali':{'familiya':"valiyev",
        'tyil':1995,
        'malumot':"oliy",
        'tillar':['phyton','c++']
        },
    'vali':{'familiya':"aliyev",
        "tyil":2001,
        "malumot":"o'rta maxsus",
        "tillar":["html",'css','js']
        },
    'hasan':{'familiya':"huanov",
             'tyil':1999,
             'malumot':"maxsus",
             "tillar":["python","php"]
        }
    }

for ism,info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, \n"
          f"{info['tyil']}-yilda tug'ilgan. \n"
        f"Malumoti: {info['malumot'].title()}.\n"
          f"Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())































































