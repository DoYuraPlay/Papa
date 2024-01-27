for i in range(1, 10):
    print(i, end=" ")
print("     Продолжить?")
oto=input("Ответ:   ")
if oto=="Да":
    for i in range(9, 0,-1):
        print(i, end=" ")
    print("     Продолжить?")
    oto2=input("Ответ:   ")
    if oto2=="Да":
        for i in range(2, 26, +4):
            print(i, end=" ")
        print("     Продолжить?")
        y=input("Ответ:   ")
        if y=="Да":
            for i in range(1, 55, +9):
                print(i, end=" ")
            print("     Продолжить?")
            r=input("Ответ:   ")
            if r=="Да":
                for i in range(50, 25, -5):
                    print(i, end=" ")
            if r=="Нет":
                print("Окей :I")
        if y=="Нет":
            print("Окей :]")
    elif oto2=="Нет":
        print("Окей :)")
elif oto=="Нет":
    print("Окей :3")