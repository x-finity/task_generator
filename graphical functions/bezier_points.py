# -*- coding: utf-8 -*-
"""bezier_points_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QXMFWtJC66JtBIdeNRObEJnzs6ePFUrr
"""

import random
import bezier
import numpy as np
import math
import fractions
from sympy import *
import matplotlib.pyplot as plt
import re
import time

def plot_bezier_total_number_extremes_or_number_max_or_number_min_or_increasing_sum_whole_points():
    n_1 = random.randint(20, 30)
    x_start = random.randint(-9, -6)
    x_end = random.randint(2, 17)
    latex_interval = "({}, {})".format(x_start, x_end + 1)
    x_arr = sorted(np.random.uniform(x_start, x_end, n_1))
    y_arr = np.random.uniform(-15, 15, n_1)
    nodes1 = np.asfortranarray([[x_start, *x_arr, x_end + 1], [1.0, *y_arr, 1.0]])
    curve1 = bezier.Curve(nodes1, degree=n_1 + 1)
    t_values = np.linspace(0.0, 1, 1000)
    points = curve1.evaluate_multi(t_values)
    if random.randint(0, 5) == 0:
        text = r" Найдите количество точек экстремума функции f(x) на отрезке" + ' ' + '\(' + str(latex(latex_interval)) + '\).'
        number = 0
        for i in range(1, len(points[0])):
            if (points[1][i]) * (points[1][i - 1]) < 0:
                number += 1
    elif random.randint(0, 5) == 1:
        text = r" Найдите количество точек максимума функции f(x) на отрезке" + ' ' + '\(' + str(latex(latex_interval)) + '\).'
        number = 0
        for i in range(1, len(points[0])):
            if (points[1][i]) * (points[1][i - 1]) < 0 and (points[1][i - 1]) > 0:
                number += 1
    elif random.randint(0, 5) == 2:
        text = r" Найдите количество точек минимума функции f(x) на отрезке" + ' ' + '\(' + str(latex(latex_interval)) + '\).'
        number = 0
        for i in range(1, len(points[0])):
            if (points[1][i]) * (points[1][i - 1]) < 0 and (points[1][i - 1]) < 0:
                number += 1
    elif random.randint(0, 5) == 3:
        text = r" Найдите промежутки возрастания функции f(x). В ответе укажите сумму целых точек, входящих в эти промежутки."
        numbers = []
        for i in range(1, len(points[0])):
            if points[1][i] > 0:
                numbers.append(points[0][i])
        numbers.sort()
        segments = []
        segment = [numbers[0]]
        for i in range(1, len(numbers)):
            if numbers[i] - segment[-1] <= 0.2:
                segment.append(numbers[i])
            else:
                segments.append(segment)
                segment = [numbers[i]]
        segments.append(segment)
        cleaned_segments = []
        for segment in segments:
            cleaned_segments.append([segment[0], segment[-1]])
        tuples = [tuple(segment) for segment in cleaned_segments]
        integer_values = []
        for segment in tuples:
            start = segment[0]
            end = segment[1]
            if start - int(start) <= 0 and int(start) != 0 and int(end) > 0:
                integer_values.extend(range(int(start), int(end) + 1))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) < 0:
                integer_values.extend(range(int(start), int(end)))
            elif start - int(start) <= 0 and int(start) == 0 and int(end) != 0:
                integer_values.extend(range(int(start), int(end) + 1))
            elif start - int(start) > 0 and int(end) != 0:
                integer_values.extend(range(int(start) + 1, int(end) + 1))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) == 0 and end > 0:
                integer_values.extend(range(int(start), int(end) + 1))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) == 0 and end < 0:
                integer_values.extend(range(int(start), int(end)))
            elif start - int(start) <= 0 and int(start) == 0 and end == 0:
                integer_values.extend(range(int(start) + 1, end))
            elif start - int(start) > 0 and end == 0:
                integer_values.extend(range(int(start) + 1, end))
            elif start - int(start) <= 0 and int(start) != 0 and int(start) == end:
                continue
        integer_values_without_last = integer_values[:-1]
        number = sum(integer_values_without_last)
    elif random.randint(0, 5) == 4:
        text = r" Найдите промежутки убывания функции f(x). В ответе укажите сумму целых точек, входящих в эти промежутки."
        numbers = []
        for i in range(1, len(points[0])):
            if points[1][i] <= 0:
                numbers.append(points[0][i])
        numbers.sort()
        segments = []
        segment = [numbers[0]]
        for i in range(1, len(numbers)):
            if numbers[i] - segment[-1] <= 0.2:
                segment.append(numbers[i])
            else:
                segments.append(segment)
                segment = [numbers[i]]
        segments.append(segment)
        cleaned_segments = []
        for segment in segments:
            cleaned_segments.append([segment[0], segment[-1]])
        tuples = [tuple(segment) for segment in cleaned_segments]
        integer_values = []
        for segment in tuples:
            start = segment[0]
            end = segment[1]
            if start - int(start) <= 0 and int(start) != 0 and int(end) > 0:
                integer_values.extend(range(int(start), int(end) + 1))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) < 0:
                integer_values.extend(range(int(start), int(end)))
            elif start - int(start) <= 0 and int(start) == 0 and int(end) != 0:
                integer_values.extend(range(int(start), int(end) + 1))
            elif start - int(start) > 0 and int(end) != 0:
                integer_values.extend(range(int(start) + 1, int(end) + 1))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) == 0 and end > 0:
                integer_values.extend(range(int(start), int(end) + 1))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) == 0 and end < 0:
                integer_values.extend(range(int(start), int(end)))
            elif start - int(start) <= 0 and int(start) == 0 and end == 0:
                integer_values.extend(range(int(start) + 1, end))
            elif start - int(start) > 0 and end == 0:
                integer_values.extend(range(int(start) + 1, end))
            elif start - int(start) <= 0 and int(start) != 0 and int(start) == end:
                continue
        number = sum(integer_values)
    else:
        text = r" Найдите промежутки убывания функции f(x). В ответе укажите длину наибольшего из них."
        numbers = []
        for i in range(1, len(points[0])):
            if points[1][i] <= 0:
                numbers.append(points[0][i])
        numbers.sort()
        segments = []
        segment = [numbers[0]]
        for i in range(1, len(numbers)):
            if numbers[i] - segment[-1] <= 0.2:
                segment.append(numbers[i])
            else:
                segments.append(segment)
                segment = [numbers[i]]
        segments.append(segment)
        cleaned_segments = []
        for segment in segments:
            cleaned_segments.append([segment[0], segment[-1]])
        tuples = [tuple(segment) for segment in cleaned_segments]
        integer_values = []
        for segment in tuples:
            start = segment[0]
            end = segment[1]
            if start - int(start) <= 0 and int(start) != 0 and int(end) > 0:
                integer_values.append(list(range(int(start), int(end) + 1)))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) < 0:
                integer_values.append(list(range(int(start), int(end))))
            elif start - int(start) <= 0 and int(start) == 0 and int(end) != 0:
                integer_values.append(list(range(int(start), int(end) + 1)))
            elif start - int(start) > 0 and int(end) != 0:
                integer_values.append(list(range(int(start) + 1, int(end) + 1)))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) == 0 and end > 0:
                integer_values.append(list(range(int(start), int(end) + 1)))
            elif start - int(start) <= 0 and int(start) != 0 and int(end) == 0 and end < 0:
                integer_values.append(list(range(int(start), int(end))))
            elif start - int(start) <= 0 and int(start) == 0 and end == 0:
                integer_values.append(list(range(int(start) + 1, end)))
            elif start - int(start) > 0 and end == 0:
                integer_values.append(list(range(int(start) + 1, end)))
            elif start - int(start) <= 0 and int(start) != 0 and int(start) == end:
                continue
        result = [len(sublist) for sublist in integer_values]
        number = max(result) - 1
    ax = curve1.plot(num_pts=2456)
    ax.spines[["left", "bottom"]].set_position('zero')
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    arrow_length = 10
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom')
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='center', va='bottom')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True, linewidth=0.5, linestyle='dotted')
    plt.axis('equal')
    ax.set_xticks(range(x_start - 9, x_end + 9))
    ax.set_yticks(range(-17, 17))
    ax.set_xticklabels([i if i % 2 == 0 else '' for i in range(x_start - 9, x_end + 9)])
    ax.set_yticklabels([i if i % 2 == 0 else '' for i in range(-17, 17)])
    ax.set_xlim(x_start - 1, x_end + 2)
    ax.set_ylim(min(points[1]) - 1, max(points[1]) + 1)
    plt.legend(labels=["y = f'(x)"])
    plt.show()
    task = r'На рисунке изображен график производной функции f(x), определенной на интервале' + ' ' + '\(' + str(latex(latex_interval)) + '\).' + text
    answer = number
    return task, answer