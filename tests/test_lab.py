"""Проверки лабораторной работы №4. Функции поставки, без подмен."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from curry import add
from endless import stream
from fib_gen import fibonacci, take_fibonacci
from randspan import span
from reduce_sum import total

ROOT = Path(__file__).resolve().parents[1]


def test_total_reduce() -> None:
    assert total([]) == 0
    assert total([2, 4, 6]) == 12


def test_fibonacci_generator_prefix() -> None:
    assert take_fibonacci(0) == []
    assert take_fibonacci(1) == [0]
    assert take_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    generated = fibonacci()
    assert [next(generated) for _ in range(7)] == [0, 1, 1, 2, 3, 5, 8]
    terms = take_fibonacci(7)
    for index in range(2, len(terms)):
        assert terms[index] == terms[index - 1] + terms[index - 2]


def test_span_inclusive_and_fixed() -> None:
    drawn = list(span(1, 3, 20, seed=2))
    assert len(drawn) == 20
    assert all(1 <= item <= 3 for item in drawn)
    assert list(span(4, 4, 3, 0)) == [4, 4, 4]


def test_curry_matches_direct_call() -> None:
    assert add(2)(5) == add(2, 5) == 7


def test_stream_continues_after_six_steps() -> None:
    source = stream(5)
    collected = []
    for _ in range(6):
        item = next(source)
        assert list(item) == ["value"]
        assert isinstance(item["value"], int)
        collected.append(item)
    extra = next(source)
    assert isinstance(extra["value"], int)
    assert extra is not collected[-1]


def test_demo_prints_reduce_result() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "main.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert str(total([2, 4, 6])) in completed.stdout
