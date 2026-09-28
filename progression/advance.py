"""Переход к следующей паре членов ряда Фибоначчи."""

from __future__ import annotations


def advance(previous: int, current: int) -> tuple[int, int]:
    """Следующая пара: прежний текущий член и сумма двух последних."""
    return current, previous + current
