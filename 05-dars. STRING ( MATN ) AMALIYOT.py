# 06-dars. STRING (MATN)
# Sana: 02.05.2024 Boshladim 12:30 da tugatdim 15:00 da
# Muallif=Muhammadyusuf 

# shahar=Andijon
# viloyat=Asaka
# matn="men yangi 📱 oldim"
 
# STRING (MATN) Ustida amallar

# ism="Ahad"
# familiya="Qayum"
# print(ism+' '+familiya)

# f-string
  
# ism="Ahad"
# familiya='Qayum'
# ism_sharif=f"{ism} {familiya}"
# print(ism_sharif)

# ism="James"
# familiya="Bond"
# print(f"Salom mening ismim {ism} {familiya}. {ism} {familiya}!")
 
# MAHSUS BELGILAR

# print("Hello World!")
# print('Hello \tWorld') # IZOH (\t) belgisi matnda uzun bo'shliq qoldiradi 
# print('Hello \nWorld') # IZOH (\n) belgisi matnni 2 ta ustunga bo'ladi

# STRING METODLARI

# ism="james"
# familiya="bond"
# ism_sharif=f"{ism} {familiya}"

# IZOH ".upper()" belgisi matndagi barcha harflarni bosh harfga aylantiradi
# ism_sharif=ism_sharif.upper()
# print(ism_sharif.upper())

# IZOH ".lower()" belgisi ".upper()" belgisining teskarisi
# print(ism_sharif.lower())

# IZOH ".title" belgisi matnning barcha birinchi harflarini bosh harfga o'tkazadi
# print(ism_sharif.title())

# IZOH ".capitalize()" belgisi matnning faqat 1-harfini bosh harfga o'zgartiradi
# ism="men \nmuhamadyusufman"
# print(ism.capitalize())
# print(ism_sharif.capitalize())
 
# meva="     olmani     olmani     "
# mmeva="     olmani     "
# IZOH ".lstrip()" matnning chap chekasidagi bo'shliqni olib tashlaydi
# IZOH ".strip()" matnning ikkala chekasidagi bo'shliqlarni olib tashlaydi
# IZOH ".rstrip()" matnning o'ng chekasidagi bo'shliqni olib tashlaydi 
# print("men "+meva.lstrip()+"yaxshi ko'raman")
# print("men "+meva.rstrip()+"yaxshi ko'raman")
# print("men "+meva.strip()+"yaxshi ko'raman")
# print("men "+mmeva.lstrip()+" yaxshi ko'raman")
# print("men "+mmeva.rstrip()+" yaxshi ko'raman")
# print("men "+mmeva.strip()+" yaxshi ko'raman")
 
# INPUT

# ism=input("Ismingiz nima")
# print("assalomu alaykum " +ism)
ism=input(" Ismingiz nima \n>>> ")
yosh=input(" Yoshingiz nechada\n>>> ")
# print("Assalomu alaykum "+yosh+" li "+ism)
print("Assalomu alaykum "+yosh+" yoshlik "+ism.title())













    