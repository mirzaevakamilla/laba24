#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

k = 0
if __name__ == '__main__':
    a = list(map(int, input().split()))
    if len(a) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    for item in a:
        if (item < 18) and (item > 8) and (item % 10 == 0):
            k = k + 1

    print("Произведение: ", math.prod([item for item in a if (item < 18) and (item > 8) and (item % 10 == 0)]))
    print("Количество: ", k)
