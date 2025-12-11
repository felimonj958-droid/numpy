"""Small helper module with correct Fibonacci functions and a quick CLI test.

This file provides:
- fibonacci_sequence(n): returns a list of the first n Fibonacci numbers
- calculate_fibonacci_stats(n): returns a dict with simple statistics

The functions are defensive for non-positive inputs.
"""

from __future__ import annotations
from typing import List, Dict, Any, Optional


def fibonacci_sequence(n: int) -> List[int]:
    """Return the first ``n`` Fibonacci numbers starting from 0.

    Examples
    --------
    >>> fibonacci_sequence(0)
    []
    >>> fibonacci_sequence(1)
    [0]
    >>> fibonacci_sequence(5)
    [0, 1, 1, 2, 3]
    """
    if n <= 0:
        return []
    result: List[int] = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def calculate_fibonacci_stats(sequence_length: int) -> Dict[str, Any]:
    """Return simple statistics for the Fibonacci sequence of given length.

    Returns a dict with keys: 'sequence', 'average', 'maximum', 'minimum', 'length'.
    For an empty sequence, numeric stats are ``None`` and length is 0.
    """
    sequence = fibonacci_sequence(sequence_length)
    if not sequence:
        return {
            'sequence': [],
            'average': None,
            'maximum': None,
            'minimum': None,
            'length': 0,
        }

    length = len(sequence)
    stats: Dict[str, Any] = {
        'sequence': sequence,
        'average': sum(sequence) / length,
        'maximum': max(sequence),
        'minimum': min(sequence),
        'length': length,
    }
    return stats


if __name__ == '__main__':
    # Quick verification when run as a script
    for n in (0, 1, 5, 10):
        stats = calculate_fibonacci_stats(n)
        print(f"n={n}: length={stats['length']}, average={stats['average']}")
    