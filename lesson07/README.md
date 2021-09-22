### Урок 7. Алгоритмы сортировки

Для каждого упражнения написать программную реализацию.

Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию).
Каждую задачу необходимо сохранять в отдельный файл. 
Рекомендуем использовать английские имена, например, task_1, task_2, и т.д.

Для оценки «Отлично» необходимо выполнить все задания.

1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, 
   заданный случайными числами на промежутке `[-100; 100)`. 
   Выведите на экран исходный и отсортированный массивы.
   _Примечания_:
   - алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
   - постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. 
   Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
   заданный случайными числами на промежутке `[0; 50)`. 
   Выведите на экран исходный и отсортированный массивы.

3. Массив размером `2m + 1`, где `m` — натуральное число, заполнен случайным образом. 
   Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
   в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

_Примечание_: задачу можно решить без сортировки исходного массива. 
Но если это слишком сложно, используйте метод сортировки, 
который не рассматривался на уроках (сортировка слиянием также недопустима).


**Решения:**
- [Задача №1](https://github.com/bostspb/algorithms/blob/master/lesson07/task01.py)
- [Задача №2](https://github.com/bostspb/algorithms/blob/master/lesson07/task02.py)
- [Задача №3](https://github.com/bostspb/algorithms/blob/master/lesson07/task03.py)