"""
Simple Fibonacci utilities and CLI.

Usage:
  python fibonacci.py 10   # prints first 10 Fibonacci numbers
"""

from __future__ import annotations

import argparse


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed).

    F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) for n>=2.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_sequence(count: int) -> list[int]:
    """Return a list with the first `count` Fibonacci numbers."""
    if count < 0:
        raise ValueError("count must be non-negative")
    seq: list[int] = []
    a, b = 0, 1
    for _ in range(count):
        seq.append(a)
        a, b = b, a + b
    return seq


def main() -> None:
    parser = argparse.ArgumentParser(description="Print the first N Fibonacci numbers")
    parser.add_argument(
        "count",
        type=int,
        help="number of Fibonacci numbers to print (non-negative)",
    )
    args = parser.parse_args()

    seq = fibonacci_sequence(args.count)
    print(" ".join(str(x) for x in seq))


if __name__ == "__main__":
    main()

