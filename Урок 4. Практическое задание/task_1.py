"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


NUMS = list(range(0, 1000))
NUMS2 = list(range(0, 1000000))

print(timeit(stmt="func_1(NUMS)", setup="from __main__ import func_1, NUMS", number=1000))
print(timeit(stmt="func_2(NUMS)", setup="from __main__ import func_2, NUMS", number=1000))
