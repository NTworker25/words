import os
import random
import sys
from random import choice

clear = lambda: os.system('cls')

head = """
                       _     
                      | |    
__      _____  _ __ __| |___ 
\ \ /\ / / _ \| '__/ _` / __|
 \ V  V / (_) | | | (_| \__|
  \_/\_/ \___/|_|  \__,_|___/   
  by NTworker                           
"""
print(head)
print("Привет! Я загадал слово, твоя задача - отгадать его по буквам.")
input("*Нажми Enter, чтобы продолжить*")
clear()
print("Поехали!")

words = ["дирижабль", "квокка", "станция", "книга", "котлета", "программист", "дом"]
word = random.choice(words)

letters = []
hp = 10

while hp > 0:
    isWin = True
    for symb in word:
        if symb in letters:
            print(symb, end=" ")
        else:
            print("*", end=" ")
            isWin = False
    print()

    if isWin:
        print("""
                              _       _ 
                             (_)     | |
 _   _  ___  _   _  __      ___ _ __ | |
| | | |/ _ \| | | | \ \ /\ / / | '_ \| |
| |_| | (_) | |_| |  \ V  V /| | | | |_|
 \__, |\___/ \__,_|   \_/\_/ |_|_| |_(_)
  __/ |                                 
 |___/         
 Ты угадал! Молодец.                         
""")
        break

    letter = input("Введите букву: ")
    letters.append(letter)
    clear()

    if letter not in word:
        hp -= 1
        print(f"Осталось попыток {hp}")

if hp == 0:
    print("""
                                                  
                                                  
  __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
 / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
| (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
 \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  __/ |                                           
 |___/                                  
 Ты проиграл! У тебя закончились попытки.          
""")




