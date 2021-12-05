# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
from multiprocessing import Pool
import time
from matplotlib import pyplot as plt

df = pd.read_csv("data.csv", sep=",", encoding="cp1251")


def min_multiprocess(num_of_proc, df):
    start_time = time.time()
    with Pool(num_of_proc):
        df_copy = df.copy()
        df_copy['Заболели'] = df_copy['Заболели'].apply(lambda _str: int(_str.replace("'", "").strip()))
        df_copy = df_copy[df_copy['Активные случаи'] >= 0]

        df_copy['Заболели'].min()

    end_time = time.time()
    print(end_time - start_time)
    return end_time - start_time


a = min_multiprocess(1, df)
b = min_multiprocess(2, df)
c = min_multiprocess(3, df)
d = min_multiprocess(4, df)
e = min_multiprocess(5, df)
f = min_multiprocess(6, df)
g = min_multiprocess(7, df)
h = min_multiprocess(8, df)
i = min_multiprocess(9, df)
j = min_multiprocess(10, df)

plt.ylabel('y')
plt.xlabel('x')
plt.title('time by number of processes')
plt.plot([0, a, b, c, d, e, f, g, h, i, j], color='blue')
plt.show()
