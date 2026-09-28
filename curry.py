"""Каррирование сложения двух целых."""

from __future__ import annotations

from collections.abc import Callable

from calls.bind import postponed


def add(a: int, b: int | None = None) -> int | Callable[[int], int]:
    """Складывает a и b либо возвращает функцию одного аргумента.

    Выполняется равенство add(a)(b) == add(a, b).
    """
    if b is None:
        return postponed(a)
    return a + b
