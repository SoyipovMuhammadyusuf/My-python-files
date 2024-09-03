# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:05:57 2024

Men yaratgan funksiyalar

@author: User

"""
# Son topish o'yini 1-qism
import random as r

def sontop(x=10):
    sonpc=r.randint(1, x)
    print(f"Men 1 dan {x} gacha bo'lgan sonlar orasidan bir son o'yladim.Uni topishga harakat qilib ko'ring.")
    #yana=True
    taxminlar=0
    while True:
        taxminlar+=1
        taxminson=int(input(">>>"))
        if taxminson>sonpc:
            print("Kichikroq son ayting.")
        elif taxminson<sonpc:
            print("Kattaroq son ayting.")
        else:
            print(f"Tabriklayman! Siz {taxminlar} ta urunish bilan topdingiz.")
            #yana=int(input("Yana o'ynaysizmi? ha(1)/yo'q(0).     >>>"))
            break
    return taxminlar
sontop(10)
################################################################
# Son topish o'yini 2-qism
def sontoppc(x=10):
    input(f"Siz 1 dan {x} gacha bo'lgan sonlar orasidan bir son o'ylang va (ENTER) tugmasini bosing.Men esa uni topishga harakat qilib ko'raman.")
    taxminlar=0
    quyi=1
    yuqori=x
    #yana=True
    while True:
        taxminlar+=1
        if quyi!=yuqori:
            son=r.randint(quyi, yuqori)
        else:
            son=quyi
        javob=input(f"Siz {son} sonini o'yladingiz! Siz men o'ylagan sonni topdingiz-(t),Men o'ylagan son kattaroq-(+),Men o'ylagan son kichikroq-(-). >>>")
        if javob=="-":
            yuqori=son-1
        elif javob=="+":
            quyi=son+1
        else:
            print(f"Qoyil men {taxminlar} ta taxmin bilan siz o'ylagan sonni topdim.")
            #yana=int(input("Yana o'ynaysizmi? ha(1)/yo'q(0).     >>>"))
            break
    return taxminlar
sontoppc(10)
############################################################
# Son topish o'yini 3-qism FINAL
def play(x=10):
    yana=True
    while yana:
        taxminlar_me=sontop(x)
        taxminlar_pc=sontoppc(x)
        if taxminlar_me<taxminlar_pc:
            print(f"Tabriklayman! Siz {taxminlar_me} ta urunish bilan g'olib bo'ldingiz.")
            yana=int(input("Yana o'ynaysizmi? ha(1)/yo'q(0).     >>>"))
        elif taxminlar_me>taxminlar_pc:
            print(f"Qoyilmaqom.Men {taxminlar_pc} ta urunish bilan g'olib bo'ldim.Keyingi safar uchun omad tilayman.")
            yana=int(input("Yana o'ynaysizmi? ha(1)/yo'q(0).     >>>"))
        else:
            print("Durrang.Keyingi safar albatta men yutaman.")
            yana=int(input("Yana o'ynaysizmi? ha(1)/yo'q(0).     >>>"))
play(20)
#########################################################
import random
from uzwords import words


def get_word():
    word = random.choice(words)
    while "-" in word or " " in word or "қ" in word or "Қ"in word:
        word = random.choice(words)
    return word.upper()


def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter


def play():
    word = get_word()
    #print(word)
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ""
    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    # print(word)
    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")

        letter = input("Ҳарф киритинг: ").upper()
        if letter in user_letters:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
            user_letters += letter
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} ҳарфи тўғри.")
        else:
            print("Бундай ҳарф йўқ.")
        user_letters += letter
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")
    return play()
play()
