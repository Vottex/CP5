while True:
    try:
        Number = int(input("Введите натуральное число: "))
        NumSys = int(input("Введите основание системы счисления (Допускается только: 2 или 8): "))
        if NumSys != 2 and NumSys != 8:
            print("Допускается только: 2 или 8!")
            continue
        break
    except ValueError:
        print("Некорректный ввод, попробуйте снова")
N_Number = ""
while Number>0:
    N_Number = str(Number % NumSys)+N_Number
    Number //= NumSys
print("В заданной вами системе счисления (",NumSys,") число будет записано так: ", N_Number)