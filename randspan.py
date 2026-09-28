"""Генератор псевдослучайных целых на включительном отрезке."""

from __future__ import annotations

from collections.abc import Iterator

from sampling.rng import make_rng


def span(low: int, high: int, count: int, seed: int) -> Iterator[int]:
    """Выдаёт count значений random.randint(low, high) при заданном зерне.

    Обе границы входят в диапазон, как у randint.
    """
    drawer = make_rng(seed)
    produced = 0
    while produced < count:
        yield drawer.randint(low, high)
        produced += 1
