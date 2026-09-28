"""Бесконечный поток словарей со случайным целым полем value."""

from __future__ import annotations

from collections.abc import Iterator

from sampling.rng import make_rng


def stream(seed: int) -> Iterator[dict[str, int]]:
    """Неисчерпаемый генератор записей вида {"value": int}."""
    drawer = make_rng(seed)
    while True:
        yield {"value": drawer.randint(0, 999_999)}
