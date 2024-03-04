import random
def probel():
    N = int(input("введите сколько будет слов "))
    s=""
    for i in range(N):
        s+=input("введите число ")
        s+=" "
    print(s)

def probelStop():
    s=""
    while True:
        choice = input("введите что-то или stop ")
        if choice=="stop":
            break
        else:
            s+=choice
            s+=" "
    print(s)

def bykvaF():
    slovo=input("введите слово ")
    if "ф" in slovo:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

def matem():
    pravda=0
    owibka=0
    while True:
        a=random.randint(1,10)
        b=random.randint(1,10)
        c=int(input(f"{a}+{b}="))
        if c ==a + b:
            pravda+=1
            print("Правильно! ")
        else:
            print("Ответ неверный ")
            owibka+=1
        if owibka==3:
            print(f"Игра окончена. Правильных ответов:{pravda} ")
            break
while True:
    choice = input("\n1-слова по выбору кол-во \n2-слова без выбора кол-во \n3-редкие слова с буквой ф \n4-математика игра \n")
    match choice:
        case "1":
            probel()
        case "2":
            probelStop()
        case "3":
            bykvaF()
        case "4":
            matem()
    if choice == "0":
        break