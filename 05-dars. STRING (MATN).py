# 05-dars. STRING (MATN)
# SANA:02.05.2024 12:30 dan 15:00 gacha
# MUALLIF: Muhammadyusuf

# ism="Muhammadyusuf"

# shahar = "Andijon"
# viloyat = 'Zankent'

# matn = "Men yangi 📱 oldim"
# print(matn)

# STRING (MATN) haqida

# ism = 'Muhammadyusuf'
# print("Mening ismim " + ism)
# ism = 'Muhammadyusuf'
# familiya = 'Soyipov'
# print(ism + familiya)

# ism = 'Muhammadyusuf'
# familiya = 'Soyipov'
# print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz

# ism = "Muhammadyusuf"
# familiya = 'Soyipov'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)
# ism = "James"
# familiya = 'Bond'
# rint(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

# MAHSUS BELGILAR
# print('Hello World!')
# print('Hello \tWorld!') # IZOH "/t" belgisi uzun bo'shliq yaratadi
# print('Hello \nWorld!') # IZOH "/n" belgisi so'zlarni qatorlarga bo'ladi

# STRING (METODLARI)

# ism = 'Muhammadyusuf'
# familiya = 'Soyipov'
# ism_sharif = f"{ism} {familiya}"

# IZOH ".upper()" gapdagi barcha harflarni bosh harfga o'tkazadi
# print(ism_sharif.upper())

# IZOH ( f"" ) o'zgaruvchilarni bir-biriga qo'shishda ishlatiladi 
# ism = 'Muhammadyusuf'
# familiya = 'Soyipov'
# ism_sharif = f"{ism} {familiya}"

# IZOH ".lower()" esa ".upper()" ning teskarisi
# print(ism_sharif.lower())

# IZOH ".title()" barcha so'zlarning 1- harfini bosh harfga o'tkazadi
# ism_sharif = 'james bond'
# print(ism_sharif.title())
# print('james bond'.upper())

# meva = "     olma     "

# IZOH ".lstrip()" so'zning chap chekkasidagi bo'shliqni olib tashlaydi
#print("Men " + meva.lstrip() + " yaxshi ko'raman")

# ".rstrip()"   so'zning o'ng chekkasidagi bo'shliqni olib tashlaydi
# print("Men " + meva.rstrip() + " yaxshi ko'raman")

# IZOH ".strip"  so'zning ikkala chekkasidagi bo'shliqni olib tashlaydi
# print("Men " + meva.strip() + " yaxshi ko'raman")

# IZOH (+) dan o'zgaruvchilarni bir-biriga qo'shishda foydalaniladi
# print("Men " + meva + " yaxshi ko'raman") 
 
# INPUT FUNKSIYASI

# ism = input("Ismingiz nima?")
# print("Assalom alaykum, " + ism)

ism = input("Ismingiz nima?\n>>>")
yosh=input("Yoshingiz nechada?\n>>>")
# print("Assalom alaykum " + ism)
# print("Assalom alaykum " + yosh + " li " + ism)
print("Assalomu alaykum " + yosh + " li " + ism.title())