#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = list(map(float, input('Введите элементы массива: ').split()))

    k = 0
    for item in a:
        if item < 0:
            k += 1
    print(f"Количество элмементов: {k}")

    s = 0
    i_min = a.index(min(a))
    for item in a[i_min + 1:]:
        s += item
    print(f"Сумма: {s}")

    for i in range(len(a)):
        if a[i] < 0:
            a[i] = a[i]**2
    print(sorted(a))
