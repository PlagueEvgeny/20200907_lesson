number = 23
boolean = True

while boolean:
    guess = int(input("Введите целое число : "))
    boolean = False
    if guess == number:
        print("Вы угадали!")
    elif guess > number:
        print("Число больше загаданного")
    else:
        print("Число меньше загаданного")
else:
    print("Цикл закончен.")