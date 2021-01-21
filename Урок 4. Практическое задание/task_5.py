"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def erat(stop):
    n = int(1000000)
    # список заполняется значениями от 0 до n
    a = list(range(0, n + 1))
    res = list()
    # Вторым элементом является единица,
    # которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    # начинаем с 3-го элемента
    i = 2

    while i <= n and len(res) < stop:
        # Если значение ячейки до этого
        # не было обнулено,
        # в этой ячейке содержится
        # простое число.
        if a[i] != 0:
            res.append(a[i])
            # первое кратное ему
            # будет в два раза больше
            j = i + i
            while j <= n:
                # это число составное,
                # поэтому заменяем его нулем
                a[j] = 0
                # переходим к следующему числу,
                # которое кратно i
                # (оно на i больше)
                j = j + i
        i += 1

    # Превращая список во множество,
    # избавляемся от всех нулей кроме одного.
    # удаляем ноль
    return res[-1]


num = 5000
print(simple(num))
print(erat(num))

print(timeit(stmt="simple(num)", setup="from __main__ import simple, num", number=1))
print(timeit(stmt="erat(num)", setup="from __main__ import erat, num", number=1))
