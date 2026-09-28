"""Снятие конечного префикса у бесконечного генератора."""

from __future__ import annotations

from collections.abc import Iterator


def pull(source: Iterator[int], count: int) -> list[int]:
    """Забирает ровно count значений. Отрицательная длина недопустима."""
    if count < 0:
        raise ValueError("Нельзя взять отрицательное число членов.")
    taken: list[int] = []
    while len(taken) < count:
        taken.append(next(source))
    return taken
