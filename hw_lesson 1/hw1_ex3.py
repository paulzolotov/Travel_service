while 1:
    age = int(input('Введите интересующий Вас год : '))
    ## 1ый способ
    if age % 4 != 0 or (age % 100 == 0 and age % 400 != 0):
        print('Невисокосный')
    else:
        print('Високосный')
    ## 2ой способ
    # if age % 4 != 0:
    #     print("Невисокосный")
    # elif age % 100 == 0:
    #     if age % 400 == 0:
    #         print("Високосный")
    #     else:
    #         print("Невисокосный")
    # else:
    #     print("Високосный")
    ## 3ий способ
    # if age % 4 == 0:
    #     if age % 100 == 0:
    #         if age % 400 == 0:
    #             print("Високосный")
    #         else:
    #             print("Невисокосный")
    #     else:
    #         print("Високосный")
    # else:
    #         print("Невисокосный")

