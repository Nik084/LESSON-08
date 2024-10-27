class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin_numbers, numbers):
        self.model = model #название автомобиля (строка)
        self.__vin = vin_numbers # номер автомобиля (целое число)
        self.__is_valid_vin(vin_numbers)
        self.__numbers = numbers #номера автомобиля (строка).
        self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_numbers):
        self.vin = vin_numbers
        if isinstance(self.vin, int) is False:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if (1000000 <= self.vin <= 9999999) is False:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        self.numbers = numbers
        if isinstance(self.numbers, str) is False:
            raise IncorrectCarNumbers ('Некорректный тип данных для номеров')
        if len(self.numbers) != 6:
            raise IncorrectCarNumbers ('Неверная длина номера')
        return True

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
