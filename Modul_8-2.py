def personal_sum(numbers):
    try:
        result = 0
        incorrect_data = 0
        for i in numbers:
            try:
                result += i
            except TypeError:
                incorrect_data += 1
        return (result, incorrect_data)
    except NameError:
        print(NameError)
def calculate_average(numbers, numb_result=1):
    try:
        collect_numb = (len(numbers) - personal_sum(numbers)[1])
        try:
            incorrect = []
            for i in numbers:
                if isinstance(i, str):
                    incorrect.append(i)
            if incorrect != []:
                print(f'В numbers №{numb_result} найдены данные некорректного типа для подсчёта суммы: {incorrect}')
            if personal_sum(numbers)[0] == 0:
                print(f'numbers №{numb_result} не содержит данные для вычисления')
            return f'Результат №{numb_result}: {round((personal_sum(numbers)[0] / collect_numb), 3)}'
        except ZeroDivisionError:
            return f'Результат №{numb_result}: 0'
    except TypeError:
        print (f'В numbers под №{numb_result} записан некорректный тип данных')

print(calculate_average((2, 3, 4, 6, 15)))
print(calculate_average(['dfr', 'drty', 'weert'], 2))
print(calculate_average((), 3))
print(calculate_average([1, 2, 3.81, "klot", 7, 6.2], 4))
print(calculate_average([235], 5)) #в списке один элемент - число
print(calculate_average(235, 6)) # вместо списка - число
print(calculate_average((235), 7)) # передана не коллекция
print(calculate_average(['235'], 8))
print(calculate_average('235', 9))

