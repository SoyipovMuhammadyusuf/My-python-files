# 08-dars. Ro'yxatlar bilan ishlash
# 11.05.2024 12:27 dan 16:30 gacha
# Dasturchi: Muhammadyusuf    

# TARTIBLASH=sort() elementlarni taxlashda ishlatiladi
# cars=["bmw","mercedes benz","volvo","general motors","tesla","audi"]
# cars.sort()
# cars.sort(reverse=True) # Teskarisiga qarab taxlash Z-A
# print(cars)

# # # Katta kichik harf
# cars=["bmw","mercedes benz","volvo","general motors","tesla","audi"]
# cars.sort()
# print(cars)

# # # sorted() asl matnga tegmagan holda elementlarni tartiblash
# cars=["bmw","mercedes benz","volvo","general motors","tesla","audi"]
# print(sorted(cars))
# print(sorted(cars,reverse=True))
# # # mehmonlar=["Odil","Hamid","Temur","Azizbek","Farrux"]
# print("sorted() qaytargan ro'yxat:",sorted(mehmonlar))
# print("asl ro'yxat o'zgarmas qoldi:", mehmonlar)
# print(sorted(mehmonlar,reverse=True))

# # # Sonli ro'yxat
# ages=[12,98,34,65,34,76,11]
# ages.sort()
# print(ages)

# # # reverse orqali ro'yxatni aylantirish
# fruits=["pear","benana","apple","Watermelon","lemon"]
# fruits.reverse()
# print(fruits)
 
# # Ro'yxat uzunligi
# fruits=["pear","benana","apple","
# len() ro'yxatdagi elementlar sonini aniqlab beradi
# print("Elementlar soni:",len(fruits)) 
# uzunlik=len(fruits)

# # # Range() 
# sonlar=[28,51,24,24,25,25,21,528,4745,15814,245,1,574,15,4784,854,15]
# sonlar=list(range(0,10))
# sonlar=len(list(range(0,10)))
# print(sonlar)

# # # Range() va Qadam
# toq_sonlar=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# juft_sonlar=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18,]
# toq_sonlar=len(list(range(1,20,2)))
# juft_sonlar=len(list(range(0,43,2)))
# toq_sonlar=list(range(1,20,2))
# juft_sonlar=list(range(0,43,2))
# print(toq_sonlar[2]+juft_sonlar[3])
# print(juft_sonlar[2]*toq_sonlar[1])
 
# MAX() MIN() SUM()
# narxlar=[12000,14000,22552,56000,48111,]
# arzon=min(narxlar)
# qimmat=max(narxlar)
# jami=sum(narxlar)
# print("Eng arzoni:",arzon,"Eng qimmati:",qimmat,"Barchasi:",jami)
# a=min(narxlar)
# b=max(narxlar)
# c=sum(narxlar)
# print(c-(a+b))

# Ro'yxatni kesish
# cars=["bmw","mercedes benz","volvo","general motors","tesla","audi"]
# print(cars[0:3])
# print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

# Ro'yxatdan nusxa olish 
# sonlar = [1, 2, 3, 4, 5] # sonlar degan ro'yxat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# # # # # TUPLES<->LIST
# toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)
# tomonlar = (20, 30, 55.2)
# print(tomonlar)
toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
print(toys[-1])
# print(toys[2:5])
