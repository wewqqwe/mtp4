"""Демонстрация средств лабораторной работы №4."""

from __future__ import annotations

from curry import add
from endless import stream
from fib_gen import take_fibonacci
from randspan import span
from reduce_sum import total


def main() -> None:
    numbers = [2, 4, 6]
    print(f"Сумма: {total(numbers)}")
    print(f"Начало ряда Фибоначчи: {take_fibonacci(7)}")
    print(f"Случайный отрезок: {list(span(1, 3, 5, seed=2))}")
    print(f"Каррирование: {add(2)(5)} и {add(2, 5)}")
    source = stream(11)
    preview = [next(source) for _ in range(3)]
    print(f"Поток данных: {preview}")


if __name__ == "__main__":
    main()
