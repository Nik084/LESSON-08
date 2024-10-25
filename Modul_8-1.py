def add_everything_up(a, b):
    try:
        # if isinstance(a, str) and isinstance(b, str):
        if isinstance((a + b), str):
            return f'only "str": {a} & {b}'
        else:
            result = a + b
    except TypeError:
        return f'{a}{b}'
    else:
        return result

print(add_everything_up(123, 'word'))
print(add_everything_up('magic', 456.5))
print(add_everything_up(700, 876.54))
print(add_everything_up('gh', 'hj'))

