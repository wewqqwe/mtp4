"""Бесконечный генератор Фибоначчи и срез его начала."""

from __future__ import annotations

from collections.abc import Iterator

from progression.advance import advance
from progression.prefix import pull


def fibonacci() -> Iterator[int]:
    """Бесконечная последовательность, которая начинается с 0, затем 1."""
    previous = 0
    current = 1
    while True:
        yield previous
        previous, current = advance(previous, current)


def take_fibonacci(n: int) -> list[int]:
    """Возвращает первые n членов генератора Фибоначчи."""
    return pull(fibonacci(), n)
