import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

num_list = [1.5, 0.5, 7.8, 6]
name_list = ['one', 'two', 'three', 'four']

p1 = plt.bar(range(len(num_list)), num_list, color = 'rgb', tick_label = name_list)

# 展示图形
plt.savefig("test.png")