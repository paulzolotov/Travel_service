#! /usr/local/bin/python3

'''
Создайте декоратор, remember_result который будет сохраняет результат последнего вызова
декорированной функции и выводить его в консоль перед каждым новым вызовом

@remember_result
def sum_list(*args):
     result = ""
     for item in args:
          result += item
          print(f"Current result = '{result}'")
     return result

sum_list("a", "b")
Last result = 'None'
Current result = 'ab'

sum_list("abc", "cde")
Last result = 'ab'
Current result = 'abccde'

sum_list(3, 4, 5)
Last result = 'abccde'
Current result = '12'
'''


def remember_result(res_list):
    def my_decorator(function):
        def wrapper(*args, **kwargs):
            last_result = res_list[-1]
            print(f"Last result = '{last_result}'")
            result = function(*args, **kwargs)
            res_list.append(result)
            print(f"Current result = '{result}'")
            return result
        return wrapper
    return my_decorator


@remember_result([None])
def sum_list(*args):
    if type(args[0]) in [int, float]:
        result = sum(args)
    else:
        result = ""
        for item in args:
            result += item
    return result


sum_list("a", "b")
sum_list("abc", "cde")
sum_list(3, 4, 5)



