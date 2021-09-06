"""
Задача №5
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

row = ''
symbol_from = 32
symbol_to = 127
while symbol_from <= symbol_to:
    for symbol_from in range(symbol_from, symbol_from + 10):
        if symbol_from <= symbol_to:
            row += f'{str(symbol_from)} - {chr(symbol_from)}\t'
    row += '\n'

print(row)