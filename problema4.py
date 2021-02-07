#!/bin/python3

# Hay varios imports que agrega HackerRank para confundir, pero en realidad solo se necesita la librería de regex re
# Incluído el shebang de arriba

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
result = ""
for i in range(m):
    for row in matrix:
        char = row[i]
        result += char
        continue

result = re.sub(r"([A-z0-9])[^A-z0-9]+([A-z0-9])", "\\1 \\2", result)
print(result)
