# Sana: 27.07.2024
# 14-dars. Dictionary Lug'atlar bilan ishlash
# Dasturchi: Muhammadyusuf Soyipov

################ Amaliyot

men={"ism":"muhammadyusuf soyipov","t_yil":2009,"yosh":15}
print(f"Mening ismim {men['ism'].title()},\
      men {men['t_yil']}-yilda tug'ilganman\
      va men hozirda {men['yosh']} yoshdaman")

ukam={"ism":"muhammadayub soyipov","yosh":2,"oiladagi orni":"chaqaloq",
      'yoqtirgan ovqati':"makaron"}
print(f"Mening ismim {men['ism'].title()},\
      mening ukamning ismi esa {ukam['ism'].title()},\
      u hozirda {ukam['yosh']} yoshda va u {ukam['oiladagi orni']},\
          uning yoqtirgan ovqati esa {ukam['yoqtirgan ovqati']}")

oyim={
      1:"mastava",
      2:"sho'rva",
      3:"grechka",
      4:"somsa",
      5:"qozonkabob"
      }

print(f"{oyim[1]}")

otam={
      1:"palov",
      2:"shashlik",
      3:"go'shtlik somsa",
      4:"lag'mon",
      5:"makaron"
      }

print(f"{otam[2]}")

opam={
      1:"chips",
      2:"go'sht",
      3:"qovurdoq",
      4:"kars-kurs",
      5:"shirinliklar"
      }

print(f"{opam[3]}")

ukam={
      1:"chips",
      2:"choy",
      3:"pechenniy",
      4:"tvarog",
      5:"shokolad"
      }

print(f"{ukam[4]}")

men={
     1:"osh",
     2:"shashlik",
     3:"muzqaymoq",
     4:"ayron",
     5:"shokoladlik pechenniylar"
     }

print(f"{men[1]} {men[2]} {men[3]} {men[4]} {men[5]}.")

#men=["osh","shashlik","muzqaymoq","ayron","shokoladlik pechenniylar"]
#print(men[1:5])




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

print(f"{phyton_izohli_dictionary['str()']}")


en_uz={'apple': 'olma', 'banana': 'banan', 'apricot': "o'rik"}
a=input("Istalga so'zni kiriting\n>>> ")
if a in en_uz:
    print(f"{en_uz[a]}")
else:
    print("Bunday so'z mavjud emas")

###################### ORRRRRRRRRRR

en_uz={'apple': 'olma', 'banana': 'banan', 'apricot': "o'rik"}
a=input("Istalga so'zni kiriting\n>>> ")
meva=en_uz.get(a,"Bunday so'z mavjud emas")
print(meva)




























