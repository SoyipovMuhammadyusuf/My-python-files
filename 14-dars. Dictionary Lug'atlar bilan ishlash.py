# Sana: 27.07.2024
# 14-dars. Dictionary Lug'atlar bilan ishlash
# Dasturchi: Muhammadyusuf Soyipov



car_0={"model":"ferrari","rang":"qizil"}
print(car_0['model'])
print(car_0['rang'])

en_uz={"apple":"olma","banana":"banan","apricot":"o'rik"}
print(en_uz['apple'])

mevalar={"olma":10000,"tarvuz":8000,"qovun":10000}
print(f"Olma narxi {mevalar['olma']} so'm")



# # # Luga'tda istalgan ma'lumot turlarini saqlash mumkin
talaba={"ism familiya":"murod olimov","yosh":20,"t_yil":2004}
print(f"{talaba['ism familiya'].title()},\
      {talaba['t_yil']}-yilda tug'ilgan,\
      {talaba['yosh']} yoshda")

# Yangi kalit so'z qo'shish
talaba['kurs']=4
talaba['fakultet']="informatika"
# Oldindan mavjud bo'lgan kalit so'zni o'zgartirish
talaba['ism']='abdulloh'

print(talaba)



# # # Bo'sh lug'atni to'ldirish
talabaa={}
talabaa['ism']='qobil rasulov'.title()
talabaa['kurs']=3
talabaa['yosh']=20
print(talabaa)
print(f"Talaba {talabaa['ism']} {talabaa['kurs']}-kurs")

# Qiymatni yangilash
talabaa["kurs"]=4
print(f"Talaba {talabaa['ism']} {talabaa['kurs']}-kurs")



# Kalit so'z yokida qiymatni o'chirish
talaba={"ism familiya":"murod olimov","yosh":20,"t_yil":2004}
print(talaba)
del talaba['yosh']
print(talaba)

print(en_uz)
en_uz={'apple': 'olma', 'banana': 'banan', 'apricot': "o'rik"}
del en_uz['apple']
print(en_uz)



# Lug'atlarni bir nechta qatorlarda yozish
telefonlar={
    'ali':"iphone x",
    'anvar':'poco f5',
    "husniddin":"infinix",
    'sardor':'galaxy A6',
    'orif':"nokia"
    }

# # # # .get() metodi
en_uz={'apple': 'olma', 'banana': 'banan', 'apricot': "o'rik"}
meva=en_uz.get('apple',"Bunday meva mavjud emas")
print(meva)

meva=en_uz.get('pineapple',"Bunday meva mavjud emas")
print(meva)

telefonlar={
    'ali':"iphone x",
    'anvar':'poco f5',
    "husniddin":"infinix",
    'sardor':'galaxy A6',
    'orif':"nokia"
    }
phone=telefonlar.get('hasan')
print(phone)






































