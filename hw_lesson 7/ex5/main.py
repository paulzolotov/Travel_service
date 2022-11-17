#! /usr/local/bin/python3

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



