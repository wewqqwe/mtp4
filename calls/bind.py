"""Фиксация левого слагаемого для второго вызова."""

from __future__ import annotations

from collections.abc import Callable


def postponed(left: int) -> Callable[[int], int]:
    """Возвращает функцию одного аргумента: она прибавляет его к left."""

    def apply_right(right: int) -> int:
        return left + right

    return apply_right
