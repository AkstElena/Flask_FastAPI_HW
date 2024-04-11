"""
Задание №7
Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
В каждом решении нужно вывести время выполнения вычислений.
"""
from random import randint, seed
import multiprocessing
import time

seed(0)
my_list = [randint(1, 100) for i in range(1000000)]

start_time = time.time()

summ_list = 0
counter = multiprocessing.Value('i', 0)


def increment(current_list, cnt):
    for i in range(len(current_list)):
        with cnt.get_lock():
            cnt.value += current_list[i]
    print(f"Значение счетчика: {cnt.value:_}")


if __name__ == '__main__':
    processes = []
    parts = 5
    for i in range(parts):
        p = multiprocessing.Process(target=increment, args=(my_list[(len(my_list) // parts) * i:len(my_list) // parts * (i + 1)], counter,))
        processes.append(p)
        p.start()
    p = multiprocessing.Process(target=increment, args=(my_list[(len(my_list) // parts) * parts:], counter,))
    processes.append(p)
    p.start()

    for p in processes:
        p.join()

    print(f"Значение счетчика в финале: {counter.value:_}")
    print(f"Result in {time.time() - start_time:.2f} seconds")
