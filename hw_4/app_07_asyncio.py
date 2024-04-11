"""
Задание №7
Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
В каждом решении нужно вывести время выполнения вычислений.
"""
from random import randint, seed
import asyncio
import time

seed(0)
my_list = [randint(1, 100) for i in range(1000000)]
# print(sum(my_list))

summ_list = 0


async def summa_list(new_list):
    global summ_list
    for i in range(len(new_list)):
        summ_list += new_list[i]
    print(f"Значение счетчика: {summ_list:_}")


async def main():
    tasks = []
    parts = 10
    for i in range(parts):
        task = asyncio.create_task(summa_list(my_list[(len(my_list) // parts) * i:len(my_list) // parts * (i + 1)]))
        tasks.append(task)
    task = asyncio.create_task(summa_list(my_list[(len(my_list) // parts) * parts:]))
    tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f"Значение счетчика в финале: {summ_list:_}")
    print(f"Result in {time.time() - start_time:.2f} seconds")
