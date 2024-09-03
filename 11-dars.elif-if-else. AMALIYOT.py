# Sana: 17.03.07.2024
# 10-dars: elif-if-else
# Dasturchi: Muhammadyusuf Soyipov
#                    AMALIYOT

# son=int(input("Iltimos juft sonni kiriting\n... "))
# if son==2:
#    print("Rahmat")
# else:
#    print('Bu juft son emas')



# yosh=int(input("Yoshingizni kiriting\n>>> "))
# if yosh<4 or yosh>60:
#    print("Siz uchun kirish bepul")
# elif yosh<18:
#    print("Siz uchun kirish 10000 so'm")
# elif yosh>18:
#    print("Siz uchun kirish 20000 so'm")



# yosh=int(input("Yoshingizni kiriting\n>>> "))
# if yosh<4 or yosh>60:
#    narx=0
# elif yosh<18:
#    narx=10000
# elif yosh>18:
#    narx=20000
# print(f"Siz uchun muzeyga chipta narxi {narx} so'm")



# x=int(input("1-sonni kiriting\n>>> "))
# y=int(input("2-sonni kiriting\n>>> "))
# if x<y:
#    print("x<y")
# elif x>y:
#    print("x>y")
# elif x==y:
#    print("x=y")



# mahsulotlar=["qatiq","qaymoq","smetana","tvaro'g",
# "pishloq","sut","muzqaymoq",
# "shokalad","pechenniy","chips"]
# a=int(input("Iltimos olmoqchi bo'lgan mahsulotlaringiz soni kiriting "))
# a=5
# savat=[]
# for n in range(a):
#    savat.append(input(f"{n+1}-olmoqchi bo'lgan narsangiz nima edi? \n>>> "))
# print(f"Demak,siz olmoqchi bo'lgan narsalar: {savat} shulardan iborat edi.")

# for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        print(f"{mahsulot} do'konimizda bor")
#    else:
#        print(f"{mahsulot} do'konimizda yo'q")



#a=3
#savat=[]
#for n in range(a):
#    savat.append(input(f"{n+1}-olmoqchi bo'lgan narsangiz nima edi? \n>>> "))
#mahsulotlar=["qatiq","qaymoq","smetana","tvaro'g","pishloq","sut","muzqaymoq","shokalad","pechenniy","chips"]
#bor_mahsulotlar=[]
#mavjud_emas=[]
#if savat:
#    for m in savat:
#        if m in mahsulotlar:
#            bor_mahsulotlar.append(m)
#        else:
#            mavjud_emas.append(m)
#            if len(mavjud_emas)==0:
#                print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

#if len(mavjud_emas)==0:
#    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#elif len(bor_mahsulotlar)==0:
#    print(f"Quyidagi mahsulotlar do'konimizda yo'q:{mavjud_emas}")



#foydalanuvchilar=["asadbek","ozodbek","ali","vali","salim"]
#foydalanuvchi=input("Ismingizni kiriting\n>>> ")
#if foydalanuvchi.lower() in foydalanuvchilar:
#    print("Login band, boshqa login tanlang")
#else:
#    print(f"Xush kelibsiz {foydalanuvchi.title()}")



son = int(input("Istalgan butun son kiriting: "))

for n in range(2,son+1):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")











