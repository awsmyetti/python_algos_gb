"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from random import randint
import time


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        time.sleep(0.01)
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        time.sleep(0.01)
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    time.sleep(0.01)
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def test():
    num = randint(10000, 1000000000)
    revers(num)
    revers_2(num)
    revers_3(num)


cProfile.run('test()')
