from random import randint

print("Добро пожаловать в числовую угодайку! =)")


def is_valid(num):
    return num.isdigit()


def range_l():
    while True:
        r = input("Введите минимальную границу чисел: ")
        if is_valid(r) == True:
            return int(r)
        else:
            print("Может все таки введем число? :/")


def range_r():
    while True:
        r = input("Введите максимальную границу чисел: ")
        if is_valid(r) == True:
            return int(r)
        else:
            print("Может все таки введем число? :/")


r1 = range_l()
r2 = range_r()


def input_num():
    while True:
        n = input(f"Введите число от {r1} до {r2}: ")
        if is_valid(n) == True:
            return int(n)
        else:
            print(f"Может все таки введем число от {r1} до {r2}? :/")


def guess_number():
    count = 0
    rand = randint(r1, r2)
    while True:
        n = input_num()
        count += 1
        if n < rand:
            print("Ваше число меньше, попробуй еще разок :)")
        elif n > rand:
            print("Ваше число больше, поробуй еще разок :)")
        elif n == rand:
            print(
                f"Ура, победа!!! Вы угадали число :D. Ваше количество попыток - {count}. \nХотите продолжить?"
            )
            break

    s = input(
        "Для продолжения игры введите (да) или любой символ что бы завершить игру!: "
    )
    if s == "да":
        guess_number()
    else:
        print("Cпасибо за игру, еще увидимся... :)")


guess_number()
