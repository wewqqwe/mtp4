"""Сумма целых чисел через functools.reduce."""

from __future__ import annotations

from functools import reduce

from folding.pair import pair_sum


def total(numbers: list[int]) -> int:
    """Суммирует список. Начальное значение 0 задаёт сумму пустого списка."""
    return reduce(pair_sum, numbers, 0)
