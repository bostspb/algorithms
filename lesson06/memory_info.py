import sys


class MemoryInfo:
    """Класс для подсчета занимаемой оперативной памяти под переменные в скрипте"""

    def __init__(self):
        self.full_size = 0

    def print_result(self):
        print(f'\nTotal occupied amount of memory: {self.full_size}')

    def calc(self, obj):
        memory = sys.getsizeof(obj)
        self.full_size += memory
        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    self.calc(key)
                    self.calc(value)
            elif not isinstance(obj, str):
                for item in obj:
                    self.calc(item)
